import random
import string

s_letters = list(string.ascii_lowercase)
s_letters.remove('l') # Exclude small letter l
s_letters.remove('o') # Exclude small letter o

# choose 4 random small letter characters using list comprehension
random_small_ch = [random.choice(s_letters) for i in range(4)]  
# print(random_small_ch) # ['d', 'c', 'm', 'm']

b_letters = list(string.ascii_uppercase)
b_letters.remove('O') # Exclude capital letter O
b_letters.remove('I') # Exclude capital letter I

random_cap_ch = [random.choice(b_letters) for i in range(4)]
# print(random_cap_ch) # ['B', 'H', 'V', 'I']

numbers = list(range(2, 10)) # exclude numbers 0 and 1 to avoid confusing with letters l and o or O respectively
random_nums = [random.choice(numbers) for i in range(2)]
# print(random_nums) # [9, 5]

special_chars = ['!', '@', '#', '$', '%', '&', '*']

special_chars = [random.choice((special_chars)) for i in range(2)]
# print(special_chars) # ['*', '@']

# combine all characters
raw_chars = random_small_ch + random_cap_ch + random_nums + special_chars

shuffled_chars = [random.choice(raw_chars) for i in range(len(raw_chars))]

def converts(s):
    new = ""
    for c in s:
        new += str(c)
    return new

print(converts(shuffled_chars))