# set
s = {1, 2, 3, 4, 5}
print(s)

# constructor
se = set()
print(se)

seq = set([3, 4, 5])
print(seq)

# add method

seq.add(6)

seq.update([7, 8])

print(seq)

# remove
seq.remove(6)  # throw exception if not present

print(seq)

seq.discard(8)
print(seq)

# copy
sq = seq.copy()
print(sq)

# set operations
blue_eye = {'Olivia', 'Harry', 'Lilly', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lilly', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# union
print(f"Union : {blue_eye.union(blond_hair)}")

# intersection
print(f"Blue and blond hair : {blue_eye.intersection(blond_hair)}")

#  difference
print(f"Difference blond hair and blue eyes : {blond_hair.difference(blue_eye)}")

# symmetirc difference
print(f"Difference blond hair and blue eyes : {blond_hair.symmetric_difference_update(blue_eye)}")

# subset
print(f"smel_hc is subset of blond hair : {smell_hcn.issubset(blond_hair)}")

# super set
print(f"taste_ptc is superset of smell_htc: {taste_ptc.issuperset(smell_hcn)}")

# disjoint
print(f"a blodd disjoint o blood : {a_blood.isdisjoint(o_blood)}")

