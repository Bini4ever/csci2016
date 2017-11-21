#Assn04_part2, Biniam Lemma
#This program ask the user to enter numbers and do operations
#including add, subtraction, multiplcation and division.
def main():

    print("************ Calculator Program ************")

    #a wile loop to print the menu and to process the calculation.
    while (1):
        print('''

              1. Add
              2. Subtract
              3. Multiply
              4. Divide
              5. Quit\n''')

        x = int(input("Enter your choice: "))
 
        if x == 5:
            break

        #input validation
        if x > 5 or x < 1:
            print("You should choice should be a number between 1 and 5")
            continue

        #input the numbers
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        if x == 1:
            addNum(a, b)
        elif x == 2:
            subtractNum(a, b)
        elif x == 3:
            multiplyNum(a, b)
        elif x == 4:
            divideNum(a, b)
        
        
     
#this function add two numbers
def addNum(a, b):
    print("The sum of {} and {} is".format(a, b), (a + b))

#this function subtract numbers
def subtractNum(a, b):
    print("The Difference of {} and {} is".format(a, b), (a - b))

#this function multiply two numbers
def multiplyNum(a, b):
    print("The Product of {} and {} is".format(a, b), (a * b))

#this function divide numbers
def divideNum(a, b):
    print("The Quotient of {} and {} is".format(a, b), (a / b))


if __name__ == "__main__":
    main()
