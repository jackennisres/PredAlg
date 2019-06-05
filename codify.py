videoCode = "ThIs Is A sTanDiN fOr CoDiNg SoMeThInG"
code = ""

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))




def isinlower(fletter):
    try:
        score = enlower[fletter]
        return True
    
    except:
        return False 

def isinupper(fletter):
    try:
        score = enupper[fletter]
        return True
    
    except:
        return False


def eneq(x):
    return (num1 * x) + num2

def deeq(y):
    #print(y - num2)
    return (y - num2) / num1 



enlower = {'e': 1, 't' : 2, 'a' : 3, 'o' : 4, 'i' : 5, 'n' : 6, 's' : 7, 'r': 8, 'h' : 9, 'l' : 10, 'd' : 11, 'c' : 12, 
       'u': 13, 'm': 14, 'f': 15, 'p': 16, 'g': 17, 'w': 18, 'y': 19, 'b': 20, 'v': 21, 'k': 22, 'x': 23,
       'j': 24, 'q': 25, 'z': 26, ' ': 27}

enupper = {'E': 100, 'T' : 200, 'A' : 30, 'O' : 40, 'I' : 50, 'N' : 60, 'S' : 70, 'R': 80, 'H' : 90, 'L' : 100, 'D' : 110, 'C' : 120, 
       'U': 130, 'M': 140, 'F': 150, 'P': 160, 'G': 170, 'W': 180, 'Y': 190, 'B': 200, 'V': 210, 'K': 220, 'X': 230,
       'J': 240, 'Q': 250, 'Z': 260}

decode = ""

for letter in videoCode:
    if(isinlower(letter)):
        code += str(eneq(enlower[letter]))
    if(isinupper(letter)):
        code += str(eneq(enupper[letter]))
    code += "_"
    


codeList = code.split('_')
codeList = codeList[:len(codeList) - 1]

keyList = list(enlower.keys())
valueList = list(enlower.values())

print(keyList)
print(valueList)

decoded = ""

for item in codeList:
    print("Item: " + item)
    print("Deeq: " + str(deeq(int(item))))
    if(isinlower(int(deeq(int(item))))):
        print("WOW")
        decoded += enlower[str(int(deeq(int(item))))]
    if(isinupper(int(deeq(int(item))))):
        print("BOOM")
        decoded += enupper[str(int(deeq(int(item))))]

print()     
print("Decoded message: " + decoded)
        
    #print(keyList[valueList.index(deeq(item))])
