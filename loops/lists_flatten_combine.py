# How to Combine and Flatten Lists in Python with the For / In Loop videos


legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)  #append is a key word

print(new_customers)