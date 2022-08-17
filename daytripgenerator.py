import random

destination_options = ['Tokyo', 'Berlin', 'Paris', 'Brussels', 'Barcelona', 'Dublin', 'Seoul']
restaurant_options = ['local food restaurant', 'high end restaurant', 'convinience store', 'café', 'food truck', 'tavern']
transportation_options = ['train', 'bus', 'bicycle', 'subway', 'car rental', 'taxi']
entertaiment_options = ['museums', 'theater', 'markets', 'concerts', 'picnic']

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
print(f'Your destination is {my_destination}')

my_restaurant = restaurants(restaurant_options)
print(f'You may enjoy eating at a {my_restaurant}')

my_transportation = transportation(transportation_options)
print(f'Transportation mode in the city is {my_transportation}')

my_entertaiment = entertaiment(entertaiment_options)
print(f'Enjoy your time {my_entertaiment}')


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

print(f'Your next trip will be in {my_destination}, you can enjoy the city via {my_transportation} and going to {my_entertaiment}. When feeling hungry you can go to a {my_restaurant}')