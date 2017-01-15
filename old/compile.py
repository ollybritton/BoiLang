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

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

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

    # FIXME: Loops take the next loop end as the end. Doesn't work when there are loops within loops.

    pointer = 0
    iterator = 0

    text = ""

    if(chars[0] == "yeah"):
        while iterator < charsLength:
            #print(chr(27) + "[2J")

            char = chars[iterator]

            if(char != 'boie' or char != 'bois' or char != "[" or char != "]"):
                iterator += 1

            if(char == "boii" or char == "+"):
                data[pointer] += 1
                # +

            if(char == "bboi" or char == "-"):
                data[pointer] -= 1
                # -

            if(char == "booii" or char == ">"):
                pointer += 1
                # >

            if(char == "bbooi" or char == "<"):
                pointer -= 1
                # <

            if(char == "boi!" or char == "."):
                text = text + chr(data[pointer])
                print chr(data[pointer])
                # .

            if(char == "boi?" or char == ","):
                given = raw_input()
                text = text + given
                data[pointer] = ord(given)
                # ,

            if(char == "boi..."):
                print data[pointer]

            if(char == "boi??"):
                given = raw_input()
                data[pointer] == given

            if(char == "bois" or char == "["):
                posCount = 0
                posOfEnd = 0;
                for j in range(iterator, charsLength):
                    innerChar = chars[j]
                    if posCount == -1:
                        posOfEnd = j
                        break
                    else:
                        if innerChar == "[":
                            posCount += 1

                        if innerChar == "]":
                            posCount -= 1


                if(data[pointer] == 0):
                    iterator += posOfEnd
                # [

            if(char == "boie" or char == "]"):
                posCount = 0
                posOfBegin = 0;
                for j in xrange(iterator, charsLength - iterator, -1):
                    innerChar = chars[j]
                    if posCount == -1:
                        posOfBegin = j
                        break
                    else:
                        if innerChar == "]":
                            posCount += 1

                        if innerChar == "[":
                            posCount -= 1

                iterator = posOfBegin
                # ]


#            print bcolors.OKBLUE + "Generation: "+ bcolors.ENDC + bcolors.OKGREEN + str(iterator) + bcolors.ENDC + bcolors.OKBLUE", List: " + bcolors.ENDC + bcolors.OKGREEN + str(data) + bcolors.ENDC + bcolors.OKBLUE + ", Pointer On: " + bcolors.ENDC + bcolors.OKGREEN + str(pointer) + bcolors.ENDC
            print data, char
            currentPoint = point(pointer, data)
            bcolors.OKGREEN + str(currentPoint) + bcolors.ENDC + "\n"
            time.sleep(delay)

        print bcolors.OKBLUE + "Code Run: " + bcolors.ENDC + bcolors.OKGREEN + code + bcolors.ENDC + "\n"
        print bcolors.OKBLUE + "Text Printed: " + bcolors.ENDC + bcolors.OKGREEN + text + bcolors.ENDC
        print bcolors.OKBLUE + "Final List:" + bcolors.ENDC + bcolors.OKGREEN + str(data) + bcolors.ENDC

code = "yeah +[>++++++++++<-]>[>+++++<-]"

print run(code, 0.1)
