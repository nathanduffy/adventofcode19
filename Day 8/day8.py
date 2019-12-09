import functools

#input = "0222112222120000"
with open('input.txt', 'r') as file:
    input = file.read()


width = 25
height = 6

images = [None] * int(len(input)/(width*height))

for i in range(len(images)):
    images[i] = {
        'key': i,
        'num_zeros': 0
    }
    for x in range(height):
        for y in range(width):
            amount = ((x*width)+y)+(width*height*i)
            #print(input[amount])
            if input[amount] == '0':
                images[i]['num_zeros'] += 1
                #print("({},{}) = {}".format(x,y,input[amount]))

#print(images)
#print(functools.reduce(lambda a, b: a if a['num_zeros'] < b['num_zeros'] else b, images))

num_layers = int(len(input)/(width*height))

def translate_layer(layers):
    #print("Translating {}".format(layers))
    for layer in layers:
        if layer == '0':
            return ' '
        elif layer == '1':
            return '1'

image = [[None]*width]*height  
for i in range(height):
    return_string = ""
    for j in range(width):
        amount = (i*width)+j
        #print("({},{}) = {}".format(i,j, translate_layer(input[amount:width*height*num_layers:width*height])))
        return_string += str(translate_layer(input[amount:width*height*num_layers:width*height]))
    print(return_string)

#for i in range(width)
#    return_string = ""
#    for j in range(height)
#        return_string.append('')



# Another way
#for i in range(int(len(input)/(width*height))):
#    beginning = i*(height*width)
#    end = (i+1)*(height*width)
#    print("layer {} has {} 0's, {} 1s, and {} 2s".format(i, input[beginning:end].count('0'), input[beginning:end].count('1'), input[beginning:end].count('2')))