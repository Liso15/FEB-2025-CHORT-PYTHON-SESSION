#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent /100)
        print(f"Discounted price: {discounted_price}")
        return discounted_price
    else:
        print(f"Original price: {price} (No discount applied)")
        return price

final_price = calculate_discount(100,50)
final_price = calculate_discount(100,2)           

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#Calculate the final price usin the function
final_price = calculate_discount(original_price, discount_percent)

# print the result

if discount_percent >= 20:
    print(f"Final price after applying {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Original price: {"final_price"}")


