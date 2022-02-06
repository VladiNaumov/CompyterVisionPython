import cv2

# 1.. Изображение в градациях серого загружает цветное изображение
img = cv2.imread('lena.jpg', 0)


# 2.Показать картинку
cv2.imshow('lena', img)
cv2.waitKey(0)

# Сначала определяем окно, затем отображаем картинку
cv2.namedWindow('lena2', cv2.WINDOW_NORMAL)
cv2.imshow('lena2', img)
cv2.waitKey(0)


# 3.Сохраните изображение
cv2.imwrite('lena_gray.jpg', img)
