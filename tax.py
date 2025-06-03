tax_13_max = 2400000 * 0.13 # 13% base is max 2.4 million
tax_15_max = 2600000 * 0.15 # 15% base is max 2.6 million: greater that 2.4 and less then 5.0
tax_18_max = 15000000 * 0.18 # 18% base is max 15.0 million: greater that 5.0 and less then 20.0
tax_20_max = 30000000 * 0.2 # 20% base is max 30.0 million: greater that 20.0 and less then 50.0

def tax(gross: float):
    if gross <= 2400000:
        return 0.13 * gross
    elif gross <= 5000000:
        remainder = (gross - 2400000) * 0.15
        return tax_13_max + remainder
    elif gross <= 20000000:
        remainder = (gross - 5000000) * 0.18
        return  tax_13_max + tax_15_max + remainder
    elif gross <= 50000000:
        remainder = (gross - 2000000) * 0.2
        return tax_13_max + tax_15_max + tax_18_max + (gross - 20000000) * 0.2
    else: # big boss
        return tax_13_max + tax_15_max + tax_18_max + tax_20_max + (gross - 50000000) * 0.22

def net(gross: float):
    return gross - tax(gross)

def print_income_info(gross: float):
    net_yearly = net(gross)
    print("gross yearly is", gross, ", net yearly is: ", net_yearly, ", net average monthly", net_yearly / 12, ", tax is: ", tax(gross))

gross_per_month = int(input("Enter gross per month: "))
print_income_info(gross_per_month * 12)
