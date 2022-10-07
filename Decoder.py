key = 5

def ascify(char, run):
    char = ord(char[run])
    return char

def charify(code):
    code = chr(code)
    return code

def stringSplitOne(full):
    #print(len(full)%2)
    workingString = ""
    leng = int(len(full))
    if (leng % 2) == 0:
        leng = int(leng/2)
    else:
        leng = (int(leng/2))+1
    for i in range (leng):
        workingString = workingString+full[i]
        #print(full[i])
    return workingString

def stringSplitTwo(full):
    #print(len(full)%2)
    workingString = ""  
    leng = int(len(full))
    if (leng % 2) == 0:
        leng = int(leng/2)
        size = leng
    else:
        leng = (int(leng/2))+1
        size = leng - 1
    for i in range (size):
        workingString = workingString+full[leng+i]
        #print(full[leng+i])
    return workingString

#print(stringSplitOne(message))
#print(stringSplitTwo(message))

def encode(string, key):
    workingString = ""
    leng = len(string)
    key = int(len(message)/key)
    for i in range (leng):
        workingString = workingString + charify(ascify(string,i)+(key))
    return workingString

def main(message, key):
    string1 = stringSplitOne(message)
    string2 = stringSplitTwo(message)
    string1 = encode(string1, key)
    string2 = encode(string2, -(key))
    message = string1 + string2
    return message


#print(encode(message, key))
#print(encode(message, -(key)))

for i in range (5):
    message = str(input("enter the message.>"))
    print("output 1:")
    print(main(message, key))
    print("output 2:")
    print(main(message, (-(key))))
