import cv2
import numpy as np

img = np.zeros((200, 200, 3), np.uint8)

# Нарисовать логотип OpenCV на самом деле очень просто
# 1. Сначала нарисуйте круг от 0° до 300°
# 2. Нарисуйте в центре маленький кружок того же цвета, что и фон
# 3. Повторите первые две части и поверните их на определенный угол

# рисуем зеленую часть
cv2.ellipse(img, (43, 125), (45, 45), 0, 0, 300,
            (0, 255, 0), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (43, 125), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

# рисуем красную часть
cv2.ellipse(img, (90, 40), (45, 45), 120, 0, 300,
            (0, 0, 255), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (90, 40), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

# рисуем синюю часть
cv2.ellipse(img, (137, 125), (45, 45), -60, 0, 300,
            (255, 0, 0), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (137, 125), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
