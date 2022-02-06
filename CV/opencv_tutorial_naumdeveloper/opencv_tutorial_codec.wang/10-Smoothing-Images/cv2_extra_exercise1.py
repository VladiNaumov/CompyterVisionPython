import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('lena.jpg', 0)

# Сравнение различных типов границ

# Тип границы по умолчанию
default = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_DEFAULT)
# Скопируйте исходную границу
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
# Другой - симметричная граница
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
# Этот бордюр тоже очень интересный, его можно распечатать и изучить
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
# граница с фиксированным значением
constant = cv2.copyMakeBorder(
    img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)

# показать все графики
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('original', fontsize=8)
plt.subplot(232), plt.imshow(
    replicate, 'gray'), plt.title('replicate', fontsize=8)
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect', fontsize=8)
plt.subplot(234), plt.imshow(default, 'gray'), plt.title(
    'default', fontsize=8)
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap', fontsize=8)
plt.subplot(236), plt.imshow(
    constant, 'gray'), plt.title('constant', fontsize=8)

plt.show()
