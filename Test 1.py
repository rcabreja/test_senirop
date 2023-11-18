#start of the cycle to show the 100 numbers
for number in range (1,101):
    #validation of multiple of 3 and 5
    if (number % 3 == 0) and (number % 5 == 0) : 
        print('Senir Op')

    #validation of multiple of 3
    elif(number % 3 == 0):
        print('Op')

    #default to show numbers
    else:
        print(number)
