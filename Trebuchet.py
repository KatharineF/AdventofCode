f = open("Trebuchet.txt", "r")
numbers = "1234567890"
result = 0
for line in f:
    int1 = None 
    int2 = None
    pl, pr = 0, -1
    while not int1 and int2:
        if line[pl] in numbers:
            int1 = line[pl]
        if line[pr] in numbers:
            int2 = line[pr]
        else: 
            pl += 1
            pr -= 1
    if not int1:
        while not int1:
            if line[pl] in numbers:
                int1 = line[pl]
            else: 
                pl += 1
    if not int2:            
        while not int2:
            if line[pr] in numbers:
                int2 = line[pr]
            else: 
                pr -= 1
    result = result + int(int1 + int2)
print(result)   
    