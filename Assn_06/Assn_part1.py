# CSCI 2061, Assignment 06, Problem 01
# Biniam Lemma
# This program generates days in the monts


# main function 
def main():

    add(1)
    add(1,2,3)
    add()
    add(1,2,3,4,5)

# 'add' function that take any number of arguments and returns their sum
def add(*args):
    ret = 0
    for n in args: 
        ret = ret + n
    print(ret)
   
if __name__ == "__main__":
    main()
