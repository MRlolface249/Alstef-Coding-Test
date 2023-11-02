import sys
import os

# function to read persisted number from file
def readPersistedNumber(fileName):
    if os.path.exists(fileName): # checks if file exists
        with open(fileName, 'r') as file: # opens file to read
            persistedNumber = int(file.read())
            file.close() # closes file after use
            return persistedNumber
    else:
        return 0

# function to save current number to file
def persistCurrentNumber(fileName, currentNumber):
    with open(fileName, 'w') as file: # opens file to write
        file.write(str(currentNumber))
        file.close() # closes file after use

def main():
    persistednumber = readPersistedNumber('number.txt')
    inputNumber = int(input("Enter a number: ")) #prompts user to enter a number
    if (inputNumber<0): #checks if number is negative
        print("Error: Please enter a positive number")
        sys.exit(1) # exits program with error code 1
    totalNumber = inputNumber
    while (totalNumber>152):
        totalNumber-=152
    print("The number you entered is: ",totalNumber) #displays the number to be saved to user
    #sys.exit(0) # exits program with success code 0
    persistCurrentNumber('number.txt', totalNumber)

if __name__ == "__main__":
    main()