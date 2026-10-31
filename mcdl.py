mcdl = {
    "chicken popcorn": 130,
    "burger": 90,
    "large bucket": 200,
    "mid bucket": 170,
    "small bucket": 130,
    "fries": 100,
    "coke": 80,
    "chilled coke": 120,
}

cart = {}
total = 0

print("__________MENU__________")
for item, price in mcdl.items():
    print(f"{item:20}: {price}")
print("_______________________")

while True:
    food = input("Enter the item from menu (done to quit): ").lower().strip()

    if food == "done":
        break
    elif food in mcdl:
        try:
            qty = int(input(f"Enter the quantity of {food}: "))
            if qty <= 0:
                print("Quantity must be at least 1!")
                continue
        except ValueError:
            print("Please enter a good quantity >_<")
            continue

        cart[food] = cart.get(food, 0) + qty
    else:
        print("invalid choice!!?")

print("_________BILL__________")
for item, qty in cart.items():
    cost = mcdl[item] * qty
    print(f"{item:15} x{qty:<3}  {mcdl[item]:<4} \n = {cost}")
    total += cost

print("_______________________")
print(f"Total: {total}")