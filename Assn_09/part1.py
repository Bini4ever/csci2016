# CSCI 2061, Assignment 09, Problem 01
# biniam Lemma
# This program defines a dictionary wallet that contains
# a dictionary money, a list creaditCards, a list Id
# and a dictionary copons.
def main():
    
    wallet = { 'money': { 20: 2, 10: 1, 5: 0, 1: 4},
               'creaditCards':[ 'Visa', 'Discovery', 'MasterCard'],
               'IDs':['Drivers License', 'Student ID' ]} 

    # For loop to add the total amout of the money
    total = 0
    for i in wallet['money']:
        total+= i * wallet['money'][i]
    
    # Display the wallet container
    print("Wallet Contents:")
    print()
    for i in wallet:
        if i is 'money':
            continue
        print(i, ':')
        for x in wallet[i]:
            print(x)
        print()

    # Display the total amout of money       
    print('Total case is: ${}'.format(total))
    print()

    wallet['coupons'] = {'Cub': "meat", 'Kohls': 'shirt', 'Target': 'toothpaste'}
    wallet['money'][20] += 3
    del wallet['creaditCards'][1]

    # For loop to add the total amout of the money
    total = 0
    for i in wallet['money']:
        total+= i * wallet['money'][i]

    # Display the wallet container
    print("After changes, wallet Contents are:")
    print()
    for i in wallet:
        if i is 'money':
            continue      
        print(i, ':')
        if i is 'coupons':
            for x in wallet[i]:
                print(x, '\t', wallet[i][x])
            print()
            continue
        for x in wallet[i]:
            print(x)
        print()

    # Display the total amout of money       
    print('Total case is: ${}'.format(total))

if __name__ == "__main__":
    main()
