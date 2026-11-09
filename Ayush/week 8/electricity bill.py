import sys
electricity_bill = input("Enter your electricity bill units: ")
if electricity_bill.isdigit():
    electricity_bill = float(electricity_bill)
    if electricity_bill <= 100:
        bill_amount = electricity_bill * 0.5
    elif electricity_bill <= 200:
        bill_amount = (100 * 0.5) + ((electricity_bill - 100) * 0.75)
    elif electricity_bill <= 300:
        bill_amount = (100 * 0.5) + (100 * 0.75) + ((electricity_bill - 200) * 1.20)
    else:
        bill_amount = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((electricity_bill - 300) * 1.50)

    print("\033[32mYour electricity bill amount is: £{:.2f}\033[0m\n".format(bill_amount))
else:
    print("\033[31mInvalid input. Please enter a valid number of units.\033[0m\n")
sys.exit()