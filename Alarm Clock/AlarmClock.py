# Alarm Clock
#Author:  Ankan Ghosh | 12.3.24 | Innovixion Tech Task 2
'''
Design an alarm clock application that allows users to set
an alarm and be alerted at the specified time.
'''

import datetime
import time
from playsound import playsound

CLEAR = "\033[2J"  #ANSI CHaracters/escape sequence to manipulate the Terminal
CLEAR_AND_RETURN = "\033[H"

def set_alarm():
    alarm_hour = int(input("\nEnter Hour: "))
    alarm_min = int(input("\nEnter Minutes: "))
    alarm_am_pm = input("\nam/pm: ").lower()

    if alarm_am_pm == "pm":
        alarm_hour += 12

    print(f"\nAlarm is set for: {alarm_hour % 24:02d}:{alarm_min:02d}")

    return alarm_hour, alarm_min

def alarm(alarm_hour, alarm_min, seconds):
    time_elapsed = 0

    print(CLEAR)
    print(f"\nAlarm is set for: {alarm_hour % 24:02d}:{alarm_min:02d}")
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    print("\n**ALARM**\n")
    playsound("alarm.mp3")

if __name__ == "__main__":
    alarm_hour, alarm_min = set_alarm()

    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    current_min = current_time.minute

    time_to_alarm = (alarm_hour - current_hour) * 3600 + (alarm_min - current_min) * 60

    alarm(alarm_hour, alarm_min, time_to_alarm)
