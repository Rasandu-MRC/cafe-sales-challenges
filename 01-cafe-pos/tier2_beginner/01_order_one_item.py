"""
CHALLENGE: Look Up One Item's Price
DIFFICULTY: Beginner
FOLDER: 01-cafe-pos / tier2_beginner

STORY
-----
A customer walks up to the counter and asks for one item by name. You need
to check the menu, tell them the price if it exists, or apologise if it
doesn't.

YOUR TASK
---------
1. The MENU dictionary below stores each item name and its price.
2. Ask the customer what they'd like using input().
3. Check whether that item exists in MENU.
   - If it does, print its price using the format shown in the example.
   - If it doesn't, print a polite "sorry, we don't have that" message.

EXAMPLE OUTPUT (customer types "Tea")
--------------------------------------
What would you like to order? Tea
Great choice! Tea costs $3.5.

EXAMPLE OUTPUT (customer types "Pizza")
-----------------------------------------
What would you like to order? Pizza
Sorry, we don't have Pizza on the menu today.

HINTS
-----
- Use `item_name in MENU` to check if a key exists in a dictionary.
- Use `MENU[item_name]` to get the price once you know it exists.
"""

MENU = {
    "coffee": 4.50,
    "tea": 3.50,
    "muffin": 5.00,
    "toastie": 6.50,
    "hot chocolate": 4.00,
}


# TODO 1: ask the customer what they would like, using input(), and store
#         their answer in a variable called order_item

# TODO 2: check whether order_item exists in MENU
#         - if it does: print "Great choice! {order_item} costs ${price}."
#         - if it doesn't: print "Sorry, we don't have {order_item} on the menu today."

order_item = input("What do you like to order? ").lower()

if order_item in MENU:
   print(f"Great choice! {order_item.upper()} - costs ${MENU[order_item]}")

else:
   print(f"Sorry, we don't have {order_item.upper()} on the Menu today.")
   print()
   print("Here is the Menu...")
   print (MENU)
   print()
   order_item = input("What do you like to order?")
