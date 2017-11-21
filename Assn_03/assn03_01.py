#Assn03part01.cpp, Biniam Lemma, 09/08/16
#This program calculates how long it takes sound to travel
#through air, water or steel.

def main():
    
        #ask the user to select a medium and distance in feet
        print("select a medium: \n\n1. Air\n2. Water\n3. Steel\n")
        x = input("Enter your choice: ")
        x = int(x)

        # 0 validation 
        while x < 1:
                print ("Please choose between 1 and 3")
                x = input("Enter your choice: ")
                x = int(x)
        while x > 3:
                print ("Please choose between 1 and 3")
                x = input("Enter your choice: ")
                x = int(x)

        #ask the user to enter the distance              
        dist = input( "Enter the distance in feet: ")
        dist = int(dist)

        #conditonals to calculate the distance for each choice
        if x == 1:
            if dist == 0:
                print("\nDistance must be greater than zero.\m\n")
            else:
                print("\nA shound wave takes ", (dist/1100), " seconds to travel ", 
                        dist, " feet through air.\n\n")
        elif x == 2:
            if dist == 0:
                print("\nDistance must be greater than zero.\n\n")
            else:
                print("\nA shound wave takes ", (dist/4900), " seconds to travel ", 
                        dist, " feet through water.\n\n")
        elif x == 3:
            if dist == 0:
                print("\nDistance must be greater than zero.\m\n")
            else:
                print("\nA shound wave takes ", (dist/16400), " seconds to travel ", 
                        dist, " feet through water.\n\n")
            
              
    
if __name__ == "__main__":
    main()
