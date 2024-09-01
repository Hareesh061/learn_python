# read, write , append files in python

file = open("new.txt","r")

text = file.read()
print(text)
file.close()

# read, readlines, writelines


#lamda function
# lambda function is a small anonymous function in python which can take any number of arguments but can only   
# have one expression.
# syntax: lambda arguments : expression

square = lambda x : x**2
print(square(5))
