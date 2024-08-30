#exception handling in python
#try block

num = input("enter your number: ")

try:
    for i in range(1,11):
        print(int(num)*i)

except Exception as e:
    print(e)

print("ended")

