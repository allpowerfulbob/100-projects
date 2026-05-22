
def c_to_f(c):
    return c * 9/5 + 32
def f_to_c(f):
    return (f-32)*5/9
def c_to_k(c):
    return c + 273.15
def k_to_c (k):
    return k - 273.15
def convert ():
    while True:
        scale = input("Choose scale (C)elsius, (F)arenheit, "
                    "(k)elvin: ").upper()
        try:
            value = float(input("Enter temperature: "))
        except ValueError:
            print("Error: Please enter a numeric value.")
            continue
        if scale == "C":
            print ("Farenheit: ", c_to_f(value))
            print ("Kelvin: ", c_to_k(value))
        elif scale == "F":
            c = f_to_c(value)
            print ("Celcius: ", c)
            print ("Kelvin: ",  c_to_k(c))
        elif scale == "K":
            c = k_to_c(value)
            print ("Celcius: ", c)
            print ("Farenheit: ", c_to_f(c))
        else:
            print ("Unkown Scale.")
            continue
        again = input("conver another? (y/n):").lower()
        if again != "y":
            break