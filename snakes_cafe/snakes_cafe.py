from textwrap import dedent
appetizers = {
    "Wings":0, 
    "Cookies":0,
    "Spring Rolls":0,
    "salmon":0, 
    "Steak":0, 
    "Meat Torando":0, 
    "A Literal Garden":0, 
    "Ice Cream":0, 
    "Cake":0, 
    "Pie":0, 
    "Coffee":0, 
    "Tea":0, 
    "Unicorn Tears":0
}
menu_items = dedent(
"""
Appetizers
{}
{}
{}
Deserts
one
two
""".format(*appetizers)
)
greeting = dedent(
    """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
)
ask_order = dedent(
    """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
)

print(greeting)
print(menu_items)

while True:
    order = input("> " + ask_order)
    if order == "quit":
        break
    order = order.title()
    if order not in appetizers:
        print("Sorry! ....")
    else:
        appetizers[order] +=1
        print(f"** {appetizers[order]} order of {order} have been added to your meal**")
print("Thank you for your visit")
    
    