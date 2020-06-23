import random

i = 1
while (i):
    n = input("enter a 6 digit number :")
    if (len(n) != 6):
        print("invalid length, 6 digits expected")
    i = 0
    n = int(n)

gift_list = ["Suzuki Access scooty", "Royal Enfield bullet", "Tata Tigor car",
             "spiderman toy", "barbie doll", "dhothi", "T-shirt", "saree", "churidhar", "cosmetics",
             "dinner set", "parker pen", "Amazon gift card"]

sum_of_enter_number = 0  # exaple 1+2+3+4+5+6= 21
sum_of_added_number = 0  # example 2+1=3
while (n):
    sum_of_enter_number += (n % 10)
    n = n // 10
    if (n == 0):
        sum_of_added_number = sum_of_enter_number % 10
        sum_of_added_number += sum_of_enter_number // 10


h = [0] * 10

if (sum_of_added_number in random.sample(range(0, 9), 5)):
    a = random.choice(gift_list)
    if (h[sum_of_added_number] == 0):
        print("you won ", a)
    else:
        print(" sorry! already taken")
    if (sum_of_added_number < 3 and h[sum_of_added_number] != 1):
        h[sum_of_added_number] = 1
        gift_list.remove(a)

else:
    print("Try again better luck next time ")