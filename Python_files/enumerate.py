#enumerate function in python  


marks = [3,4,5,6,4]

# index=0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("hai")
#     index+=1


for index,mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("hi")