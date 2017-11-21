# CSCI 2061, Assignment 10, Problem 01
# Robert Niemann
# Biniam Lemma
# This program propts the user to enter strings and write them to a file.
# After writing it to file it open the file for input and display the contents.

# Main function 
def main():

    #variables
    var = 'y';
    charCount = 0
    alphaCount = 0
    numCount = 0
    spaceCount = 0
    wordCount = 0

    # open new file called 'sentence.txt' to write the file in it
    outfile = open('sentence.txt', 'w')

    # prompt the user to enter the sentence and write them in the file 'sentence.txt'
    while var is not 'n':
        sent = input("Please enter a sentence: ")
        outfile.write(sent + '\n')
        var = input("Go again? ")
        if var not in ('y', 'n'):
            print("please for YES enter 'y' and for NO 'n'")
            var = input("Go again?")
        

    # close the file
    outfile.close()

    # open the file for input and diplay the content
    # and count each characters, words, alphabetic caracters,
    # numeric caracters, and white spaces.
    infile = open('sentence.txt', 'r')
    print()
    print("File contents are: ")
    for line in infile:
        print(line, end='')
        wordCount += len(line.split())
        charCount += len(line)
        for ch in line:
            if ch.isalpha():
                alphaCount += 1
            elif ch.isnumeric():
                numCount += 1
            elif ch.isspace():
                spaceCount += 1
    # close the file 
    infile.close()

    # display the values for counted words, characters, alphabetic caracters,
    # numeric caracters, and white spaces.
    print("Character count: \t\t{}".format(charCount))
    print("Alphabetic character count: \t{}".format(alphaCount))
    print("Numeric character count: \t{}".format(numCount))
    print("Whitespace character count: \t{}".format(spaceCount))
    print("Word count: \t\t\t{}".format(wordCount))

    
    
if __name__ == "__main__":
    main()
