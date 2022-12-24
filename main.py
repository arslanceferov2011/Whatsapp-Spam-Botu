import pyautogui
import time
import os

count = int(input("Say daxil edin : "))

message = input("Mesaj daxil edin : ")

second = 10

while(second > 0):
    print("Baslamaq ucun son",second,"saniye")
    time.sleep(1)
    os.system("cls")
    second -= 1

while (count > 0):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")

    count -= 1

os.system("cls")

print("Sonlandi")    