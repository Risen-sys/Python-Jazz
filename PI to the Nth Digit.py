import decimal

def generate_pi(decimal_places):
    decimal.getcontext().prec = decimal_places + 2
    pi = decimal.Decimal(0)
    for k in range(1000):
        pi += (decimal.Decimal(1)/decimal.Decimal(16)**k) * (decimal.Decimal(4)/(8*k+1) - 
                                                             decimal.Decimal(2)/(8*k+4) - 
                                                             decimal.Decimal(1)/(8*k+5) - 
                                                             decimal.Decimal(1)/(8*k+6))
    return str(pi)[:-1]

decimal_places = int(input("Enter the number of decimal places for PI: "))
print(generate_pi(decimal_places))

