import logging
import sys

LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0"

def main():
    OG_opcode = list(map(int, input.split(',')))
    
    logging.basicConfig(format=LOGGING_FORMAT,
                        level=logging.INFO,
                        stream=sys.stdout)
    logging.info('Started the opcode program on an input of length {}'.format(len(OG_opcode)))

    for i in range(99):
        for j in range(99):
            OG_opcode[1] = i
            OG_opcode[2] = j

            logging.info('Testing opcode[1] as {} and opcode[2] as {}'.format(i, j))

            iterate_program(OG_opcode)

def iterate_program(opcode_local):
    counter = 0

    opcode = opcode_local.copy()
    while(counter<=len(opcode)):
        if(opcode[counter] == 99):
            logging.info('Final State was {}'.format(opcode[0]))
            return opcode[0]
        else:
            #logging.info('Program currenly is {}'.format(opcode))
            opcode = operate_program(opcode[counter:counter+4], opcode)
        counter+=4

    
    

def operate_program(operation, program):
    output = 0

    if(operation[0] == 1):
        output = program[operation[1]] + program[operation[2]]
    if(operation[0] == 2):
        output = program[operation[1]] * program[operation[2]]

    #logging.info('Operation was {} and output was {} into register {}'.format(operation, output, operation[3]))   
    program[operation[3]] = output

    return program


if __name__ == "__main__":
    main()