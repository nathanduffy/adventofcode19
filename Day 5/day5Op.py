import logging
import sys

LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
input_program = "3,225,1,225,6,6,1100,1,238,225,104,0,1001,152,55,224,1001,224,-68,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,62,41,225,1101,83,71,225,102,59,147,224,101,-944,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,2,40,139,224,1001,224,-3905,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,6,94,224,101,-100,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,75,30,225,1102,70,44,224,101,-3080,224,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,55,20,225,1102,55,16,225,1102,13,94,225,1102,16,55,225,1102,13,13,225,1,109,143,224,101,-88,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1002,136,57,224,101,-1140,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,101,76,35,224,1001,224,-138,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,677,224,102,2,223,223,1005,224,434,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,494,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1006,224,539,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,644,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226"

class operation:
    def __init__(self, input=[]):
        '''Create operation from an array. 
                First Item: the opcode
                Last Item: the return
                Middle: the parameters'''
        instruction = str(input[0]).zfill(5)
        
        self.opcode = int(instruction[-1])
        #self.output_loc = input[len(input)-1]
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

    iterate_program(OG_opcode)

def iterate_program(opcode_local):
    counter = 0
    opcode = opcode_local.copy()
    
    while(counter<=len(opcode)):
        
        inputs = number_of_paramaters(opcode[counter])
        
        operation_object = operation(opcode[counter:counter+(inputs+1)])
        #logging.info("This is the object {}".format(operation_object))

        if(opcode[counter] == 99):
            #logging.info('Final State was {}'.format(opcode[0]))
            return opcode[0]
        if(operation_object.opcode == 5):
            # Jump if True
            if operation_object.getParm(0, opcode):
                counter = operation_object.getParm(1, opcode)
            else:
                counter += inputs+1
        elif(operation_object.opcode == 6):
            # Jump if False
            if not operation_object.getParm(0, opcode):
                counter = operation_object.getParm(1,opcode)
            else:
                counter += inputs+1
        else:
            opcode = execute_operation(operation_object, opcode)
            #logging.info("Current State of the program is {}".format(opcode))
            counter+=inputs+1


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
    

def execute_operation(operation, program):
    output = 0
    parms = operation.parameters

    if(operation.opcode == 1):
        #1 means addition
        output = operation.getParm(0, program) + operation.getParm(1, program)
    if(operation.opcode == 2):
        #2 means multiplication
        output = operation.getParm(0, program) * operation.getParm(1, program)
    if(operation.opcode == 7):
        # Less than
        output = 1 if operation.getParm(0,program) < operation.getParm(1,program) else 0
    if(operation.opcode == 8):
        # Equals
        output = 1 if operation.getParm(0,program) == operation.getParm(1,program) else 0
    if(operation.opcode == 4):
        print_comp = operation.getParm(0, program)
        print("This was the output of the program {}".format(print_comp))
    elif operation.opcode == 3:
        #take input and save it to the parameter
        output = int(input("What is the input for the program "))
        program[operation.parameters[0]] = output
    else:
        #logging.info('Operation was {} and output was {} into register {}'.format(operation, output, operation[3]))   
        program[operation.parameters[2]] = output
    
    return program


if __name__ == "__main__":
    main()