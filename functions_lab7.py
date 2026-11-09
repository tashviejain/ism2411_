#Answers to Self Assesment Questions
# 1: The first bug I found was the indentation error in a statment that was 5 spaces instead of the standard 4. I figured this out through the traceback. Since I could not spot this myself, I believe I need to improve on spotting issues.
# 2: This code uses a customer's tier to determine how much of a discount should be applied to the original cost. The inputs are the price and tier. It returns the final price after the discount is applied. A colleague could use it without reading the body because the function is clear about what it does by just the code itself. 
# 3: I used AI on exercise 5 to understand some of the traceback error messages. Hence. AI helped build my understanding. This is because it taught me what the error meant.


#Exercise 1

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"] :
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
    
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

#Exercise 5 
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total:.2f}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#Exercise 6
x = 100
def double_it():
    x = 999
    return x * 2

print (x)
print(double_it())
print(x)