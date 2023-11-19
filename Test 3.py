
import time

class BicycleLock():
    @classmethod
    def makeDistinct(array, input):
        control=0
        output=list('')
        for element in range(0, int(len(input))):
            for number in range(0, int(len(input))):
                if element == number:                    
                    break

                if input[element] == input[number]:
                    output.append('>')                    
                    input[number] += 1
                    equal=1
                    equal_control=0
                    while equal == 1:           
                        for i in range(0, int(len(input))):
                            if input[number] == input[i]:
                                output.append('+')
                                control += 1
                                input[number] += 1
                            else:
                                equal_control = 1
                        if equal_control == 1:
                            equal=0               
                    if control == 100:
                        break
        output = "".join(output)
        return output



bicy_lock = ([8, 8, 0, 9])
print(BicycleLock.makeDistinct(bicy_lock))

