import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('lena', img)

k = cv2.waitKey(0)
# ord() используется для получения кодировки символа
if k == ord('s'):
    cv2.imwrite('lena_save.bmp', img)
