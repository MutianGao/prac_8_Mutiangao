from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("normal Taxi", 100), SilverServiceTaxi("SilverServiceTaxi",100,2)]
now_taxi = None
choice_taxis = []
bill = 0
print("Let's Drive!")

while choice_taxis is None:
    user_choice = input("q)uit, c)hoose taxi, d)rive")
    print('Bill to date:${:.2f}'.format(bill))
    print("Invalid option")
    user_choice = input("q)uit, c)hoose taxi, d)rive")

    if user_choice == 'c':
        count = 0
        for taxi in taxis:
            print('{} -- {}'.format(count, taxi))
        try:
            taxi_choice = int(input("Choose taxi:"))
            if taxi_choice > len(taxis):
                print("invalid taxi choice")

        except ValueError:
            print("invalid taxi choice")

    elif user_choice == 'd':
        drive_distance = input('drive how far:')
        taxis[0].drive(drive_distance)
        travel_cost = taxis[0].get_fare_number()
        bill = bill + travel_cost
        print('your trip cost you ${:.2f}'.format(taxis[0]))