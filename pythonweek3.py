def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
# prompt the user for input
original_price = float(input("enter the original price of the item:"))
discount_percentage= float(input("enter the discount percentage:"))
final_price =  calculate_discount(original_price, discount_percentage)
print(final_price)