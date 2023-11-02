import sys

def main():
    inputNumber = int(input("Enter a number: ")) #prompts user to enter a number
    if (inputNumber<0): #checks if number is negative
        print("Error: Please enter a positive number")
        sys.exit(1) # exits program with error code 1
    totalNumber = inputNumber
    while (totalNumber>152):
        totalNumber-=152
    print("The number you entered is: ",totalNumber) #displays the number to be saved to user
    #sys.exit(0) # exits program with success code 0

if __name__ == "__main__":
    main()