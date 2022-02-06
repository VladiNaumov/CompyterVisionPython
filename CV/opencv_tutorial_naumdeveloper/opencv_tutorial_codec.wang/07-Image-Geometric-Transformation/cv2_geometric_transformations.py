import cv2
import numpy as np

img = cv2.imread('drawing.jpg')

# 1.Масштабировать изображение по заданной ширине и высоте
res = cv2.resize(img, (132, 150))
# Масштабирование в соответствии с пропорцией, например, оси x и y удваиваются
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)


# 2.Перевернуть изображение

# Параметр 2=0: отразить по вертикали (по оси X), параметр 2>0: отразить по горизонтали (по оси Y)
# Параметр 2<0: отразить по горизонтали и по вертикали
dst = cv2.flip(img, -1)
# np.hstack: Горизонтальное рядом, контрастное отображение
cv2.imshow('flip', np.hstack((img, dst)))  # np.hstack: 横向并排，对比显示
cv2.waitKey(0)


# 3.Панорамирование изображения
rows, cols = img.shape[:2]
# Определяем матрицу перевода, которая должна быть типа numpy float32
# перемещение по оси X 100, перемещение по оси Y 50
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)


# 4.45°повернуть изображение по часовой стрелке и уменьшить его наполовину
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)
