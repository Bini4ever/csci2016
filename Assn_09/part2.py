# CSCI 2061, Assignment 09, Problem 02
# biniam Lemma
# This program display the containt of the containers
# and calculate the shopping bill as well as display
# out of stock items
def main():
    y=0

    #containers
    shoppingList = { 'lettuce': 5, 'potato': 2, 'onion': 1}
    inventory = {'potato': 6, 'lettuce': 0, 'onion': 32, 'carrots': 15}
    prices = {'potato': 4, 'lettuce': 2, 'onion': 1.5, 'carrots': 3}

    #call printInventory function that displays the itms
    print('Item\t\t', 'Price\t\t', 'Quantity\t', 'Value')
    for i in inventory:
        printInventory(i, inventory[i], prices[i])

    #diplay the shpping bill as well as out of stock item
    print()
    print('Your shopping bill is:')
    print()
    for x in shoppingList:
        y += computeBill(x, shoppingList[x], inventory[x], prices[x])
    print()
    print('The total bill is $', y)

#printInventory function to display the items   
def printInventory(x, inv, pr):
    print(x, '  \t$', pr, '\t\t', inv, '\t\t$', (pr * inv))

#computeBill function to display the shopping bill
def computeBill(x, shop, inv, pr):
    total = 0
    if inv is 0:
        print(x, "\t\t- out of stock.")
    else:
        total = shop*pr
        print(x, 'at $', pr, 'each\t- total ${}'.format(total))
    return total


if __name__ == "__main__":
    main()
