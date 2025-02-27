import cv2
import numpy as np

# 1.Коррозия и расширение
img = cv2.imread('j.bmp', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  # Коррозия
dilation = cv2.dilate(img, kernel)  # 膨胀

cv2.imshow('erosion/dilation', np.hstack((img, erosion, dilation)))
cv2.waitKey(0)


# 2.Определите структурные элементы
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # прямоугольная структура
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # Эллиптическая структура
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # форма креста
print(kernel)

# 3.Открытая операция и закрытая операция
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # определяем элементы структуры

# операция закрытия
img = cv2.imread('j_noise_out.bmp', 0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', np.hstack((img, opening)))
cv2.waitKey(0)

# операция закрытия
img = cv2.imread('j_noise_in.bmp', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing', np.hstack((img, closing)))
cv2.waitKey(0)


# 4.Морфологический градиент
img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('morphological gradient', np.hstack((img, gradient)))
cv2.waitKey(0)


# 5.Цилиндр
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('top hat', np.hstack((img, tophat)))
cv2.waitKey(0)


# 6.Черная шляпа
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('black hat', np.hstack((img, blackhat)))
cv2.waitKey(0)
