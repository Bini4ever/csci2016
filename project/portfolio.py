# CSCI 2061, Final Project.
# Robert Niemann
# Biniam Lemma and Ismail Abiola
# This program use for keeping track of the value of a group of stockes.
import sqlite3
import collections


#***************************    Main function   *****************************************
#                                                                                       *                                                                                           
# The main function will give the usere a choise for Adding and Deleting stockes,       *
# Loading file, Updating prices, Reporting with sorting either by name or value,        *
# and Quit                                                                              *
#                                                                                       *                                                                                   
#****************************************************************************************
def main():
    
    fileName = '' # variable to store the name of the file
    disc = {} # variable to store the dictionary 

    # list choises, so the user choose one
    choise = input('(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ')

    # A while loop that operate different taskes until the user enter Q of quit
    while (choise.upper() != 'Q'):

        # if the user entered L load file
        if (choise.upper() == 'L'):
            fileName = input('Load file: ')
            print()
            portfolioList = sqlite3.connect(fileName)
            cursor = portfolioList.execute('select * from portfolioList order by t1')
            disc = creatDisc(cursor)

        # if the user entered R for report ask whether they would like to sort by name or value
        elif (choise.upper() == 'R'):
            sortby = input('Sort output on (N)ame, or (V)alue? ')

            # sorting by name - call sortByName() function to sort by name
            if (sortby.upper() == 'N'):
                sortByName(fileName)

            # sorting by Value - call sortByValue() function to sort by value
            elif (sortby.upper() == 'V'):
                sortByValue(fileName)

        # if the user entered A add additional ticker - call addTicker() to add
        elif (choise.upper() == 'A'):
            addTicker(fileName)

        # if the user entered D delete ticker - call removeTicker() to delete
        elif (choise.upper() == 'D'):
            removeTicker(fileName)

        # if the user entered U update the price - call updatePrice() to ubdate
        elif (choise.upper() == 'U'):
            updatePrices(fileName)

        # list the choise again
        choise = input('(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ')

    # if user entered Q ask to save the file or not
    YorN = input("Save " + fileName + "(y/n)")
    if YorN.upper() == "Y":
        portfolioList.commit()
    print()
    print("Bye.")





#***************************    CreatDisc function   ********************************
#                                                                                   *
# creatDisc function create a Dictionary of the file list                           *
#                                                                                   *
#************************************************************************************  
def creatDisc(cursor):
    d = {}
    for row in cursor:
        gl = ((row[4] - row[3]) * 100)/row[3]
        d[row[1]] = [row[0], row[1], row[2], row[3], row[4], row[2] * row[4], gl]
    return d


#***************************    addTicker function   ********************************
#                                                                                   *
# addTicker function adds a stock to the portfolio                                  *
#                                                                                   *
#************************************************************************************ 
def addTicker(fileName):

    print('Add a stock to your portfolio...')
    print()

    ticker = input('Ticker: ')
    name = input('Company Name: ')
    number = int(input('Number of shares: '))
    price = float(input('Purchase price per share: $'))

    portfolioList = sqlite3.connect(fileName)
    portfolioList.execute('insert into portfolioList (t1, t2, i1, i2, i3, i4) values (?, ?, ?, ?, ?, ?)', (ticker, name, number, price, price, number*price))
    portfolioList.commit()



#***************************    removeTicker function   *****************************
#                                                                                   *
# RemvoeTicker function deletes spacific ticker form the portfolio                  *
#                                                                                   *
#************************************************************************************ 
def removeTicker(fileName):

    symbol = input("Enter the ticker symbol of the stock to remove: ")
    symbol = symbol.upper()
    portfolioList = sqlite3.connect(fileName)
    portfolioList.execute('delete from portfolioList where t1 = ?', (symbol,))
    portfolioList.commit()



#***************************    UpdateTicker function   *****************************
#                                                                                   *
# updateTicker function that updates spacific stock price                           *
#                                                                                   *
#************************************************************************************ 
def updatePrices(fileName):
    print('Update stock prices (<Return> to keep current value)...')
    print()
    portfolioList = sqlite3.connect(fileName)
    cursor = portfolioList.execute('select * from portfolioList order by t2')

    for row in cursor:
        var = row[0] + ": "
        i3 = float(input(var))
        i4 = row[3] * i3
        portfolioList.execute('update portfolioList set i3 = ? where i4 = ?', (i3, i4,))
 

    portfolioList.commit()       


#***************************    sortByName function   *******************************
#                                                                                   *
# sortByName function sorts the file by name                                        *
#                                                                                   *
#************************************************************************************ 
def sortByName(fileName):
 
    portfolioList = sqlite3.connect(fileName)
    cursor = portfolioList.execute('select * from portfolioList order by t1')
    disc = creatDisc(cursor)
    d = collections.OrderedDict(sorted(disc.items()))
    displayList(d)
    portfolioList.commit()
    


#***************************    sortByValue function   ******************************
#                                                                                   *
#  sortByValue function sorts the portfolio by value                                *
#                                                                                   *
#************************************************************************************ 
def sortByValue(fileName):

    portfolioList = sqlite3.connect(fileName)
    cursor = portfolioList.execute('select * from portfolioList order by i4')
    disc = creatDisc(cursor)          
    displayList(disc)
    portfolioList.commit()



    
#***************************    displayList function   ******************************
#                                                                                   *
#  DisplayList function displays the portfolio                                      *
#                                                                                   *
#************************************************************************************ 
def displayList(d):
    total = 0.0
    totalgl = 0.0

    for key in d.keys():
        total += d[key][5]
        totalgl += d[key][6]

    tab1 = "\t"
    tab2 = "\t\t"
    tab3 = "\t\t\t"
    tab4 = "\t\t\t\t"
    tab7 = "\t\t\t\t\t\t\t\t"

    print('Company\t\t\t\t\tShares\tPur.\tLatest\tValue\t\t    G/L')
    print('===========================================================================================')
    for key in d.keys():
        if (len(key + d[key][0]) > 20):
            print(key, '(', d[key][0], ')', tab2 , d[key][2], '\t', d[key][3], '\t', d[key][4], '\t',d[key][5], '\t', "{:.2f}".format(d[key][6]), '%')
        elif (len(key + d[key][0]) > 15):
            print(key, '(', d[key][0], ')', tab2 , d[key][2], '\t', d[key][3], '\t', d[key][4], '\t',d[key][5], '\t\t', "{:.2f}".format(d[key][6]), '%')
        elif (len(key + d[key][0]) > 9):
            print(key, '(', d[key][0], ')', tab3 , d[key][2], '\t', d[key][3], '\t', d[key][4], '\t',d[key][5], '\t', "{:.2f}".format(d[key][6]), '%')
        elif (len(key + d[key][0]) > 5):
            print(key, '(', d[key][0], ')', tab4 , d[key][2], '\t', d[key][3], '\t', d[key][4], '\t',d[key][5], '\t', "{:.2f}".format(d[key][6]), '%')
        else:
            print(key, '(', d[key][0], ')', tab4 , d[key][2], '\t', d[key][3], '\t', d[key][4], '\t',d[key][5], '\t', "{:.2f}".format(d[key][6]), '%')

    print(tab7, '-------------------------')
    print(tab7, "{:.2f}".format(total), '\t', "{:.2f}".format(totalgl))
    print(tab7, '=========================')

    

if __name__ == "__main__":
    main()
