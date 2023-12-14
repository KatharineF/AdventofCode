# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green


#ID = line number 
#only 12 red cubes, 13 green cubes, and 14 blue cubes?
#for line in f 
    #if possible
        #result += line
#Pointer along line (starting at p = 6)
#for char in line[6:]
    #go along line until number 
    #store number in "value"













    #if ":" first number is + 2
    #The letter at char + 2 then equals the number at char. If this number is larger than the control group then move on to next line.
    #If counter makes it all the way to the next line then the ID of this line can be added to total number
    #



f = open("Cube.txt", "r")
testBag = {"r":12, "g":13, "b":14}  
gameBag = {"r":0, "g":0, "b":0}
result = 0

for ID, line in enumerate(f):
    line = line.replace('reen', '')
    line = line + ";"
    possible = True
    value = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            value += char
        elif char in "rbg":
            gameBag[line[x]] = int(value)
        elif char in ";,:":
            value = ""
            if char == ";":
                for keys in testBag:
                    if gameBag[keys] > testBag[keys]:
                        possible = False
                gameBag = {"r":0, "g":0, "b":0}
                

    
    if possible == True:
        result += (ID + 1)
                
print(result)