class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(["rainy", "snowy", "sunny", "hot", "cold"])
print("cloudy" in weather) 
print("snowy" in weather) 