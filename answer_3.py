def printLine(inputStr, inputNum):
    result = ""
    words = inputStr.split()
    #print(words,end="")

    for word in words:
        if (len(result) + len(word) > inputNum):
            print(result)
            result = ""

        result = result + word + " "

    print (result)

if __name__ == '__main__':
    
    print("Enter the Line")
    inputStr = input()

    print("Enter the number")
    inputNum = int(input())
    printLine(inputStr, inputNum)
    
