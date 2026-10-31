 #


foods=[]
cost=[]
total=0


while True:
    food = input("Enter the name of the food to order (done to quit): ")
    if food.lower() == "done":
        break
    else:
        price=float(input(f"Enter the price of the {food}: "))
        foods.append(food)
        cost.append(price)
        
print(foods)
print(cost)
    
print("_________BILL_________")
for food in foods:
    print(food)
    
for price in cost:
        total +=price
print(total)
