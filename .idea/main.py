import random
import pyautogui

chars="abcdefghijklmnopqrstuvxyz0123456789";
allchar=list(chars)
pwd =pyautogui.password("Enter password:")
sample_pwd=""
while(sample_pwd != pwd):
    sample_pwd=random.choices(allchar,k=len(pwd))
    print("<===="+str(sample_pwd)+"====>")

    if(sample_pwd==list(pwd)):
        print("The password is:"+"".join(sample_pwd))
        break
