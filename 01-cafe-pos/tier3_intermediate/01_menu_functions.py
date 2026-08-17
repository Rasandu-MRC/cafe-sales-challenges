"""
CHALLENGE: Rebuild Ordering With Functions
DIFFICULTY: Intermediate
FOLDER: 01-cafe-pos / tier3_intermediate

STORY
-----
The head barista wants the ordering logic cleaned up so different parts of
the café's system can reuse it. Instead of one long block of code, you'll
break the logic into three separate functions.

YOUR TASK
---------
Implement the three functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom to run a full ordering loop.

EXAMPLE OUTPUT
--------------
What would you like? (type 'done' to finish): Coffee
Added Coffee - $4.5
What would you like? (type 'done' to finish): Muffin
Added Muffin - $5.0
What would you like? (type 'done' to finish): done

----- RECEIPT -----
Coffee            $4.50
Muffin            $5.00
--------------------
TOTAL:            $9.50
"""

MENU = {
    "coffee": 4.50,
    "tea": 3.50,
    "muffin": 5.00,
    "toastie": 6.50,
    "hot chocolate": 4.00,
}


def get_price(item_name):

    if item_name is None:
        return None

    return MENU.get(str(item_name).strip().lower())   # not sure from Copilot AI assitance


def calculate_total(order_list):

    total = 0
    for item in order_list:
        price = get_price(item)
        if price is not None:
            total += price
    return total


def display_receipt(order_list, total):

    print()
    print("-------- RECEIPT --------")
    for item in order_list:
        price = get_price(item)
        if price is not None:
            print(f"{item.title():<18} ${price:.2f}")
    print("-------------------------")
    print(f"TOTAL:            ${total:.2f}")


if __name__ == "__main__":
    order_list = []             # not sure from AI assitance

    while True:
        order_item = input("What would you like? (type 'done' to finish): ").strip().lower()

        if order_item == "done" or order_item == "finish":
            break

        if order_item in MENU:
            order_list.append(order_item) # append mean? (from AI assitance)
            print(f"Added {order_item.title()} - ${MENU[order_item]:.2f}")
        else:
            print(f"Sorry, {order_item} is not on the menu.")

    total = calculate_total(order_list)
    display_receipt(order_list, total)



