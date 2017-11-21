# CSCI 2061, Assignment 07, Problem 01
# Biniam Lemma
# This program calculates monthly payments and total payments of mortgage

#Mortgage class
class Mortgage:

    #No arg Constractor
    def __init__():
        self._loanAmount = 0
        self._annualRate = 0
        self._years = 0
    
    #Constractor that tekes three arguments and initializes the data memebers
    def __init__(self, loanAmount = 0, annualRate = 0, years = 0):
        self._loanAmount = loanAmount
        self._annualRate = annualRate
        self._years = years
        self._monthlyRate = annualRate/12
        self._numPayments = years*12

    #setLoanAmount method that initializes the loanAmount
    def setLoanAmount(self, loanAmount):
         self._loanAmount = loanAmount

    #setLoanAmount method that initializes the annualRate and monthlyRate
    def setAnnualRate(self, annualRate):
         self._annualRate = annualRate
         self._monthlyRate = annualRate/12

    #setLoanAmount method that initializes the years and numbPayments
    def setYear(self, years):
         self._years = years
         self._numPayments = years*12

    #getMonthlyPayment, accessor method, that calculate and returns the monthlyPayment       
    def getMonthlyPayment(self):
         self._monthlyPayment = self._loanAmount * (self._monthlyRate*(1+self._monthlyRate)**self._numPayments)/(((1 + self._monthlyRate)**self._numPayments) - 1)
         return self._monthlyPayment

    #getPayBack, accessor method, that calculates and returns the total payment
    def getPayBack(self):
         return self.getMonthlyPayment() * self._numPayments

#main function
def main():

    #mortgag class invocation to creat an object
    mortgage1 = Mortgage(1000, 0.12, 10)
    mortgage2 = Mortgage()
    mortgage2.setLoanAmount(2000)
    mortgage2.setAnnualRate(0.06)
    mortgage2.setYear(20)

    #Displaying the results
    print('1st Mortgage is for $1000, 12% interest rate and a period of 10 years')
    print('Monthly payment for 1st mortgage is ${:.2f}'.format(mortgage1.getMonthlyPayment()))
    print('Total Payments for 1st mortgage is ${:.2f}'.format(mortgage1.getPayBack()))
    print()
    print('2st Mortgage is for $2000, 06% interest rate and a period of 20 years')
    print('Monthly payment for 2st mortgage is ${:.2f}'.format(mortgage2.getMonthlyPayment()))
    print('Total Payments for 2st mortgage is ${:.2f}'.format(mortgage2.getPayBack()))


     

    
if __name__ == "__main__":
    main()
