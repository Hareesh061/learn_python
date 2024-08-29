# telling wishes based on time
import time
t = time.strftime('%H:%M:%S')

hr = int(time.strftime('%H'))

if(hr>=0 and hr <12):
    print("good morning")

elif(hr>=12 and hr<18):
    print("afternoon")

else:
    print("night")


