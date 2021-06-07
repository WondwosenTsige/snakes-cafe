from textwrap import dedent
menu_items_list = {
    "Wings":0, 
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0, 
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
our_menu = dedent(
"""
Appetizers
-----------

{}
{}
{}

Entrees
-----------

{}
{}
{}
{}

Deserts
-----------

{}
{}
{}

Drinks
-----------

{}
{}
{}
""".format(*menu_items_list)
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
print(our_menu)
print(ask_order)

while True:
    order = input("> ")
    if order == "quit":
        break
    order = order.title()
    if order not in menu_items_list:
        print(f"Sorry! We dont have {order} in our menu")
    else:
        menu_items_list[order] +=1
        print(f"** {menu_items_list[order]} order of {order} have been added to your meal**")
print("Thank you for your visit")
    
    