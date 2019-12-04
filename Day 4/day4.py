def main():
    min = 245182
    max = 790572

    possiblePWs = []
    for num in range(min, max+1, 1):
        everDecreases = False
        containsDouble = False
        num = str(num)

        i=1
        while(i<6):
            if(int(num[i]) < int(num[i-1])):
                everDecreases = True or everDecreases
            if(int(num[i]) == int(num[i-1])):
                containsDouble = True
            #print("num[i] is {} and num[i-1] is {}. everDecreases is {} and containsDouble is {}".format(num[i], num[i-1], everDecreases, containsDouble))
            i+=1

        #print("Testing {} which containsDoubles = {} and onlyIncreases = {}".format(num, containsDouble, not(everDecreases)))

        if (not everDecreases) and containsDouble:
            possiblePWs.append(num)

    print("The total length is {}".format(len(possiblePWs)))

    finalPWList = []
    #possiblePWs = [112233, 123444, 111122]

    for pw in possiblePWs:
        inarow = 1
        passesLastCheck = False
        pw = str(pw)
        i=1

        while(i<6):
            if(int(pw[i]) == int(pw[i-1])):
                inarow +=1
            else:
                if inarow==2:
                    passesLastCheck = True
                inarow = 1
            i+=1

        
        if passesLastCheck or inarow==2:
            finalPWList.append(pw)

    print("The total number of passwords that match this new criteria is {}".format(len(finalPWList)))
    #print("And they are {}".format(finalPWList))


if __name__ == "__main__":
    main()