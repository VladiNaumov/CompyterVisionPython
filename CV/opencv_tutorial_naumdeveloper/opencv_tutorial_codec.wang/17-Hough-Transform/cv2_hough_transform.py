import cv2
import numpy as np


# 1. Преобразование линии Хафа
img = cv2.imread('shapes.jpg')
drawing = np.zeros(img.shape[:], dtype=np.uint8)  # 创建画板
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Преобразование линии Хафа
lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 90)

# Нарисуйте обнаруженную линию (обратите внимание на полярные координаты)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))

cv2.imshow('hough lines', np.hstack((img, drawing)))
cv2.waitKey(0)


# 2. Преобразование статистической вероятности линии Хафа
drawing = np.zeros(img.shape[:], dtype=np.uint8)

lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90,
                        minLineLength=50, maxLineGap=10)

# рисуем обнаруженную линию
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(drawing, (x1, y1), (x2, y2), (0, 255, 0), 1, lineType=cv2.LINE_AA)

cv2.imshow('probabilistic hough lines', np.hstack((img, drawing)))
cv2.waitKey(0)


# 3. Преобразование окружности Хафа
drawing = np.zeros(img.shape[:], dtype=np.uint8)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=30)
circles = np.int0(np.around(circles))

# Нарисовать обнаруженный круг
for i in circles[0, :]:
    cv2.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2)  # рисуем внешний круг
    cv2.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3)  # рисуем центр круга

cv2.imshow('circles', np.hstack((img, drawing)))
cv2.waitKey(0)
