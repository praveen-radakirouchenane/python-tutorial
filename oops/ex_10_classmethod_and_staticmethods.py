class Restaurant:

    def __init__(self, name, cuisine, location):
        self.name = name
        self.cuisine = cuisine
        self.location = location

    @classmethod
    def from_dict(cls, restaurant_dict):
        return cls(
            restaurant_dict["name"],
            restaurant_dict["cuisine"],
            restaurant_dict["location"]
        )
    
    @classmethod
    def from_string(cls, restaurant_string):
        name, cuisine, location = restaurant_string.split('-')
        return cls(
            name,
            cuisine,
            location
        )
    
class RestaurantUtil:

    def is_valid_location(location):
        return location in ['east','west','north']
    
restaurant_1 = Restaurant.from_dict({"name":"petu","cuisine":"indian","location":"west"})
print(restaurant_1)
print(restaurant_1.__dict__)


restaurant_2 = Restaurant.from_string("hut-thai-east")
print(restaurant_2)
print(restaurant_2.__dict__)

is_valid_location = RestaurantUtil.is_valid_location('south')
print(is_valid_location)