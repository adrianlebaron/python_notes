from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451

# How to Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python

from decimal import Decimal

product_cost = 88.90
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))

# Overview of Popular Math Functions in Python Video

import math

loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss)))     #gets the values in the parenthesis first.
print(round(product_cost))
print(math.sqrt(product_cost))  #gives Decimal
print(math.pow(5, 2))     # 5 square same as the one below
print(5 ** 2)
