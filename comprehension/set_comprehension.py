fruits = ["apple", "banana", "cherry", "date", "elderberry", "apple"]

my_favorite_fruits = {fruit for fruit in fruits }

print(my_favorite_fruits)


cuisines = {
    "indian": ["dal", "biryani", "samosa", "curry"], 
    "chinese": ["noodles","curry"],
    "thai": ["curry", "red curry", "green curry"]
}

unique_dishes = { dish for dishes in cuisines.values() for dish in dishes if "curry" in dish}

print(unique_dishes)