# CSCI 2061, Assignment 06, Problem 04
# Biniam Lemma
# This program generates days in the monts

# main function
def main():
    highScore( ann = 100, bob = 90, carol = 80, dave = 70)
    highScore( ann = 100, bob = 90, carol = 80, dave = 70, ed = 69)
    highScore( ann = 100, bob = 90)
    
# 'highScore' function that print the highest score 
def highScore(**kwargs):
    name = ""
    score = 0
    
    for k in kwargs:
        if score < kwargs[k]:
            name = k
            score = kwargs[k]
            
    print("The highest score was: ", name, kwargs[name])
    print()
    
if __name__ == "__main__":
    main()
