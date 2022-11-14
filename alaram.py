import datetime
from playsound import playsound
new=datetime.datetime.now()
print(new.time())
alaramHour=int(input("Enter the Hour:"))
alaramMin=int(input("Enter the Minint:"))
alaramAm=input("Enter the Am/Pm:")

if alaramAm=="Pm":
    alaramHour+12

while True:
    if alaramHour==datetime.datetime.now().hour and alaramMin==datetime.datetime.now().minute:
        print("Playing...")
        playsound('D:\\Users\Dhivakar\Desktop\Alarams\song.mp3')
        break
