import random, string

lower = list(string.ascii_lowercase)
lower.remove('l') # Exclude l
lower.remove('o') # Exclude o
lower_case = "".join(lower)

upper = list(string.ascii_uppercase)
upper.remove('O') # Exclude O
upper.remove('I') # Exclude I
upper_case = "".join(upper)

numbers = "23456789" # Exclude 0 and 1

special_chars = "@#$&_-()=%*:/!?+."

pass_raw = lower_case + upper_case + numbers + special_chars

length = int(input("How Many Characters Do You Want Your Password To Be: "))
password = "".join(random.sample(pass_raw, length))

print("Password: " + password)