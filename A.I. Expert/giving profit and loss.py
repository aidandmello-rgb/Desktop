costprice = float(input("Enter the cost price: "))
sellingprice = float(input("Enter the selling price: "))

if sellingprice > costprice:
    profit = sellingprice - costprice
    print("Profit:", profit)
else:
    loss = costprice - sellingprice
    print("loss:", loss)