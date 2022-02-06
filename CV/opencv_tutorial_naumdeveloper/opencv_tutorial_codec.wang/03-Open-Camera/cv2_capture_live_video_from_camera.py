import cv2

# 1.Включите камеру
capture = cv2.VideoCapture(2)

# 2.Получить захваченное разрешение
width, height = capture.get(3), capture.get(4)
print(width, height)
# Захватите в двойном исходном разрешении,
# Параметр 1 может напрямую записывать числа или символы OpenCV
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

while(True):
    # получить рамку
    ret, frame = capture.read()
    # Преобразовать этот кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
