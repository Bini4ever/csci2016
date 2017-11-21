# CSCI 2061, Assignment 06, Problem 04
# Biniam Lemma
# This program generates days in the monts


# main program
def main():

    for i in monthDays(3, 3):
        print(i)

    print("=====")
    
    for i in monthDays():
        print(i)
    

# generator function 
def monthDays(start = 0, months = 12):
    i = start
    monthIndex = i + months
    days = 31
    
    while i < monthIndex:
        if i == 1:
            days -= 3
            yield days
            days += 3
        elif i == 3 or i == 5 or i == 8 or i == 10:
            days -= 1
            yield days
            days += 1
        else: yield days
        i+=1
        
    
if __name__ == "__main__":
    main()
