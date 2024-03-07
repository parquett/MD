#check if dict is full of 1
def fullDict(dict):
    for i in dict:
        if dict[i]!=1: return False
    return True

def truthTable(expression):
    expression = expression.lower()

    #defining qty of variables and print header
    count=0
    t=""
    for char in expression:
        if char.isalpha():
            if t.find(char)==-1:
                count=count+1
                t=t+char

    for x in t: print(x ,end =" | ")
    print(expression, end='\n')
    #----------------------------------

    dictionary = {}

    #making dictionary with variables
    for x in t:
        dictionary[x] = 0

    # truth table for zeros
    expressionCopy = expression
    for key in dictionary:
        expressionCopy = expressionCopy.replace(key, str(dictionary.get(key)))
    for x in dictionary: print(dictionary[x], end=" | ")
    print(eval(expressionCopy), end='\n')

    #go through the values of variables
    while not(fullDict(dictionary)):
        arr = list(dictionary.values()) #making an array containing the values of dictionary

        for idx in range(len(arr)):
            if arr[idx] == 0:
                arr[idx] = 1
                if idx != 0:
                    for jdx in range(len(arr)):
                        arr[jdx] = 0
                        if jdx + 1 == idx:
                            break
                break

        #truth table for others
        i = 0
        #updating the dictionary with new values
        for key in dictionary:
            dictionary[key] = arr[i]
            i = i+1

        expressionCopy = expression

        for key in dictionary:
            expressionCopy = expressionCopy.replace(key, str(dictionary.get(key)))


        for x in dictionary: print(dictionary[x], end = " | ")
        print(eval(expressionCopy), end='\n')


expression = "a&c"
truthTable(expression)