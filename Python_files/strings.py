# strings in python(strings are immutable)




name = "hari is a good name"
print(name[0])
print(name[1])
print(name[2])

for character in name:
    print(name)
    break






# string slicing




names = "hari, ramu"
print(len(names))

print(names[0:4])

name ="anupaam"
print(name[-1])
print(name[-2])
print(name[-3])
print(name[0:1])
print(name[0:2])
print(name[2:3])

print(name[0:-1])
print(name[0:-2])
print(name[0:-3])
print(name[2:-4])
print(name[-1:3])


# string methods in python



a = "!! Madeva ahi alli Ho !!"
print(a.upper())
print(a.lower())
print(a.rstrip('!'))

print(a.replace('Madeva','jon'))

print(a.split(" "))

print(a.capitalize())

# other methods: endswith(), find(), swapcase(), title()