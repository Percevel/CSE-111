import csv
print("Inkom Emporium")
print()

products = {}
with open("proving3/products.csv", "rt") as pfile:
    reader = csv.reader(pfile)
    next(reader)
    for row in reader:
        val = [row[1],float(row[2])]
        products[row[0]] = val


totItem = 0
totPrice = 0

print("Requested Items")
with open("proving3/request.csv", "rt") as rfile:
    reader = csv.reader(rfile)
    next(reader)
    for row in reader:
        prod = products[row[0]]
        print(f"{prod[0]}: {row[1]} @ {prod[1]}")
        totItem += int(row[1])
        totPrice += float(prod[1]) * int(row[1])

print()
salesTax = totPrice * .06
print(f"Number of Items: {totItem}")
print(f"Subtotal: {totPrice}")
print(f"Sales Tax: {salesTax:.2f}")
print(f"Total: {(totPrice+salesTax):.2f}")