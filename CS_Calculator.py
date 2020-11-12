
# this is my new calculator

euros = float(input("How many euros do you have?: "))
yen = float(input("How many yen do you have?: "))

euros_to_dollars = (euros * 1.18)
yen_to_dollars = (yen * 0.0095)

usd = (euros_to_dollars + yen_to_dollars)

print("you currently have: ",usd,"usd")