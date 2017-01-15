import sys
import time
from fileHandle import *
from findBracket import *
from translate import *

class clrs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def new_array():
    array = []
    for i in range(0,20):
        array.append(0)
    return array

def describe(cells, iterator, character, pointer):
    iterator = clrs.OKBLUE + "Iteration: " + clrs.ENDC + clrs.OKGREEN + str(iterator) + ", " + clrs.ENDC
    cells = clrs.OKBLUE + "Cells: " + clrs.ENDC + clrs.OKGREEN + str(cells) + ", " + clrs.ENDC
    command = clrs.OKBLUE + "Executing: " + clrs.ENDC + clrs.OKGREEN + str(character) + ", " + clrs.ENDC
    bfCharacter = clrs.OKBLUE + "In BF: " + clrs.ENDC + clrs.OKGREEN + toBrainFudge(character) + ", " + clrs.ENDC
    pointer = clrs.OKBLUE + "Pointer On: " + clrs.ENDC + clrs.OKGREEN + str(pointer) + "." + clrs.ENDC
    print iterator, cells, command, bfCharacter, pointer

def transform(program):
    chars = program.split(" ")
    return chars

def parse(program):
    data = new_array()
    pointer = 0
    commands = transform(program)
    programLength = len(commands)
    brackets = find_brackets(commands)
    iterator = 0
    pointer = 0
    text = ""

    if(commands[0] != "yeah"):
        print clrs.FAIL + "Error: No \"yeah\". (Prefix your program with \"yeah\")."
        sys.exit()
    else:
        while iterator < programLength:
            command = commands[iterator]
            currVal = data[pointer]

            if(command != "bois" or command != "bois"):
                iterator += 1

            if(command == "boii"):
                data[pointer] += 1
            if(command == "bboi"):
                data[pointer] -= 1

            if(command == "booii"):
                pointer += 1
            if(command == "bbooi"):
                pointer -= 1

            if(command == "boi!"):
                character = chr(currVal)
                print character
                text = character + text
            if(command == "boi?"):
                arg = raw_input()
                data[pointer] = ord(arg)

            if(command == "bois"):
                if(data[pointer] != 0):
                    # No? Do next thing.
                    iterator += 1
                else:
                    match = 0
                    # Yes?
                    for i in range(0, len(brackets)):
                        # Loop through all the positions of the brackets, until you find yourself.
                        if brackets[i][0] == iterator:
                            # Yay, I found it! (Hopefully).
                            match = i
                            break
                    print "changing iterator " + str(brackets[match][1]+1)
                    # Go to the command after "boie".
                    iterator = brackets[match][1]+1
                    # If we goto the command *after* "boie", we don't have to check the loop again.


            if(command == "boie"):
                match = 0
                # Find a match in the brackets.
                for i in range(0, len(brackets)):
                    if brackets[i][1] == iterator:
                        # Yay, it's there.
                        match = i
                        break

                val = brackets[match][0]
                iterator = val



            if(inspect_flag == True):
                describe(data, iterator, command, pointer)
                raw_input()

    print ""
    print clrs.OKBLUE + "Code Run: " + clrs.ENDC + clrs.OKGREEN + str( program ) + clrs.ENDC
    print clrs.OKBLUE + "In BF: " + clrs.ENDC + clrs.OKGREEN + str( toBrainFudge(program) ) + clrs.ENDC
    print clrs.OKBLUE + "Final: " + clrs.ENDC + clrs.OKGREEN + str(data) + clrs.ENDC
    if text != "":
        print clrs.OKBLUE + "Text: " + clrs.ENDC + clrs.OKGREEN + text + clrs.ENDC

parse( read_file( file_arg ) )
