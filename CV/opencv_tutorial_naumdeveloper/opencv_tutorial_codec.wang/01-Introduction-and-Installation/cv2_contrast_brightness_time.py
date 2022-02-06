import cv2
import numpy as np

# запускаем таймер
start = cv2.getTickCount()

# Прочитайте изображение и отрегулируйте контрастность и яркость
img = cv2.imread('lena.jpg')
res = np.uint8(np.clip((0.8 * img + 80), 0, 255))

# остановить время
end = cv2.getTickCount()

# Единицы：s
print((end - start) / cv2.getTickFrequency())
