#Assn4_part1, Biniam Lemma, 09/15/16
#This payroll program calculates employees' wage and display
def main():

    print("************** Payroll Program ****************\n")
    print("**************** Data Input *******************")
    x = input("Please enter the number of employees: ")
    x = int(x)
    y = 0

    #initalize the array list to null
    name = []
    hours = []
    wageRate = []
    wage = []
    y = 0

    #while loop to input name, wagerate and hours
    while y < x:
       print('')
       name.append(input("Enter the employee name: "))
       wageRate.append(float(input("Enter the employee wage rate: $")))
       hours.append(float(input("Enter the emplyee hours: ")))
       y += 1

    y = 0
    #calculate the wage
    while y < x:
       wage.append(wageRate[y] * hours[y])
       y += 1

    #output the payrool Data
    print("\n************** Payroll Data ****************")
    y = 0
    while y < x:
       print("Employee:", name[y])
       print("\tHours:", hours[y])
       print("\tRate:  ${}/hr".format(wageRate[y]))
       print("\tWage:  ${}\n".format(wage[y]))
       y += 1

    
if __name__ == "__main__":
    main()
