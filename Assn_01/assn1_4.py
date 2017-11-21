# Main function: calls addThree three times
# with 3 arguments, no arguments, and 1 arguments
def main():
    addThree(4, 5, 6) 
    addThree()
    addThree(4)

# AddThree function: passes three parameters and display sum
def addThree(a=1, b=2, c=3):
    print("The sum of the three values is ", a+b+c)
    
if __name__ == "__main__":
    main()
