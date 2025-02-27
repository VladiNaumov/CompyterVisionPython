import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)

# Рассчитываем только площадь 200*200 в верхнем левом углу
mask = np.zeros(img.shape, dtype=np.uint8)
mask[:200, :200] = 255

hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.plot(hist_mask)
plt.show()
