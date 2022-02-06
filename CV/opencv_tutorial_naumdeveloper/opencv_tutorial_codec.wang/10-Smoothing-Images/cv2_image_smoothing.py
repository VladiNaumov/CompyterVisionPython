import cv2
import numpy as np

img = cv2.imread('lena.jpg')
# 1.Средний фильтр
blur = cv2.blur(img, (3, 3))

# Приведенный выше фильтр средних значений также может быть реализован с помощью блочной фильтрации:：normalize=True
# blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)


# 2.Фильтр Гаусса
gau_blur = cv2.GaussianBlur(img, (3, 3), 0)

# Три изображения накладываются друг на друга и отображаются горизонтально
res = np.hstack((img, blur, gau_blur))
cv2.imshow('res', res)
cv2.waitKey(0)

# Фильтр среднего против фильтра Гаусса
img = cv2.imread('gaussian_noise.bmp')
blur = cv2.blur(img, (5, 5))  # средний фильтр
gaussian = cv2.GaussianBlur(img, (5, 5), 1)  # Фильтр Гаусса

res = np.hstack((img, blur, gaussian))
cv2.imshow('gaussian vs average', res)
cv2.waitKey(0)


# 3.Средний фильтр против медианного фильтра
img = cv2.imread('salt_noise.bmp', 0)

blur = cv2.blur(img, (5, 5))  # средний фильтр
median = cv2.medianBlur(img, 5)  # медианный фильтр

res = np.hstack((img, blur, median))
cv2.imshow('median vs average', res)
cv2.waitKey(0)


# 4.Двусторонняя фильтрация против фильтрации по Гауссу
img = cv2.imread('lena.jpg', 0)
gau = cv2.GaussianBlur(img, (5, 5), 0)  # Фильтр Гаусса
blur = cv2.bilateralFilter(img, 5, 75, 75)  # двусторонний фильтр

res = np.hstack((img, gau, blur))
cv2.imshow('res', res)
cv2.waitKey(0)
