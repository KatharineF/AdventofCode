# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..


# {{1: {'num': '467', 'p1': 0, 'p2': 3, 'line': 0}}
# {2: {'num': '114', 'p1': 5, 'p2': 8, 'line': 0}}
# {3: {'num': '35', 'p1': 2, 'p2': 4, 'line': 2}}
# {4: {'num': '633', 'p1': 6, 'p2': 9, 'line': 2}}
# {5: {'num': '617', 'p1': 0, 'p2': 3, 'line': 4}}
# {6: {'num': '58', 'p1': 7, 'p2': 9, 'line': 5}}
# {7: {'num': '592', 'p1': 2, 'p2': 5, 'line': 6}}
# {8: {'num': '755', 'p1': 6, 'p2': 9, 'line': 7}}
# {9: {'num': '664', 'p1': 1, 'p2': 4, 'line': 9}}
# {10: {'num': '598', 'p1': 5, 'p2': 8, 'line': 9}}}


# gears = ((1, 4), (8,5))


# for x in gears:
    #gears[x][0]

#check if there are 2 dictionaries with lines in range of lineRange
#store these two dictonaries 
#if True:
    #for each dictionary check that number is within pointerRange

#set range from dict
# for 467 
    # line range = 0-1
    # pointer range = 0-3 

# or 

# [1][3], [4][3], [3][6], [5][6], [8][3], [8][5]


#






# Create a dictionary of dictionaries of numbers:
    #(number: 467, line: 0, p1: 0, p2:2)


# for i in schema_dict
    # for line +/- 1 
    # for p1-1:p2+1 
    # if one char in "*#+$" 
        #result += schema[i][0:3]


    


def find_p2(p2):
    if line[p2].isnumeric:
        while line[p2].isnumeric():
            p2 += 1
    return p2

def fill_schemaDict(schemaDict, x, num, p1, p2, lineNo, length):
    schemaDict[x] = {"num": num, "p1": p1, "p2": p2, "lineNo": lineNo, "length": length} 
    return schemaDict

def set_line_range(line):
    if line == 0:
        return iter(range(line, line + 2))
    elif line >= len(schema) - 1:
        return iter(range(line - 1, line + 1))
    else:
        return iter(range(line - 1, line + 2))

def set_pointer_range(p1, p2, lineLength):
    if p1 != 0:
        p1 = p1 - 1
    if p2 != lineLength:
        p2 = p2 + 1 
    return iter(range(p1, p2))

def deep_get(dictionary, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)

schemaDict = {}
with open('Gears.txt') as my_file:
    schema = my_file.readlines() #<--- read more about this

num = None
dictIndex = 0 
gears = []
for x, line in enumerate(schema):
    p1 = 0 
    p2 = p1 + 1
    while p2 < len(line):
        if line[p1].isnumeric():
            p2 = find_p2(p2)
            num = line[p1:p2]
            schemaDict = fill_schemaDict(schemaDict, dictIndex, num, p1, p2, x, len(line))
            p1 = p2
            p2 = p1 + 1
            dictIndex += 1
        if line[p1] == "*":
            gear = (x, p1)
            gears.append(gear)
        p1 += 1
        p2 += 1
#print(schemaDict)

result = 0

for index in gears:
    lineRange = set_line_range(gears[index][0])
    



# for index in schemaDict:
#     #print("num", schemaDict[index]["num"])
#     lineRange = set_line_range(schemaDict[index]["lineNo"])
#     for x in lineRange:
#         pointerRange = set_pointer_range(schemaDict[index]["p1"], schemaDict[index]["p2"], schemaDict[index]["length"],) #<--- this only works if all lines are the same length
#         for y in pointerRange:
#             #print(x,y)
#             #print(schema[x][y])
#             if schema[x][y] in "*":
#                 result += int(schemaDict[index]["num"])
#                 #print(int(schemaDict[index]["num"]))
print(result)
#     if schema[schemaDict[x]["line"]] == 0:
#         lineJump = 0

#     if schema[schemaDict[x]["line"]][schemaDict[x]["p1"]:schemaDict[x]["p2"]] in "467":
#         print("ifduss")
    
#print(schemaDict[x]["num"])






#print(schema[3][4:7])



#print(int(schema[2][2:4]))






    # print("num", index)
    # lineRange = set_line_range(schemaDict[index]["line"])

    # pointerRange = set_pointer_range(schemaDict[index]["p1"], schemaDict[index]["p2"], len(schema[index]))
    # for x in lineRange:
    #     for y in pointerRange:
    #         print(x,y)
    #         print(schema[x][y])  <---- why doesn't this work?