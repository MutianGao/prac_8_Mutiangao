from prac_08.silver_service_taxi import SilverServiceTaxi

test_car = SilverServiceTaxi('Hummer', 200, 4)
test_car.drive(18)
print(test_car.get_fare_number())
print(test_car)