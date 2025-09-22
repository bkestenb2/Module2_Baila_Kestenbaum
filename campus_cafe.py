"""
Psuedocode:
set coffe price = 2.25 and muffin = 2.75 and print out to user 
Ask user quantity of each item (coffe and muffin) and tip amount (main) 
Create function to compute the total for each item (line total)
create function to compute tax(.00875), tip, and total/subtotal (compute totals)
creat function to print out a neat receipt format with coffee qty x amount = total, same with muffin, and add the 2 for a subtotal.  Add in tax and tip amount, and give the total (print receipt)
create function to format currency to 2 decimal places with a $ symbol (format currency)
"""
# === Campus Cafe Program ===

def format_currency(x: float) -> str: #formating currency to 2 decimal places and a $ symbol into a string
    return f"${x:.2f}"

def line_total(unit_price: float, qty: int) -> float: #getting the total for each item changing into a float
    return unit_price * qty

def compute_totals(subtotal: float, tax_rate: float, tip_percent: float) -> tuple[float, float, float]: #computing the totals and changing into tuple
    tax = subtotal * tax_rate #tax amount
    tip = subtotal * tip_percent / 100 #tip amount
    total = subtotal + tax + tip #total
    return (tax, tip, total)

def print_receipt(coffee_qty: int, muffin_qty: int, coffee_price: float, muffin_price: float, tip_percent: int): #output receipt
    coffee_total = line_total(coffee_price, coffee_qty) #how much coffee
    muffin_total = line_total(muffin_price, muffin_qty) #how many muffins
    subtotal = coffee_total + muffin_total #subtotal
    tax, tip, total = compute_totals(subtotal, 0.08875, tip_percent)
#The actual output
    print("\n== Receipt ==") 
    print(f"{coffee_qty} x Coffee @ {format_currency(coffee_price)} = {format_currency(coffee_total)}")#coffe amount x coffee cost = total coffee cost
    print(f"{muffin_qty} x Muffin @ {format_currency(muffin_price)} = {format_currency(muffin_total)}")#muffin amount x muffin cost = total muffin cost
    print(f"Subtotal: {format_currency(subtotal)}")# subtotal, fromat 2 decimal places with $ symbol
    print(f"Tax (8.875%): {format_currency(tax)}")# tax, format 2 decimal places with $ symbol
    print(f"Tip ({tip_percent}%): {format_currency(tip)}")# tip, format 2 decimal places with $ symbol
    print(f"TOTAL: {format_currency(total)}")# total, format 2 decimal places with $ symbol
    print("Thank you!")  
    
def main():  #menu output
    coffee_price = 2.25
    muffin_price = 2.75
    print("== Campus Cafe ===")
    print("Coffee: $2.25")
    print("Muffin: $2.75")

    try: 
        coffee_qty = int(input("How many cups of coffee? "))#user input amount of coffee
        muffin_qty = int(input("How many muffins? "))#user input amount of muffins
        tip_percent = int(input("Tip percent: "))#user input amount tip

        if coffee_qty < 0 or muffin_qty < 0 or tip_percent < 0:
            raise ValueError("All inputs must be positive integers.") #if put in number less than 0, prompts error

    except ValueError:
        print("Invalid input, please insert a positive integer.") #if put in word instead of integer, promps errror
        return

    print_receipt(coffee_qty, muffin_qty, coffee_price, muffin_price, tip_percent)

# Run the program
if __name__ == "__main__":
    main()




"""
Original:
Call function campus_cafe_total
Ask the user how many cups of coffe they want
create variable "coffee" = 2.25
Ask the user how many muffins they want
create variable "muffin" = 2.75
add tax subtotal*.08875
add tip subtotal*(tip percent/100)
Add all together
Print receipt by doing # x item name @ price = line total (so 2 lines)
Print subttl,tax,tip,and total on seperate lines \n
Format $ with 2 decimal places

Code:
print ("Coffee - $2.25")
print ("Muffins - $2.75")
def campus_cafe_total():
    question1 = "How many cups of coffee?" #created variable question1 to find out how many cups of coffee
    coffee = int(input(question1)) #allowing for user to input amount
    coffeecost = 2.25 #creating a variable to use as the cost of 1 coffee
    totalcoffee = coffeecost*coffee #finding total cost of coffee
    question2 = "How many muffins?" #created variable question1 to find out how many muffins
    muffin = int(input(question2)) #allowing for user to input amount
    muffincost = 2.75 #creating a variable to use as the cost of 1 muffin
    totalmuffin = muffincost*muffin #finding total cost of muffins
    subtotal = totalmuffin + totalcoffee
    tax = subtotal * .08875
    tipq = "Percent tip" #creating a variable for the percent of tip to be inputed
    tippercent = float(input(tipq)) #allowing for user to input percent amount
    tip = subtotal*(tippercent/100) #figuring out total tip amount
    total = subtotal + tax + tip
    subtotal = round(subtotal, 2)
    print(f"{coffee} x coffee @ $2.25 = {totalcoffee}")
    print(f"{muffin} x muffin @ $2.75 = {totalmuffin}")
    print(f"subtotal: ${subtotal}")
    print(f"tax(8.875%): ${round(tax, 2)}")
    print(f"tip amount: ${round(tip, 2)}")
    print(f"Total: ${round(total, 2)}")


campus_cafe_total()
"""
