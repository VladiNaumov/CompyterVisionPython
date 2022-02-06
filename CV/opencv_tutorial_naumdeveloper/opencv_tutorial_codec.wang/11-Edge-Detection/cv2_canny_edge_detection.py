import cv2
import numpy as np

# 1.Хитрое обнаружение краев
img = cv2.imread('handwriting.jpg', 0)
edges = cv2.Canny(img, 30, 70)

cv2.imshow('canny', np.hstack((img, edges)))
cv2.waitKey(0)


# 2. Сначала порог, затем обнаружение границ
# Сегментация порога (с использованием автоматического порога Otsu, упомянутого в дополнительной части)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)

cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)
