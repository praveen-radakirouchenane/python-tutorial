class BaseRestaurant: 
    def __init__(self,type_):
        self.type = type_

    def cuisine(self):
        print(f"This is {self.type} cuisine")

class ThaiRestaurant(BaseRestaurant):
    def prepare(self):
        print(f"This is Restaurant")

class IndianRestaurant: 
    ind_cls = BaseRestaurant # Composition(not inheriting just refering); Refers the base class and can access only it's values 

    def __init__(self):
        self.name = self.ind_cls("Indian") # creating an object using reference 

    def serve(self):
        print(f"This is {self.name.type} restaurant")
        self.name.cuisine()

class MultiCusineRestaurant(IndianRestaurant): # inheriting
    ind_cls = ThaiRestaurant # composition 


# thai_res = ThaiRestaurant("Thai")
# thai_res.prepare()
# thai_res.cuisine()

# ind_res = IndianRestaurant()   
# ind_res.name.cuisine()
# ind_res.serve()

multi_res = MultiCusineRestaurant()
multi_res.serve()
multi_res.ind_cls.prepare("Thai")

