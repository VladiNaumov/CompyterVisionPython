import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)


# 1.Расчет гистограммы
# Расчет с использованием функций OpenCV
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # производительность：0.022158 s

# Расчет с использованием функций numpy
hist, bins = np.histogram(img.ravel(), 256, [0, 256])  # производительность：0.020628 s

# 使用numpy函数计算
hist = np.bincount(img.ravel(), minlength=256)  # производительность:：0.003163 s


# 2.Расчет с использованием функций numpy
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# Нарисуйте гистограмму
plt.plot(hist)
plt.show()


# 3.или использовать ранее вычисленный результат гистограммы
equ = cv2.equalizeHist(img)
cv2.imshow('equalization', np.hstack((img, equ)))  # отображать рядом
cv2.waitKey(0)

# рисуем гистограмму после выравнивания
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()


# 4.Адаптивная коррекция гистограммы
img = cv2.imread('tsukuba.jpg', 0)
equ = cv2.equalizeHist(img)  # Применить глобальное выравнивание гистограммы

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  #Адаптивная эквализация, необязательные параметры
cl1 = clahe.apply(img)

cv2.imshow('equalization', np.hstack((equ, equ, cl1)))  # отображать рядом
cv2.waitKey(0)
