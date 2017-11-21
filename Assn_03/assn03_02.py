#Assn3.part2, Biniam Lemma, 09/08/2016
#This program prompts the user for thhe number of students
#and number of tests per student, then it calculates the
#average for all three tests.

def main():

    a = input("Enter the number of students: ")
    b = input("Enter the number of tests: ")
    a = int(a)
    b = int(b)
    x = 0
    totalav = 0
    
    while (x < b):
       total = 0.0
       av = 0.0
       print("\n****************Test {} Scores****************\n".format(x+1))
       y = 0
       z = 0
       scores=[]
       while (y < a):
           var = input("Enter the score for test {} for the student {} : ".format(x+1, y+1))
           scores.append(var)
           y=y+1

       while (z < a):
           total = total + float(scores[z])
           z = z+1
       av = total/a
       totalav = totalav+av
       print("Average for test {} was ".format(b), av)
       
       x=x+1
    overalav = totalav/b
    print ("\nAverage for all three tests was ", overalav)

    
if __name__ == "__main__":
    main()
