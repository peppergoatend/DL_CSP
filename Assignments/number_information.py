# DL, Number Information

for number in range (1,21):
    if number%5 == 0:
        divided_5 = "divisible by 5."
    else:
       divided_5 = "is not divisble by 5."
    if number%2 == 0:
        odd_even = "even"
    else:
        old_even = "odd"
print(f"{number} is {odd_even} and {divided_5}")
