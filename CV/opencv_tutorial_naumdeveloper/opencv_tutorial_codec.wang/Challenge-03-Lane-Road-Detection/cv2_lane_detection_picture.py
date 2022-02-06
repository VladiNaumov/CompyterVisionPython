# Загрузка изображений и видео ：http://blog.codec.wang/cv2_lane_detection_material.zip

import cv2
import numpy as np

# Размер ядра фильтра Гаусса
blur_ksize = 5

# Canny обнаружение границ с высоким и низким порогом
canny_lth = 50
canny_hth = 150

# Параметры преобразования
rho = 1
theta = np.pi / 180
threshold = 15
min_line_len = 40
max_line_gap = 20


def process_an_image(img):
    # 1. Оттенки серого, фильтр и Canny
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 1)
    edges = cv2.Canny(blur_gray, canny_lth, canny_hth)

    # 2. Отметьте четыре точки координат для захвата ROI
    rows, cols = edges.shape
    points = np.array([[(0, rows), (460, 325), (520, 325), (cols, rows)]])
    # [[[0 540], [460 325], [520 325], [960 540]]]
    roi_edges = roi_mask(edges, points)

    # 3. Извлечение линии Хафа
    drawing, lines = hough_lines(roi_edges, rho, theta,
                                 threshold, min_line_len, max_line_gap)

    # 4. Расчет переулка
    draw_lanes(drawing, lines)

    # 5. Окончательно объедините результат с исходным изображением
    result = cv2.addWeighted(img, 0.9, drawing, 0.2, 0)

    return result


def roi_mask(img, corner_points):
    # создать маску
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, corner_points, 255)

    masked_img = cv2.bitwise_and(img, mask)
    return masked_img


def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    Статистическая вероятность Преобразование линии Хафа
    lines = cv2.HoughLinesP(img, rho, theta, threshold,
                            minLineLength=min_line_len, maxLineGap=max_line_gap)

    # Создаем новый пустой холст
    drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # Рисуем результат обнаружения линии
    # draw_lines(drawing, lines)

    return drawing, lines


def draw_lines(img, lines, color=[0, 0, 255], thickness=1):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)


def draw_lanes(img, lines, color=[255, 0, 0], thickness=8):
    # a. Разделите левую и правую дорожки
    left_lines, right_lines = [], []
    for line in lines:
        for x1, y1, x2, y2 in line:
            k = (y2 - y1) / (x2 - x1)
            if k < 0:
                left_lines.append(line)
            else:
                right_lines.append(line)

    if (len(left_lines) <= 0 or len(right_lines) <= 0):
        return

    # b. Очистите аномальные данные
    clean_lines(left_lines, 0.1)
    clean_lines(right_lines, 0.1)

    # c. Получить набор точек левой и правой линий дорожки и построить прямую линию
    left_points = [(x1, y1) for line in left_lines for x1, y1, x2, y2 in line]
    left_points = left_points + [(x2, y2)
                                 for line in left_lines for x1, y1, x2, y2 in line]

    right_points = [(x1, y1)
                    for line in right_lines for x1, y1, x2, y2 in line]
    right_points = right_points + \
        [(x2, y2) for line in right_lines for x1, y1, x2, y2 in line]

    left_results = least_squares_fit(left_points, 325, img.shape[0])
    right_results = least_squares_fit(right_points, 325, img.shape[0])

    # Обратите внимание на порядок точек здесь
    vtxs = np.array(
        [[left_results[1], left_results[0], right_results[0], right_results[1]]])
    # d.Заполните полосу движения
    cv2.fillPoly(img, vtxs, (0, 255, 0))

    # или просто нарисуйте линии дорожек
    # cv2.line(img, left_results[0], left_results[1], (0, 255, 0), thickness)
    # cv2.line(img, right_results[0], right_results[1], (0, 255, 0), thickness)


def clean_lines(lines, threshold):
    # Итеративно вычисляем среднее значение наклона, исключая данные с большой разницей из разности
    slope = [(y2 - y1) / (x2 - x1)
             for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        mean = np.mean(slope)
        diff = [abs(s - mean) for s in slope]
        idx = np.argmax(diff)
        if diff[idx] > threshold:
            slope.pop(idx)
            lines.pop(idx)
        else:
            break


def least_squares_fit(point_list, ymin, ymax):
    # подходит метод наименьших квадратов
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]

    # polyfit Третий параметр - это порядок подгоночного полинома, поэтому 1 означает линейный
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)  # получить подходящий результат

    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))

    return [(xmin, ymin), (xmax, ymax)]


if __name__ == "__main__":
    img = cv2.imread('test_pictures/lane2.jpg')
    result = process_an_image(img)
    cv2.imshow("lane", np.hstack((img, result)))
    cv2.waitKey(0)
