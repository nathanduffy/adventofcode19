import logging
import sys

LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
input_program = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"

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
        #print("This was the output of the program {}".format(print_comp))
        print(print_comp)
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