import cv2
import numpy as np

# 1Добавляем картинки
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))  # 250+10 = 260 => 255
print(x + y)  # 250+10 = 260 % 256 = 4


# 2.Смешивание изображений
img1 = cv2.imread('lena_small.jpg')
img2 = cv2.imread('opencv-logo-white.png')
res = cv2.addWeighted(img1, .6, img2, .4, 0)

cv2.imshow('blending', res)
cv2.waitKey(0)


# 3.Побитовая операция
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv-logo-white.png')

# Поместите логотип в верхний левый угол, чтобы нас интересовала только эта область
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# создать маску
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Сохранить фон, кроме логотипа
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, img2)  # объединить
img1[:rows, :cols] = dst  # Помещаем на исходное изображение после слияния

cv2.imshow('result', img1)
cv2.waitKey(0)
