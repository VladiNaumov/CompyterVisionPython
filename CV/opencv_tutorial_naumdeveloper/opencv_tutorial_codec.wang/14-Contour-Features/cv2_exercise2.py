import cv2

# загрузить исходное изображение
img = cv2.imread('abc.jpg', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# найти контур ABC
b, c, a = contours[0], contours[3], contours[4]

# Загрузить стандартное изображение шаблона
img_a = cv2.imread('template_a.jpg', 0)
_, th = cv2.threshold(img_a, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(th, 3, 2)

# Контур буквы А
template_a = contours[0]

print(cv2.matchShapes(a, template_a, 1, 0.0))  # 0.02557(наиболее похожи)
print(cv2.matchShapes(b, template_a, 1, 0.0))  # 0.80585
print(cv2.matchShapes(c, template_a, 1, 0.0))  # 3.26050
