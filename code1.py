foods = []
prices = []
total = []

while True:
    food = input(f"Enter a food to buy(q to quit)")
    if food == "q":
        break
    else: 
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------- YOUR CHART --------")    
 
for food in foods:
    print(foods, end=" ")
for price in prices:
     total =+ price
print(f"Your total is: ${total}")
