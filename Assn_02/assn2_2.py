def main():

    t = ('one', 'two', 'three', 'four')
    l = [3.3, 1.1, 2.2]
    d = { 33333333: 'Carol Carolson', 22222222: 'Bill Billson', 11111111: 'Ann Annson' }
    
    print("First a tuple! ")
    print(type(t), t)
    
    print("tuple sorted: ", sorted(t))
    print("\nNext a list. ")
    print(type(l), l)
    l.append(4.4)
    l.insert(0, 0.0)
    print("list with two new values inserted! ", l)
    print("list sorted: ", sorted(l))
    print("\nAnd last but not least, a dictionary! ")
    print(type(d), d)
    print("dictionary sorted: ")
    for k in sorted(d.keys()):
        print(k, d[k])
    
    
if __name__ == "__main__":
    main()
