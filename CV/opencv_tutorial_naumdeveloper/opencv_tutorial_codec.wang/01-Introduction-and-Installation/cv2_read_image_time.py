import cv2

# запускаем таймер
start = cv2.getTickCount()

# читать в изображении
img = cv2.imread('lena.jpg')

# остановить время
end = cv2.getTickCount()

# Единицы：s
print((end - start) / cv2.getTickFrequency())
