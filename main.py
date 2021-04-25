from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from string import ascii_letters, digits
from random import randint, choice
import random
import requests
import time


red = '\033[91m'
END = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[92m'

token2 = open("token.txt", "a")

print(yellow +'''____________________________________________________
|,---.        )    👑 Bʏ 𝑳𝒂𝒔𝒉𝒐𝒇𝒔𝒌𝒊 👑   (         ,---.|
|) 1 (        `====---    _   ---===='          ) 1 (|
| \ /                    | |                     \ / |
|  V      ,-.            |-|                      V  |
|        ( D )          _|-|_          ＦＡＫＥ.Ｍ     |
|         `-'         _(_) (_)          DIsᴄᴏʀᴅ      |
|                    (_) | | L_.                     |
|     𝖑𝖆𝖘𝖍𝖔𝖘𝖐𝖎#8046    '      (_  \                    |
| / \               (        /  /                / \ |
|( 1 )                                          ( 1 )|
| \ / ---==<                             >==---  \ / |
|____________________________________________________|''' + END)
kill_process = input(red + "►─═ " + yellow + "𝑺𝒕𝒂𝒓𝒕 ? " + blue + " 𝒀/𝑵 :" + END)

if kill_process == "Y":


    rage = input(red + "►─═ " + yellow + "𝑯𝒐𝒘 𝒎𝒂𝒏𝒚 𝒂𝒄𝒄𝒐𝒖𝒏𝒕𝒔 𝒅𝒐 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 ?" + blue + " Number " + END)
    rage = int(rage)

    for i in range(rage):

        #main
        file =  open("acc.txt", "a")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.minimize_window()
        print("                                                                                    ")
        print(green + "----------------" + red + "------------" +  blue + "-----------" + yellow + "---------"  + red +"-------------" + red + "----------"  + yellow + "-------------")
        print("                                                                                    ")
        print(red + "─═  " + yellow + "𝑺𝒊𝒏𝒈𝒖𝒑𝒊𝒏𝒈" + END)
        print("                                                       ")
        driver.get("https://discord.com/register")
        driver.implicitly_wait(5)
        file.write("\n ------------------- ")

         #gmail
        print(red + "  10%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒈𝒎𝒂𝒊𝒍" + END)
        rand = f'{"".join([choice(ascii_letters + digits) for n in range(randint(9, 12))])}'
        email = driver.find_element_by_name("email")
        email.send_keys(rand + '@' + "gmail" + '.com')
        file.write("\n email : " + rand + '@' + "gmail" + ".com")


         #radnom username from list
        print(red + "  30%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆" + END)
        mylist = ["javad", "mmd", "nikulas", "nima", "shahin", "killer", "fatti", "nightman", "blue man", "secret team","aboli", "abolfazel", "mohsen", "kianosh", "kiarash", "Sina", "night killer", "tina", "TnT", "TLS","Streetman", "shyan", "wiliyam"]
        username = driver.find_element_by_name("username")
        username.send_keys(random.choice(mylist))
        file.write("\n username : " + random.choice(mylist))


        ###random password
        rand2 = f'{"".join([choice(ascii_letters + digits) for n in range(randint(8, 8))])}'
        print(red + "  40%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒑𝒂𝒔𝒔𝒘𝒐𝒓𝒅" + END)
        password = driver.find_element_by_name("password")
        password.send_keys(rand2)
        file.write("\n password : " + rand2)
        file.write("\n ------------------- ")

        #brithday
        print(red + "  50%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒕𝒂𝒓𝒊𝒌𝒉 𝒕𝒂𝒗𝒂𝒍𝒐𝒅" + END)
        p1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div[1]')
        p1.click()
        year = ["react-select-2-option-3", "react-select-2-option-2", "react-select-2-option-1","react-select-2-option-2"]
        s1 = driver.find_element_by_id(random.choice(year))
        s1.click()
        p2 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div/div[1]")
        p2.click()
        mounth = ["react-select-3-option-4", "react-select-3-option-5","react-select-3-option-6","react-select-3-option-7","react-select-3-option-8", "react-select-3-option-3"]
        s2 = driver.find_element_by_id(random.choice(mounth))
        s2.click()
        p3 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[3]/div/div/div/div/div[1]")
        p3.click()
        day = ["react-select-4-option-18", "react-select-4-option-19","react-select-4-option-20", "react-select-4-option-21"]
        s3 = driver.find_element_by_id(random.choice(day))
        s3.click()

        ###sumbiT
        finish = driver.find_element_by_class_name("contents-18-Yxp")
        finish.click()




        # finisH
        print(red + "  100%  " + blue + "✨𝐶𝑟𝑒𝑎𝑡𝑒𝑑" + END)
        print("                                                       ")
        print("                                                       ")
        time.sleep(70)

        # token

        while True:
            email = (rand + '@' + "gmail" + '.com')
            password = (rand2)

            payload = {
                "email": email,
                "password": password
            }

            r = requests.post('https://discord.com/api/v8/auth/login', json=payload).json()
            if "captcha_key" in r:
                print(" captcha request , connection timeout ")
                time.sleep(1)
            elif "errors" in r:
                print("Run again.")
            elif r["token"] == None:
                break
            else:
                token2.write(r["token"])
                time.sleep(5)

        while True:
            if r["token"] == None:
                mfa_payload = {
                    "ticket": r["ticket"]
                }
                r2 = requests.post('https://discord.com/api/v8/auth/mfa/totp', json=mfa_payload).json()
                if "message" in r2:
                    time.sleep(1)
                else:
                    token2.write(r2["token"])
                    print(red + " ─═  " + yellow + "𝒔𝒂𝒗𝒆𝒅 " + blue + "𝒕𝒐𝒌𝒆𝒏" + END)
                    time.sleep(5)





        # news

        print(red + "   ─" + yellow + " 𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆 : " + green + random.choice(mylist))
        print(red + "   ─" + yellow + " 𝒑𝒂𝒔𝒔𝒘𝒐𝒓𝒅 : " + green + rand2)
        print(red + "   ─" + yellow + " 𝒈𝒎𝒂𝒊𝒍 : " + green + rand + '@' + "gmail" + ".com")
        print("                                                       ")
       ## time.sleep(20)
        print(red + "─═  " + yellow + "𝑺𝒂𝒗𝒆 𝒊𝒏" + blue + " 𝒂𝒄𝒄.𝒕𝒙𝒕" + END)
        driver.quit()




else:
     print(red + "►─═ " + yellow + "𝙗𝙮𝙚 𝙨𝙚𝙚 𝙮𝙤𝙪 𝙖𝙜𝙖𝙞𝙣 " + END)





