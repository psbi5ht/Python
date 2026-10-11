cart = []
prices = []

print("--- Welcome to the Supermarket ---")

# 1. The WHILE loop collects items until the user decides to stop
while True:
    item = input("Enter item name (or type 'checkout' to finish): ")
    
    if item.lower() == 'checkout':
        break # Breaks out of the while loop
        
    price = float(input(f"Enter price for {item}: ₹"))
    
    # Save the data to our lists
    cart.append(item)
    prices.append(price)
    print(f"🛒 Added {item} to cart.\n")

print("\n--- Final Receipt ---")

# 2. The FOR loop goes through the fixed list to display items
total_cost = 0
for i in range(len(cart)):
    print(f"{cart[i]}: ₹{prices[i]:.2f}")
    total_cost += prices[i]

print("---------------------")
print(f"Total Amount Due: ₹{total_cost:.2f}")
print("Thank you for shopping with us!")
