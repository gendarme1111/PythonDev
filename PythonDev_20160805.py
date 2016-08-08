
#literalIn = input("Please input your name: ")
#print(literalIn)

priceIn = input("Please input the price: ")
quantityIn = input("Please input the quantity: ")
print("Total: %.5f, %d = %10.2f" % (float(priceIn), int(quantityIn), float(priceIn) * int(quantityIn)))