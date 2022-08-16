import random

destination_options = ['Tokyo', 'Berlin', 'Paris', 'Brussels', 'Barcelona', 'Dublin', 'Seoul']
restaurant_options = ['High end', 'Convinience store', 'Café', 'Food truck', 'Fast food']
transportation_options = ['Train', 'Bus', 'Bicycle', 'Subway', 'Car rental', 'Taxi']
entertaiment_options = ['Museums', 'Theater', 'Markets', 'Concerts', 'Picnic']

def destinations(destination_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_destination = random.choice(destination_options)
        confirmation = input(f'Would you like to visit {selected_destination}? y/n: ')
    return selected_destination

def restaurants(restaurant_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_restaurant = random.choice(restaurant_options)
        confirmation = input(f'Would you like to eat at {selected_restaurant}? y/n: ')
    return selected_restaurant

def transportation(transportation_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_transportation = random.choice(transportation_options)
        confirmation = input(f'Would you like to move through the city via {selected_transportation}? y/n: ')
    return selected_transportation

def entertaiment(entertaiment_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_entertaiment = random.choice(entertaiment_options)
        confirmation = input(f'Would you like to go to {selected_entertaiment}? y/n: ')
    return selected_entertaiment


my_destination = destinations(destination_options)
print(my_destination)

my_restaurant = restaurants(restaurant_options)
print(my_restaurant)

my_transportation = transportation(transportation_options)
print(my_transportation)

my_entertaiment = entertaiment(entertaiment_options)
print(my_entertaiment)


confirmation = 'n'
while confirmation == 'n':
    confirmation = input('Would you like to complete your day trip? y/n: ')
    if confirmation != 'n':
        break
    ask_for_update = input('Type which option would you like to change? destination/restaurant/transportation/entertaiment: ')
    if ask_for_update == 'destination':
        my_destination = destinations(destination_options)
    elif ask_for_update == 'restaurant':
        my_restaurant = restaurants(restaurant_options)
    elif ask_for_update == 'transportation':
        my_transportation = transportation(transportation_options)
    elif ask_for_update == 'entertaiment':
        my_entertaiment = entertaiment(entertaiment_options)

print(my_destination, my_restaurant, my_transportation, my_entertaiment)