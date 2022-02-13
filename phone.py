import phonenumbers as ph
from phonenumbers import timezone,carrier,geocoder
import pywhatkit
import random
import datetime
# import os



print('''


*****
Choose one : 
[1] Phone Number
[2] Whats App
*****


''')

ch = int(input("-> "))


# for i in range(101):
#     os.system("CLS")
#     print(str(i) + "%")
#     time.sleep(0.1)
    


if ch == 1:
    c_code = str(input("[*] Enter Country Code :" ))
    num = str(input("[*] Enter a Phone Number :" ))
    num = "+" + c_code + num


    detail = ph.parse(num)

    time = timezone.time_zones_for_number(detail)
    carr = carrier.name_for_number(detail, "en")
    geo = geocoder.country_name_for_number(detail, "en") 

    print(detail)
    print("-> Country Name : " + geo)
    print("-> Time Zone : " + time[0])
    print("-> Carrier Name : " + carr)

elif ch == 2 :
    c_code = input("Enter country code : ")



    num = input("Enter number where you want to send message : ")
    num ="+" + c_code + num

    hour_ = datetime.datetime.now().hour
    minute_ = datetime.datetime.now().minute
    minute_ = minute_ + 1



    for i in range(100):

        r1 = str(random.randrange(1,9))

        
        r2 = str(random.randrange(1,9))
        r3 = str(random.randrange(1,9))
        r4 = str(random.randrange(1,9))
        r5 = str(random.randrange(1,9))
        r6 = str(random.randrange(1,9))
        r7 = str(random.randrange(1,9))
        r8 = str(random.randrange(1,9))

        ran = "9" + "8" + r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
        if minute_ == datetime.datetime.now().minute:
            minute_ = minute_ + 1

        pywhatkit.sendwhatmsg(num , ran , hour_ , minute_ , 7  , 10 )


else:
    print("Choose from given options")

