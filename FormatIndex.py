quantity=3
item=567
price=30000
myorder="i want to pay{2}dollars for {0} pieces of item{1}"
print(myorder.format(quantity,item,price))

OUTPUT:
i want to pay30000dollars for 3 pieces of item567
