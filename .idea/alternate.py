import random
import pyautogui

chars = "abcdefghijklmnopqrstuvxyz0123456789"
allchar = list(chars)

pwd = pyautogui.password("Enter password:")
sample_pwd = random.choices(allchar, k=len(pwd))

while sample_pwd != list(pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))
    print("<====" + str(sample_pwd) + "====>")

print("The password is:" + "".join(sample_pwd))