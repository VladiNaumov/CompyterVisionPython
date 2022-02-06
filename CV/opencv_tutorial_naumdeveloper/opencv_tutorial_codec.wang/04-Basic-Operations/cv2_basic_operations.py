import cv2

img = cv2.imread('lena.jpg')

# 1.Получить значение пикселя
px = img[100, 90]
print(px)  # [103 98 197]

# Получить только значение синего канала
px_blue = img[100, 90, 0]
print(px_blue)  # 103


# 2.. Измените значение пикселя
img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]


# 3.Форма изображения
print(img.shape)  # (263, 247, 3)
# Форма включает количество строк, столбцов и каналов.
height, width, channels = img.shape
# img — изображение в градациях серого ：height, width = img.shape

# всего пикселей
print(img.size)  # 263*247*3=194883
# тип данных
print(img.dtype)  # uint8


# 4.ROI Перехват
face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)


# 5.Разделение и слияние каналов
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# Более рекомендуемый способ получить канал
b = img[:, :, 0]
cv2.imshow('b', b)
cv2.waitKey(0)
