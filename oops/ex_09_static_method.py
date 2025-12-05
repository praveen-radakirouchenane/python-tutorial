class Restaurant:

    @staticmethod
    def restaurant_names(names):
        return [name.strip() for name in names.split(',')]
    

raw_names = " a2b  ,  thaitree,  mexico, petu"
cleaned_names = Restaurant.restaurant_names(raw_names)
print(raw_names)
print(cleaned_names)