# CSCI 2061, Assignment 10, Problem 01
# Robert Niemann
# Biniam Lemma

# Person, super class
class Person(object):
    def __init__(self, name, age, address, typePerson):
        self.name = name
        self.age = age
        self.address = address
        self.typePerson = typePerson

    def restaurant(self):
        pass

    def order(self):
        pass
        
    def pay_bill(self, bill):
        pass

# Millionare, sub class
class Millionare(Person):
    def __init__(self, name, age, address, typePerson, vacationHomes):
        Person.__init__(self, name, age, address, typePerson)
        self.vacationHomes = vacationHomes

    def restaurant(self):
        print('Restaurant: Driver, take me to Mannys Steakhouse')

    def order(self):
        print('Order: Caviar, filet mignon, Lobster and several bottles of your best wine!')
        
    def pay_bill(self, bill):
        tip = bill / 2
        total = bill + tip
        print("Bill: Here you go ${}! And keep the change!".format(total))


# Teacher, sub class       
class Teacher(Person):
    def __init__(self, name, age, address, typePerson, mortgage):
        Person.__init__(self, name, age, address, typePerson)
        self.mortgage = mortgage

    def restaurant(self):
        print('Restaurant: Honey, how about Chilis tonight?')

    def order(self):
        print('Order: Can I have the special? And how much is a tall beer?')
        
    def pay_bill(self, bill):
        tip = bill * 0.15
        total = bill + tip
        print('Bill: Are you sure {} is correct? Ok, here you go {}'.format(bill, total))


# Student, sub class       
class Student(Person):
    def __init__(self, name, age, address, typePerson, rent):
        Person.__init__(self, name, age, address, typePerson)
        self.rent = rent

    def restaurant(self):
        print('Restaurant: MacDonalds or Culvers?')
        
    def order(self):
        print('Order: Burger and fries please!')
        
    def pay_bill(self, bill):
        print('Bill: Can I owe you {} bucks or do the dishes?'.format(bill))


# main function
def main():
    persons = []
    again = 'Y'

    ## Input data for different people and add appropriate object to list
    while(again == 'Y' or again == 'y'):

        name = input('Please enter the name: ')
        age = int(input('Please enter the age: '))
        address = input('Please enter the address: ')
        typePerson = input('Please enter the type of person: ')
        
        if typePerson.lower() == 'millionare':
            vacationHomes = int(input('How many vacation homes does he/she have? '))
            persons.append(Millionare(name, age, address, typePerson, vacationHomes))

        if typePerson.lower() == 'teacher':
            mortgage = float(input('How much mortgage is remaining? '))
            persons.append(Teacher(name, age, address, typePerson, mortgage))

        if typePerson.lower() == 'student':
            rent = float(input('How much is rent this month? '))
            persons.append(Student(name, age, address, typePerson, rent))

        again = input('Go again?')
        print()
        
        
    ## Display information for people in list
    for person in persons:
        print(person.typePerson, "", person.name)
        person.restaurant()
        person.order()
        bill = float(input('What is the bill?'))
        person.pay_bill(bill)
        print()
      

if __name__ == '__main__': main()
