import cv2
import numpy as np

# Загружаем изображение рукописной цифры
img = cv2.imread('handwriting.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# Создаем две карты цветов для рисования
img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)

# Возьмем контур цифры 3 в качестве примера
cnt = contours[0]
cv2.drawContours(img_color1, [cnt], 0, (0, 0, 255), 2)

# 1.Контурная зона
area = cv2.contourArea(cnt)  # 4386.5
print(area)


# 2.Периметр контура
perimeter = cv2.arcLength(cnt, True)  # 585.7716
print(perimeter)


# 3.Имиджевый момент
M = cv2.moments(cnt)
print(M)
print(M['m00'])  # То же, что и предыдущая область: 4386.5
cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']  # Центроид
print(cx, cy)

# 4.Ограничивающий прямоугольник изображения и минимальный ограничивающий прямоугольник
x, y, w, h = cv2.boundingRect(cnt)  # описанный прямоугольник
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)  # Минимальный описанный прямоугольник
box = np.int0(cv2.boxPoints(rect))  # Четыре угла прямоугольника закруглены

# Вы также можете использовать astype(np.int) для округления
cv2.drawContours(img_color1, [box], 0, (255, 0, 0), 2)

cv2.imshow('contours', img_color1)
cv2.waitKey(0)


# 5.Минимальная описанная окружность
(x, y), radius = cv2.minEnclosingCircle(cnt)
(x, y, radius) = np.int0((x, y, radius))
# Или используйте это предложение для округления：(x, y, radius) = map(int, (x, y, radius))
cv2.circle(img_color2, (x, y), radius, (0, 0, 255), 2)


# 6.Подгонка эллипса
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img_color2, ellipse, (0, 255, 0), 2)

cv2.imshow('contours2', img_color2)
cv2.waitKey(0)


# 7.Соответствие формы
img = cv2.imread('shapes.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
img_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
print(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0))  # 0.0
print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))  # 2.17e-05
print(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))  # 0.418
