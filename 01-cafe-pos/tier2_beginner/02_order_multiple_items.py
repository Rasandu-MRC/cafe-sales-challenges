"""
CHALLENGE: Take a Full Order
DIFFICULTY: Beginner
FOLDER: 01-cafe-pos / tier2_beginner

STORY
-----
A customer wants to order several things, one at a time, until they say
they're finished. You need to keep a running total of what they owe.

YOUR TASK
---------
1. Keep asking the customer "What would you like? (type 'done' to finish)"
2. Every time they type a valid menu item, add its price to a running total
   and print a short confirmation.
3. If they type something not on the menu (and not "done"), print a message
   saying it's not available, and ask again.
4. When they type "done", stop asking and print their final total.

EXAMPLE OUTPUT
--------------
What would you like? (type 'done' to finish): Coffee
Added Coffee - $4.5
What would you like? (type 'done' to finish): Muffin
Added Muffin - $5.0
What would you like? (type 'done' to finish): Pizza
Sorry, Pizza is not on the menu.
What would you like? (type 'done' to finish): done
Your total is $9.5

HINTS
-----
- Use a `while True:` loop, and use `break` to stop it when the customer
  types "done".
- Keep a variable like `total = 0` outside the loop, and add to it inside.
"""

from turtle import done


MENU = {
    "coffee": 4.50,
    "tea": 3.50,
    "muffin": 5.00,
    "toastie": 6.50,
    "hot chocolate": 4.00,
}


total = 0

# TODO: write a while loop that:
#   - asks "What would you like? (type 'done' to finish): "
#   - if the answer is "done", stops the loop
#   - if the answer is a valid menu item, adds its price to `total`
#     and prints "Added {item} - ${price}"
#   - otherwise prints "Sorry, {item} is not on the menu."


# TODO: after the loop finishes, print the final total, e.g. "Your total is $9.5"



while True:
   order_item = input("What would you like to order? (type 'done' to finish)").lower()

   if order_item == "done":
        break

   if order_item in MENU:
            total += MENU[order_item]
            print(f"Added {order_item} - ${MENU[order_item]}")
            print()
   else:
            print(f"Sorry, {order_item} is not on the menu.")
            print()

        
   
print()
print(f"Your total is ${total}")
