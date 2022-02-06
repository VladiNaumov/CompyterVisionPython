import cv2
import math
import datetime
import numpy as np

margin = 5  # верхнее, нижнее, левое и правое поля
radius = 220  # радиус круга
center = (center_x, center_y) = (225, 225)  # центр круга

# 1. Создайте новый артборд и залейте его белым цветом
img = np.zeros((450, 450, 3), np.uint8)
img[:] = (255, 255, 255)

# 2. Рисуем диск
cv2.circle(img, center, radius, (0, 0, 0), thickness=5)

pt1 = []

# 3. Нарисуйте 60-секундные и минутные линии
for i in range(60):
    # Самая внешняя окружность, вычислить точку A
    x1 = center_x+(radius-margin)*math.cos(i*6*np.pi/180.0)
    y1 = center_y+(radius-margin)*math.sin(i*6*np.pi/180.0)
    pt1.append((int(x1), int(y1)))

    # Маленькие концентрические окружности, вычислить точку B
    x2 = center_x+(radius-15)*math.cos(i*6*np.pi/180.0)
    y2 = center_y+(radius-15)*math.sin(i*6*np.pi/180.0)

    cv2.line(img, pt1[i], (int(x2), int(y2)), (0, 0, 0), thickness=2)

# 4. Нарисуйте 12-часовую линию
for i in range(12):
    # 12-часовой график должен быть немного длиннее
    x = center_x+(radius-25)*math.cos(i*30*np.pi/180.0)
    y = center_y+(radius-25)*math.sin(i*30*np.pi/180.0)
    # Здесь используется предыдущая pt1
    cv2.line(img, pt1[i*5], (int(x), int(y)), (0, 0, 0), thickness=5)


# К этому моменту базовая диаграмма циферблата нарисована

while(1):
    # Продолжайте копировать карту циферблата, чтобы обновить рисунок, иначе он будет перекрываться
    temp = np.copy(img)

    # 5. Получить системное время и нарисовать динамические часы-минуты-секунды тремя линиями
    now_time = datetime.datetime.now()
    hour, minute, second = now_time.hour, now_time.minute, now_time.second

    # рисуем вторую линию
    # Угол в OpenCV рассчитывается по часовой стрелке, поэтому его нужно преобразовать
    sec_angle = second*6+270 if second <= 15 else (second-15)*6
    sec_x = center_x+(radius-margin)*math.cos(sec_angle*np.pi/180.0)
    sec_y = center_y+(radius-margin)*math.sin(sec_angle*np.pi/180.0)
    cv2.line(temp, center, (int(sec_x), int(sec_y)), (203, 222, 166), 2)

    # рисуем разметочную линию
    min_angle = minute*6+270 if minute <= 15 else (minute-15)*6
    min_x = center_x+(radius-35)*math.cos(min_angle*np.pi/180.0)
    min_y = center_y+(radius-35)*math.sin(min_angle*np.pi/180.0)
    cv2.line(temp, center, (int(min_x), int(min_y)), (186, 199, 137), 8)

    # нарисовать временную шкалу
    hour_angle = hour*30+270 if hour <= 3 else (hour-3)*30
    hour_x = center_x+(radius-65)*math.cos(hour_angle*np.pi/180.0)
    hour_y = center_y+(radius-65)*math.sin(hour_angle*np.pi/180.0)
    cv2.line(temp, center, (int(hour_x), int(hour_y)), (169, 198, 26), 15)

    # 6. Добавить текст текущей даты
    font = cv2.FONT_HERSHEY_SIMPLEX
    time_str = now_time.strftime("%d/%m/%Y")
    cv2.putText(img, time_str, (135, 275), font, 1, (0, 0, 0), 2)

    cv2.imshow('clocking', temp)
    if cv2.waitKey(1) == 27:  # Нажмите ESC для выхода
        break
