# match case statement

import matchcase
a = 4

match a:

    case 0:
        print("hai")

    case 4: 
        print("bau")
        

    case _ if 5 > a:
        print("greater")

print("end")
