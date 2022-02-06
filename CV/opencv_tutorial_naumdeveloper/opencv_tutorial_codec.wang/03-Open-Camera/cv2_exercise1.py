import cv2


def track_back(x):
    '''
    ### Функция обратного вызова, x представляет положение ползунка
    '''
    # Изменить положение кадра видео
    capture.set(cv2.CAP_PROP_POS_FRAMES, x)


cv2.namedWindow('window')

capture = cv2.VideoCapture('demo_video.mp4')
# Получить общее количество кадров в видео
frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)

# создать слайдер
cv2.createTrackbar('process', 'window', 1, int(frames), track_back)

while(capture.isOpened()):
    ret, frame = capture.read()

    cv2.imshow('window', frame)
    if cv2.waitKey(30) == ord('q'):
        break
