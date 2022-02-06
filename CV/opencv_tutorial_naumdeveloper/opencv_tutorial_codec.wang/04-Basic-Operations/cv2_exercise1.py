import cv2

img = cv2.imread('lena.jpg')

# # Красный канал шляпы ROI
hat_r = img[25:120, 50:220, 2]
cv2.imshow('hat', hat_r)
cv2.waitKey(0)
