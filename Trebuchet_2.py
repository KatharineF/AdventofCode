#two sliding windows p_left p_right <--- splices of line
#four pointers p_l1, p_l2, p_r1, pr2
#dictionary of ints and strings

#if line[p_l1] 







 
f = open("Trebuchet.txt", "r")
#f = ("9eightone", "hczsqfour3nxm5seven4", "9twopjqkghmbone")



stringToInt = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
result = 0

for line in f:
    left = None
    leftNumInt = None
    right = None
    rightNumInt = None
    p_l1, p_r1 = 0, len(line) - 1
    #print(p_r1)
    p_l2, p_r2 = p_l1 + 1, p_r1 - 1 

    if line[p_l1] in stringToInt.values():
        leftNumInt = line[p_l1]
        left = True
    
    while not left:
        if line[p_l2] in stringToInt.values():
            leftNumInt = line[p_l2]
            left = True
        for leftNum in stringToInt.keys():
            if leftNum in line[p_l1:p_l2]:
                leftNumInt = stringToInt[leftNum]
                left = True
                break
        p_l2 += 1
    #print(line)
    #print(p_r1)
    if line[p_r1] in stringToInt.values():
        rightNumInt = line[p_r1]
        right = True
    while not right:
        #print(p_r2, p_r1)
        #print(line[p_r2:])
        if line[p_r2] in stringToInt.values():
            rightNumInt = line[p_r2]
            right = True
        #print (right)
        for rightNum in stringToInt.keys():
            if rightNum in line[p_r2:]:
                rightNumInt = stringToInt[rightNum]
                right = True
                break
        p_r2 -= 1        
    #print(int(stringToInt[leftNum] + stringToInt[rightNum]))

    
        #result += int(leftNumInt) if leftNumInt else int(stringToInt[leftNum]
        #print(leftNumInt, rightNumInt)
    result += int(leftNumInt + rightNumInt) 


print(result)
    



