children_age = [4,5,6,3,2]

children_age_gen = (age for age in children_age)

print(children_age_gen)

avg_children_age_gen = sum(age for age in children_age)/len(children_age)

print(avg_children_age_gen)