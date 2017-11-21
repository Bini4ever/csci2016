# Main function calculates and display cos of a stock transaction,
# commission and the total amount
def main():
    sCost = 750 * 35.0
    cCost = sCost * 0.02
    tCost = sCost + cCost
    print("Stock cost: $ ", sCost)
    print("Commission cost: $ ", cCost)
    print("Total cost : $", tCost)
    
if __name__ == "__main__":
    main()
