#else in loop in python

for i in range(5):
    print(i)

else:
    print("ended")




for i in []:
    print(i)

else:
    print("ended")



for i in range(5):
    print(i)
    if(i==4):
        break

else:
    print("ended")