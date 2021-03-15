from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from string import ascii_letters, digits
from random import randint, choice
import os, sys



red = '\033[91m'
END = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[92m'

print(red + "░▒▓█►─═ " + yellow + "ＦＡＫＥ.Ｍ " + "DIsᴄᴏʀᴅ"+  red + " ═─◄█▓▒░" + END)
print(red + "░▒▓█►─═ "  + yellow +  " 👑 Bʏ 𝑳𝒂𝒔𝒉𝒐𝒇𝒔𝒌𝒊 👑 "  + red + " ═─◄█▓▒░"+ END)

kill_process = input( red + "►─═ " + yellow + "𝑺𝒕𝒂𝒓𝒕 ? " + blue +  " 𝒀/𝑵 :" + END)

if kill_process == "Y":

    loop = [
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
        'x',
    ]
    for i in loop:
       file = open("acc.txt", "a")
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.implicitly_wait(5)
       driver.minimize_window()
       print("                                                                                    ")
       print(green + "----------------"+ red + "-----------------------" + yellow + "----------------------"+ red + "-----------------------")
       print("                                                                                    ")
       print( red + "─═  "+ yellow  + "𝑺𝒊𝒏𝒈𝒖𝒑𝒊𝒏𝒈" + END)
       print("                                                       ")
       driver.get("https://discord.com/register")
       driver.implicitly_wait(5)
       file.write("\n ------------------- " )



       ###gmail
       print(red + "  10%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒈𝒎𝒂𝒊𝒍" + END)

       rand = f'{"".join([choice(ascii_letters + digits) for n in range(randint(9, 12))])}'
       email = driver.find_element_by_name("email")
       email.send_keys(rand + '@' + "gmail" + '.com')
       file.write("\n email : " + rand + '@' + "gmail" + ".com")

       # random username
       print(red + "  30%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆" + END)
       rand3 = f'{"".join([choice(ascii_letters + digits) for n in range(randint(5, 6))])}'
       username = driver.find_element_by_name("username")
       username.send_keys(rand3)
       file.write("\n username : " + rand3)

       ###random password
       rand2 = f'{"".join([choice(ascii_letters + digits) for n in range(randint(8, 8))])}'
       print(red + "  40%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒑𝒂𝒔𝒔𝒘𝒐𝒓𝒅" + END)
       password = driver.find_element_by_name("password")
       password.send_keys(rand2)
       file.write("\n password : " + rand2)
       file.write("\n ------------------- " )
       ###brithday
       print(red + "  50%  " + yellow + "𝑰𝒎𝒑𝒐𝒓𝒕𝒊𝒏𝒈 " + green + "𝒕𝒂𝒓𝒊𝒌𝒉 𝒕𝒂𝒗𝒂𝒍𝒐𝒅" + END)

       o1 = driver.find_element_by_xpath(
         "/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div[1]")
       o1.click()
       s1 = driver.find_element_by_id("react-select-2-option-0")
       s1.click()
       o2 = driver.find_element_by_xpath(
         "/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div/div[1]")
       o2.click()
       s2 = driver.find_element_by_id("react-select-3-option-0")
       s2.click()
       o3 = driver.find_element_by_xpath(
         "/html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[4]/div[1]/div[3]/div/div/div/div/div[1]")
       o3.click()
       s3 = driver.find_element_by_id("react-select-4-option-18")
       s3.click()

        ###sumbiT
       finish = driver.find_element_by_class_name("contents-18-Yxp")
       finish.click()
       driver.maximize_window()


       #CAPTCHA
       driver.maximize_window()
       print(red + "  80%  " + yellow + "𝑷𝒍𝒛 𝒅𝒐 " + green + "𝒄𝒂𝒑𝒕𝒄𝒉𝒂  !!" + END)
       time.sleep(50)


        # finisH
       print(red + "  100%  " + blue + "✨𝐶𝑟𝑒𝑎𝑡𝑒𝑑" + END)
       print("                                                       ")
       print(red + "─═  "+ yellow + "𝑺𝒂𝒗𝒆 𝒊𝒏" + blue + " 𝒂𝒄𝒄.𝒕𝒙𝒕" + END)
       print("                                                       ")


       #news

       print(red + "   ─" + yellow + " 𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆 : " + green + rand3)
       print(red + "   ─" + yellow + " 𝒑𝒂𝒔𝒔𝒘𝒐𝒓𝒅 : " + green + rand2)
       print(red + "   ─" + yellow + " 𝒈𝒎𝒂𝒊𝒍 : " + green + rand + '@' + "gmail" + ".com")
       print("                                                       ")



       edame = input( red + "►─═ " + yellow + "𝒔𝒕𝒐𝒑  ? " + blue +  " 𝒀/𝑵 :" + END)
       if edame == "Y":
           sys.exit(red + "►─═" + blue + "𝙗𝙮𝙚 𝙨𝙚𝙚 𝙮𝙤𝙪 𝙖𝙜𝙖𝙞𝙣 " + END)



    else:
      print(red + "►─═" + blue + "𝙗𝙮𝙚 𝙨𝙚𝙚 𝙮𝙤𝙪 𝙖𝙜𝙖𝙞𝙣 " + END)



