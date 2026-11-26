def calculate_discount(price, discount):
    return price - (price * discount / 100)

final_price = calculate_discount(1000, 10)
print(final_price)
