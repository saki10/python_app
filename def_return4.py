def Grades (test) :
    if test >= 100 :
        print("S")
    elif test >= 90 :
        print("A")
    elif test >= 80 :
        print("B")
    elif test >= 70 :
        print("C")
    else :
        print("D")
Grades(80)


def Grades (test) :
    if test >= 100 :
        return("S")
    elif test >= 90 :
        return("A")
    elif test >= 80 :
        return("B")
    elif test >= 70 :
        return("C")
    else :
        return("D")
test = 70
print(test,"点は" ,Grades(80))