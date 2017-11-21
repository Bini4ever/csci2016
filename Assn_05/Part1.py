# CSCI 2061, Assignment 05, Problem 01
# Biniam Lemma
# Employee Payroll Program

# main program
def main():
    print("**************** Payroll Program ****************")
    print()
    print("****************   Data Input    ****************")
    numEmployees = int(input("Please enter the number of employees: "))
    print()
    employeeNames = []
    employeeRates = []
    employeeHours = []
    employeeWages = []

    # loop to enter payroll data
    for employeeNumber in range(numEmployees):
        while True:
            print("Data entry for employee {}".format(employeeNumber + 1))

            # throw exceptions
            try:
                name = readName()
                rate = readRate()
                hours = readHours()
                
            except EmpNameError as e: 
                print(e, "\nPlease Start over\n")
                continue
            except RateError as e:
                print(e, "\nPlease Start over\n")
                continue
            except HoursError as e:
                print(e, "\nPlease Start over\n")
                continue
            except ValueError as e:
                print("Data entered in incorrect format\nPlease start over\n")
                continue
            except TypeError as e:
                print("Data entered in incorrect format\nPlease start over\n")
                continue
            else:
                employeeNames.append(name)
                employeeRates.append(rate)
                employeeHours.append(hours)
                employeeWages.append(employeeHours[employeeNumber] * employeeRates[employeeNumber])
                print()
                break
            print()
            print()

    print()
    print("****************  Payroll Data  ****************")
    for employeeNumber in range(numEmployees):
        print("Employee: {}".format(employeeNames[employeeNumber]))
        print("   Hours: {}".format(employeeHours[employeeNumber]))
        print("   Rate:  ${}/hr".format(employeeRates[employeeNumber]))
        print("   Wage:  ${}".format(employeeWages[employeeNumber]))
        print()

 #Thrown if employee name is zero length
class EmpNameError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

 #Thrown if hourly rate <0 or > 20
class RateError(Exception): 
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



# Thrown if weekly hours <0 OR > 60
class HoursError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



# function readName
def readName():
    ret = input("Enter the employee name: ")
    if ret == "":
        raise EmpNameError('Name cannot be zero length')
    else: return ret

# function readRate
def readRate():
    ret = float(input("Enter the employee wage rate (0..20): "))
    if ret < 0 or ret > 20:
        raise RateError('Hourly rate must be between 0 and 20')
    else: return ret

# function readHours
def readHours():
    ret = float(input("Enter the employee hours (0..60): "))
    if ret < 0 or ret > 60:
        raise HoursError('Hours must be between 0 and 60')
    else: return ret

if __name__ == "__main__": main()

