price=float(24.95)
discount=float(0.4)
copies=60

single=price*(1-discount)
#this is the price for each copy

total=single*copies
#this is the price for all copies

shipping=(single-1)*0.75+3
#this is the shipping cost

cost=shipping+total
print(cost)