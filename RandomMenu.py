from random import *
entrees=["burger", "chicken", "steak", "pasta"]
sides=["macaroni and cheese", "salad", "fries", "biscuit", "coleslaw", "fruit"]
desserts=["sundae", "cheesecake", "strawberry shortcake", "pie"]
drinks=["soda", "smoothie", "milkshake", "water"]

print("Here's your random menu:")

EntreeIndex=randint(0, len(entrees)-1)
SidesIndex=randint(0, len(sides)-1)
SidesIndex2=randint(0, len(sides)-1)
DessertIndex=randint(0, len(desserts)-1)
DrinkIndex=randint(0, len(drinks)-1)

print("Your entree is", entrees[EntreeIndex])
print("Your sides are", sides[SidesIndex], "and", sides[SidesIndex2])
print("Your dessert is", desserts[DessertIndex])
print("Your drink is", drinks[DrinkIndex])

dessertprice=randint(3,7)
entreeprice=randint(7,12)
sidesprice=randint(3,6)
sidesprice2=randint(2,5)
drinkprice=randint(1,3)

'''if EntreeIndex==0 or 3:
    entreeprice=9
else:
    entreeprice=12
if SidesIndex==0 or 2 or 3:
    sidesprice=3
else:
    sidesprice=5
if SidesIndex2==0 or 2 or 3:
    sidesprice2=3
else:
    sidesprice2=5
if DessertIndex==0 or 1:
    dessertprice=7
else:
    dessertprice=5
if DrinkIndex==0 or 3:
    drinkprice=1
else:
    drinkprice=3'''

print("Your total cost is", entreeprice+sidesprice+dessertprice+sidesprice2+drinkprice, "dollars")
