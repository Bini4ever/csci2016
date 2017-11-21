# CSCI 2061, Assignment 06, Problem 04
# Biniam Lemma
# This program generates days in the monts

# main function
def main():

    print( add(1,2,3,4) )
    print( add(1,2,3) )
    print( add(1,2) )
    print( add(1) )
    print( add()) 

# 'add' function that sum and return all arguments passed to it
def add(first = None, second = None, thrid = 1, fourth = 1):
    ret = 0
   
    if first == None and second == None:
        ret = thrid + fourth
    elif second == None:
        ret = first + thrid + fourth
    else:
        ret = first + second + thrid + fourth
    return ret
   
if __name__ == "__main__":
    main()
