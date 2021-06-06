print("$ python snakes_cafe.py")
print("*"*40)
print("**  Welcome to the Snakes Cafe!  **")
print("**")
print("** To quit any time, type \"quit\" **\n")
print("*"*40)

print("Appetizers\n")
print("-------\nWings\nCookies\nSpring Rolls\n")
print("Entrees\n")
print("-------\nSalmon\nStake\nMeat Torando\nA Literal Garden\n")
print("Drinks\n")
print("-------\nCoffee\nTea\nUnicorn Tears\n")

print("********************************\n** What do you like to order? **\n********************************\n")
order = input("> ")
count = 0
appetizers = ["Wings", "Cookies", "Spring Rolls", "salmon", "Steak", "Meat Torando", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
#entrees = ["salmon", "Steak", "Meat Torando", "A Literal Garden"]
#desserts = ["Ice Cream", "Cake", "Pie"]
#drinks = ["Coffee", "Tea", "Unicorn Tears"]

for items in appetizers:
    if order == items:
        count =+1
        print(f"\n** {count} order of {order} have been added to your meal**")
        order = input("> ")
    
    