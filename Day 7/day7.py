import logging
import sys
from itertools import permutations

LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
input_program = "3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99"

class operation:
    def __init__(self, input=[]):
        '''Create operation from an array. 
                First Item: the opcode
                Last Item: the return
                Middle: the parameters'''
        instruction = str(input[0]).zfill(5)
        
        self.opcode = int(instruction[-1])
        self.parameters = input[1:len(input)]
        self.parameter_mode = list(reversed(list(map(int, list(instruction[0:3])))))
    def __str__(self):
        return str(self.__dict__)
    def getParm(self, loc, program):
        #logging.info("Get parms for {} at location {}".format(self, loc))
        if self.parameter_mode[loc] == 0:
            #logging.info("returned {}".format(program[self.parameters[loc]]))
            return program[self.parameters[loc]]
        elif self.parameter_mode[loc] == 1:
            return self.parameters[loc]

def main():
    OG_opcode = list(map(int, input_program.split(',')))
    
    logging.basicConfig(format=LOGGING_FORMAT,
                        level=logging.INFO,
                        stream=sys.stdout)
    logging.info('Started the opcode program on an input of length {}'.format(len(OG_opcode)))

    #part1(OG_opcode)

    iterate_program()

def iterate_program(opcode_local, input_list):
    counter = input_loc = final_ouput = 0
    opcode = opcode_local.copy()
    
    while(counter<=len(opcode)):
        
        inputs = number_of_paramaters(opcode[counter])
        output = 0
        
        operation_object = operation(opcode[counter:counter+(inputs+1)])
        #logging.info("This is the object {}".format(operation_object))

        if(opcode[counter] == 99):
            #logging.info('Final State was {}'.format(opcode[0]))
            return int(final_ouput)
        elif(operation_object.opcode == 1):
            #1 means addition
            output = operation_object.getParm(0, opcode) + operation_object.getParm(1, opcode)
        elif(operation_object.opcode == 2):
            #2 means multiplication
            output = operation_object.getParm(0, opcode) * operation_object.getParm(1, opcode)
        elif operation_object.opcode == 3:
            #take input and save it to the parameter
            output = input_list[input_loc]
            input_loc+=1
            opcode[operation_object.parameters[0]] = output
            counter+=inputs+1
            continue
        elif(operation_object.opcode == 4):
            final_ouput = operation_object.getParm(0, opcode)
            counter+=inputs+1
            continue
        elif(operation_object.opcode == 5):
            # Jump if True
            if operation_object.getParm(0, opcode):
                counter = operation_object.getParm(1, opcode)
                continue
        elif(operation_object.opcode == 6):
            # Jump if False
            if not operation_object.getParm(0, opcode):
                counter = operation_object.getParm(1,opcode)
                continue
        elif(operation_object.opcode == 7):
            # Less than
            output = 1 if operation_object.getParm(0,opcode) < operation_object.getParm(1,opcode) else 0
        elif(operation_object.opcode == 8):
            # Equals
            output = 1 if operation_object.getParm(0,opcode) == operation_object.getParm(1,opcode) else 0
        
        opcode[operation_object.parameters[2]] = output
        counter+=inputs+1
        #logging.info("Current State of the program is {}".format(opcode))
                


def number_of_paramaters(opcode):
    opcode = int(list(str(opcode))[-1])
    #logging.info("Request for {}".format(opcode))
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
        return 3
    elif opcode == 5 or opcode == 6:
        return 2
    elif opcode == 3 or opcode == 4:
        return 1
    else:
        return 0

def part1(OG_opcode):
    # Part 1
    max_output = 0
    for comb in permutations((0,1,2,3,4), 5):
        output = 0
        opcode_copy = OG_opcode.copy()
        for i in comb:
            output = iterate_program(opcode_copy, [i,output])
            #print("Ran iterate_program({}) and got {}".format(i, output))
        if output > max_output:
            max_output = output
    print("The maximum combination was {}".format(max_output))

if __name__ == "__main__":
    main()