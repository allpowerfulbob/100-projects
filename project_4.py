rates = {
    ("USD", "EUR"): 0.92,
    ("USD", "GBP"): 0.80,
    ("EUR", "USD"): 1.09,
    ("GBP", "USD"): 1.25,
    ("EUR", "GBP"): 0.87,
    ("GBP", "EUR"): 1.15
    }
print ("Simple Currency Converter")
def convert_currency(frm, to, value):
    if (frm, to) in rates:
        return value * rates[frm, to]
    else:
        return None
def run_converter():
    while True:
        frm = input("Convert from (USD/EUR/GBP): ").upper()
        to = input("Convert to (USD/EUR/GBP): ").upper()
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Error: amount must be a number.")
            continue
        result = convert_currency(frm, to, amount)
        if result is None:
            print("Conversion not available.")
        else:
            print("Result: ", result)
        again = input("Would you like another conversion? (y/n): ").lower()
        if again !="y":
            break