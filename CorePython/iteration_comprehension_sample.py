# Comprehensions Iteration Sample
import math
# general form

# [expression(item) for item in iterable]

# list comprehension
words = "Why sometimes I have believed as six impossible things before breakfast".split()

words_leng = [len(word) for word in words]

print(f"list comprehension : {words_leng}")

# set comprehensive
set_fact = [len(str(math.factorial(x))) for x in range(20)]
print(f"set comprhension: {set_fact}")

# dictionary comprehension
# genral form : {key_exp(key) : value_expr(value) for key , value in iterables}
country_to_capital = { 'United Kingdom': 'UK',
                       'India': 'Delhi',
                       'Moroco': 'Rabat',
                       'Sweden': 'Stockholm'}
capital_to_county = {capital: country for country, capital in country_to_capital.items()}
print(f"dictionary comprehension :  {capital_to_county}")






