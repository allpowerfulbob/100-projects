rates = {
    ("USD", "EUR"): 0.92,
    ("USD", "GBP"): 0.80,
    ("EUR", "USD"): 1.09,
    ("GBP", "USD"): 1.25,
    ("EUR", "GBP"): 0.87,
    ("GBP", "EUR"): 1.15
    }
print ("Simple Currency Converter")
from_curr = input ("From (USD/EUR/GBP): ").upper()
to_curr = input("To (USD/EUR/GBP): ").upper()
amount = float(input("Amount: "))
if (from_curr, to_curr) in rates:
    result = amount * rates[(from_curr, to_curr)]
    print("Converted amount: ", result)
else:
    print("Conversion not supported.")