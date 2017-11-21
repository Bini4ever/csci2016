# CSCI 2061, Assignment 10, Problem 02
# Robert Niemann
# Biniam Lemma
# This program creates a sqlite database and display. the program will
# allow the user to add more infromation, to search student, and to delete
# student fro the database

import sqlite3

# main function
def main():

    # Creating the database
    studentList = sqlite3.connect('studentList.db')
    studentList.execute('drop table if exists studentList')
    studentList.execute('create table studentList (t1 text, i1 int, t2 text, i2 float)')
    studentList.execute('insert into studentList (t1, i1, t2, i2) values (?, ?, ?, ?)', ('Ann Annson', 19, 'Freshman', 3.0))
    studentList.execute('insert into studentList (t1, i1, t2, i2) values (?, ?, ?, ?)', ('Bill Billson', 20, 'Sophmore', 3.4))
    studentList.execute('insert into studentList (t1, i1, t2, i2) values (?, ?, ?, ?)', ('Carl Carlson', 21, 'Junior', 4.0))
    studentList.execute('insert into studentList (t1, i1, t2, i2) values (?, ?, ?, ?)', ('Dawn Dawnson', 22, 'Senior', 2.7))


    # Display the database
    cursor = studentList.execute('select * from studentList order by t1')
    for row in cursor:
        print(row)
        
    print()
    var = 'y'


    # while loop that allow the user to enter multiple student's information
    while (var is not 'n'):
        # prompt the to enter additional students and add those students to the database
        name = input('Please enter student name: ') # enter the student's name
        age = int(input('Please enter student age: ')) # enter the age
        year = input('Please enter student year: ') # enter the year
        GPA = float(input('Please enter student GPA: ')) # enter the GPA
        # add the student into the studentList
        studentList.execute('insert into studentList (t1, i1, t2, i2) values (?, ?, ?, ?)', (name, age, year, GPA))
        # Ask the user if they want to enter another student's information
        # If 'y' for yes go again or if 'n' for no stop.
        var = input('Go again? ')
        # input validation
        if var not in ('y', 'n'):
            print("Please enter 'y' for yes and 'n' for no ")
            var = input('Go again? ')
            continue
             
    studentList.commit()


    # Display the database after the additions
    print()
    print("After additions, database is: ")
    cursor = studentList.execute('select * from studentList order by t1')
    for row in cursor:
        print(row)


    # Prompt the user to enter name to search from the database
    print()
    name = input('Student to search for? ')
    cursor = studentList.execute('select * from studentList order by t1')
    studentList.commit()
    # Search the student; if exist display the information
    for row in cursor:
        if (row[0].upper() == name.upper()):
            print(row)

    # Prompt the user to enter name to delete from the database
    print()
    name = input('Student to delete? ')
    
    # Search the student and delete from the database
    studentList.execute('delete from studentList where t1 = ?', (name,))
    studentList.commit()

    # display the rest data in the database
    print()
    print('After deletion, database is: ')
    cursor = studentList.execute('select * from studentList order by t1')
    for row in cursor:
        print(row)
    
if __name__ == "__main__":
    main()
