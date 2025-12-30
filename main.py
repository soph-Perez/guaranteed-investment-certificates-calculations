print(f"\n{'Term (in Years)':>10} {'Interest Rate (as Percentage)':>30}") # loop through this
print(f"{'1':>8} {'4.9':>24}")
print(f"{'2':>8} {'4.1':>24}")
print(f"{'3':>8} {'4.0':>24}")
print(f"{'4':>8} {'3.8':>24}")
print(f"{'5':>8} {'3.75':>24}\n")

gic_term = int(input("Enter GIC Term: "))

if gic_term not in (1,2,3,4,5):
  print("Invalid input. Enter only the options shown above.\n")
  exit()

match gic_term: # can use dictionary
  case 1:
    interest_rate = 4.9
  case 2:
    interest_rate = 4.1
  case 3:
    interest_rate = 4.0
  case 4:
    interest_rate = 3.8
  case 5:
    interest_rate = 3.75

amount = float(input("Enter amount to invest: "))

total_interest = amount*gic_term*(interest_rate/100)

total_amount = total_interest + amount

print(f"Interest at end of term = ${total_interest:,.2f}")
print(f"Total at end of term = ${total_amount:,.2f}\n")