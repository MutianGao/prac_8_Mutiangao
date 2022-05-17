from prac_08.car import Car


class SilverServiceTaxi(Car):
    price_per_km = 1.23
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(), self.current_fare_distance, SilverServiceTaxi.price_per_km * self.fanciness, self.flagfall)

    def get_fare_number(self):
        return SilverServiceTaxi.price_per_km * self.current_fare_distance * self.fanciness

    def start_fare_number(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance = self.current_fare_distance + distance_driven
        return distance_driven
