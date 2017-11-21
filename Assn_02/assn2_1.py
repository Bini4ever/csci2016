def main():

    a = 5
    b = 3
    c = a/b
    d = round(a/b, 2)
    e = a//b
    f = a%b

    print("a and b are ", a, " and ", b)
    print("a divided by b is ", c)
    print("a divided by b but rounded to two places is ", d)
    print("a divided by b using integer division is ", e)
    print("a modulus is ", f)
    
if __name__ == "__main__":
    main()
