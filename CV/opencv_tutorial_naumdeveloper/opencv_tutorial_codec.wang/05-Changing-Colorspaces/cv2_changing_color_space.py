import cv2
import numpy as np

img = cv2.imread('lena.jpg')

# 1.Преобразование в оттенки серого
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)


# 2.Получить все режимы преобразования
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# Синее значение HSV

blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)  # [[[120 255 255]]]


# 3.Отследить синий объект
capture = cv2.VideoCapture(0)

# Диапазон синего, разный при разных условиях освещения, можно гибко регулировать
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

#Определять цвет в BGR не очень удобно, поэтому для начала
#Преобразуем изображение в палитру HSV и разобьем на три составляющие

while(True):
    # 1.Захват кадра в видео
    ret, frame = capture.read()

    # 2.Преобразование из BGR в HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3.inRange()：между нижним/верхним белым, остальные черными
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4Оставьте только синюю часть исходного изображения
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
