class Restaurant:

    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year + 1
    
    @year.setter
    def year(self, year):
        if 2000 <= year <= 2025:
            self._year = year
        else:
            raise ValueError(f"This is not acceptable year")
        

res = Restaurant(2000)
print(res.year)
res.year = 2025
print(res.year)