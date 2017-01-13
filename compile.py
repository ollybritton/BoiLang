import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def generateArray(code):
    array = []
    for i in range(0,20):
        array.append(0);
    return array

def point(pos, data):
    lengths = 0
    for i in range(0, pos):
        lengths += int( len(str(data[pos])) )

    amount = (2*pos)+lengths
    print " " * amount + "^"

def run(code, delay):
    data = generateArray(code)
    chars = code.split(" ")
    charsLength = len(chars)
    pointer = 0
    iterator = 0
    text = ""

    if(chars[0] == "yeah"):
        while iterator < charsLength:
            #print(chr(27) + "[2J")

            char = chars[iterator]

            if(char != 'boie' or char != 'bois'):
                iterator += 1

            if(char == "boii"):
                data[pointer] += 1
                # +

            if(char == "bboi"):
                data[pointer] -= 1
                # -

            if(char == "booii"):
                pointer += 1
                # >

            if(char == "bbooi"):
                pointer -= 1
                # <

            if(char == "boi!"):
                text = text + chr(data[pointer])
                print chr(data[pointer])
                # .

            if(char == "boi?"):
                given = raw_input()
                text = text + given
                data[pointer] = ord(given)
                # ,

            if(char == "boi..."):
                print data[pointer]

            if(char == "boi??"):
                given = raw_input()
                data[pointer] == given

            if(char == "bois"):
                posOfEnd = chars[iterator:len(chars)].index("boie")
                if(data[pointer] == 0):
                    iterator += posOfEnd+1
                # [

            if(char == "boie"):
                posOfBegin = len(chars) - 1 - chars[::-1].index('bois')
                iterator = posOfBegin
                # ]


#            print bcolors.OKBLUE + "Generation: "+ bcolors.ENDC + bcolors.OKGREEN + str(iterator) + bcolors.ENDC + bcolors.OKBLUE", List: " + bcolors.ENDC + bcolors.OKGREEN + str(data) + bcolors.ENDC + bcolors.OKBLUE + ", Pointer On: " + bcolors.ENDC + bcolors.OKGREEN + str(pointer) + bcolors.ENDC
            print data
            currentPoint = point(pointer, data)
            bcolors.OKGREEN + str(currentPoint) + bcolors.ENDC + "\n"
            time.sleep(delay)

        print bcolors.OKBLUE + "Code Run: " + bcolors.ENDC + bcolors.OKGREEN + code + bcolors.ENDC + "\n"
        print bcolors.OKBLUE + "Text Printed: " + bcolors.ENDC + bcolors.OKGREEN + text + bcolors.ENDC
        print bcolors.OKBLUE + "Final List:" + bcolors.ENDC + bcolors.OKGREEN + str(data) + bcolors.ENDC

code = "yeah boii boii boii boii boii boii boii boii boii boii bois booii boii boii boii boii boii boii boii booii boii boii boii boii boii boii boii boii boii boii booii boii boii boii booii boii bbooi bbooi bbooi bbooi bboi boie booii boii boii boi! booii boii boi! boii boii boii boii boii boii boii boi! boi! boii boii boii boi! booii boii boii boi! bbooi bbooi boii boii boii boii boii boii boii boii boii boii boii boii boii boii boii boi! booii boi! boii boii boii boi! bboi bboi bboi bboi bboi bboi boi! bboi bboi bboi bboi bboi bboi bboi bboi boi! booii boii boi! booii boi!"

print run(code, 0.01)
