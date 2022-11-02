from datetime import datetime
import time
from playsound import playsound


alarm_time = input("Введите время в формате 'HH:MM:SS AM/PM': ")

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Некорректный формат . Попробуйте снова.."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Некорректный формат часов. Попробуйте снова.."
        elif int(alarm_time[3:5]) > 59:
            return "Некорректный формат минут. Попробуйте снова."
        elif int(alarm_time[6:8]) > 59:
            return "Некорректный формат секунд. Попробуйте снова..."
        else:
            return "ok"


while True:
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Установка будильника на {alarm_time}...")
        break


alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()


now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")


if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Вставай!")
                    playsound('/home/user/Загрузки/Alarm Clock_alarm.wav')


while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Вставай!")
                    playsound('/home/user/Загрузки/Alarm Clock_alarm.wav')
                    break

