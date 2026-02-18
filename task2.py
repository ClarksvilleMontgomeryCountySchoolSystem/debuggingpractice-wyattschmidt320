# Debugging Challenge - Part 2: Input and Data Conversion Errors
# Run this file, enter values when prompted, and use error messages to fix bugs
# DO NOT delete code - fix it!
#
# WARNING: Some errors will cause an unintended outcome without causing
# the program to fail with an error message. Before testing, check the
# program output to ensure the result is accurate. Adjust code as needed
# before running pytest.
#
# STEP 1: Fix bugs in main() while running with input
# STEP 2: Comment out main() to use predefined test values below
# STEP 3: Fix remaining bugs and run pytest


# --- Predefined Test Values (used when main() is commented out) ---
candy_quantity_str = "3"
soda_quantity_str = "2"
gallons_str = "10.5"
pounds_str = "1.25"
lottery_quantity_str = "5"


def main():
    global candy_quantity_str, soda_quantity_str, gallons_str, pounds_str, lottery_quantity_str
    candy_quantity_str = input("How many candy bars? ")
    soda_quantity_str = input("How many sodas? ")
    gallons_str = input("How many gallons of gas? ")
    pounds_str = input("How many pounds of deli meat? ")
    lottery_quantity_str = input("How many lottery tickets? ")


# Comment out the line below after fixing input bugs
#main()


# --- Receipt Header ---
print("""
========================================
       GAS STATION RECEIPT
      Thank you for shopping!
========================================
""")

# --- Candy Bars ---
# Price: $1.89 each (float price, int quantity)
candy_price = 1.89
candy_quantity = int(candy_quantity_str)
candy_total = candy_price * candy_quantity
print(f"Candy Bars: {candy_quantity} x ${candy_price} = ${candy_total}")

# --- Soda Bottles ---
# Price: $2.49 each (float price, int quantity)
soda_price = 2.49
soda_quantity = int(soda_quantity_str)
soda_total = soda_price * soda_quantity
print(f"Soda: {soda_quantity} x ${soda_price} = ${soda_total}")

# --- Gas ---
# Price: $3.25 per gallon (float price, float quantity)
gas_price = 3.25
gallons = float(gallons_str)
gas_total = gas_price * gallons
print(f"Gas: {gallons} gallons x ${gas_price} = ${gas_total}")

# --- Deli Meat ---
# Price: $8.99 per pound (float price, float quantity)
deli_price = 8.99
pounds = float(pounds_str)
deli_total = deli_price * pounds
print(f"Deli Meat: {pounds} lbs x ${deli_price} = ${deli_total}")

# --- Lottery Tickets ---
# Price: $2 each (int price, int quantity)
lottery_price = 2
lottery_quantity = int(lottery_quantity_str)
lottery_total = lottery_price * lottery_quantity
print(f"Lottery: {lottery_quantity} x ${lottery_price} = ${lottery_total}")

# --- Receipt Total ---
receipt_total = candy_total + soda_total + gas_total + deli_total + lottery_total
print(f"""
========================================
TOTAL: ${receipt_total}
========================================
Thank you! Come again!
""")
