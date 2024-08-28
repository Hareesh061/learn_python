# #for loops

name = "hareesh"
for i in name:
    print(i)

names = ['hai','bye','hey','hello']
for name in names:
    print(name)
    if(name=='bye'):
        break


for i in range(5):
    print(i)

#(start,end, step)
for i in range(0,200,50):
    print(i)








# while loops



i = int(input("enter the number: "))
while(i<=10):
    i = int(input("enter the number: "))
    print(i)
    

i = int(input("enter the number: "))
while(i<=10):
    print(i)
    

count = 5
while(count>0):
    print(count)
    count=count-1


#break statement

for i in range(5):
    print(i)
    if(i==3):
        break
print("end")