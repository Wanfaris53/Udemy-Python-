print("Thank you for choosing Python Pizza Deliveries!\n")
size =input("What size pizza do you want? S, M, or L ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N ") # Do you want extra cheese? Y or N

total = 0

if size == 'S':
    total += 15
    if add_pepperoni == 'Y':
        total += 2
    elif add_pepperoni == 'N':
        total += 0
elif size == 'M':
    total += 20
    if add_pepperoni == 'Y':
        total += 3
    elif add_pepperoni == 'N':
        total += 0
elif size =='L':
    total += 25
    if add_pepperoni == 'Y':
        total += 3
    elif add_pepperoni == 'N':
        total += 0

if extra_cheese == 'Y':
    total += 1
elif extra_cheese == 'N':
    total += 0

print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${total}")