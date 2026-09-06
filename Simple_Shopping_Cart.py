# Simple Shopping Cart

customer_name = input("Enter customer name: ")

subtotal = 0
products = []

for i in range(1, 4):
    product_name = input(f"Enter product {i} name: ")
    price = float(input(f"Enter product {i} price: "))

    products.append((product_name, price))
    subtotal += price

# Calculate discount
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_total = subtotal - discount

# Display output
print(f"\nCustomer Name: {customer_name}")

for i, product in enumerate(products, start=1):
    print(f"\nProduct {i}: {product[0]}")
    print(f"Price: {product[1]}")

print(f"""
Subtotal: {subtotal}
Discount: {discount}
Final Total: {final_total}
""")