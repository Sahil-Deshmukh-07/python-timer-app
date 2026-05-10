import tkinter as tk
import time
import threading
import pygame

def timer(set_time):
    count = 1
    while True:
        time.sleep(1)
        current_time = time.strftime("%H:%M:%S")
        if count:
            curr_time = current_time.split(":")
            set_t = set_time.split(":")
            hours = int(set_t[0]) + int(curr_time[0])
            minutes = int(set_t[1]) + int(curr_time[1])
            seconds = int(set_t[2]) + int(curr_time[2])
            if seconds >= 60:
                seconds -= 60
                minutes += 1
            if minutes >= 60:
                minutes -= 60
                hours += 1
            if hours >= 24:
                hours -= 24
            timer_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            print("timer time ",timer_time)
            count = 0
        print(f"\rCurrent Time: {current_time}", end="", flush=True)
        if current_time == timer_time:
            pygame.mixer.init()
            pygame.mixer.music.load("assets/alarm_sound.mp3")
            pygame.mixer.music.play()
            print("\n")
            return
