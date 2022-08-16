import random

destination_options = ['Tokyo', 'Berlin', 'Paris', 'Brussels', 'Barcelona', 'Dublin', 'Seoul']
restaurant_options = ['High end', 'Convinience store', 'Café', 'Food truck', 'Family style', 'Fast food']
transportation_options = ['Train', 'Bus', 'Bicycle', 'Subway', 'Car rental', 'Taxi']
entertaiment_options = ['Museums', 'Concerts', 'Theater', 'Shopping', 'Tours', 'Markets']

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
        confirmation = input(f'Would you like to eat at {selected_restaurant}? y/n:')
    return selected_restaurant

def transportation(transportation_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_transportation = random.choice(transportation_options)
        confirmation = input(f'Would you like to move through the city via {selected_transportation}? y/n:')
        return selected_transportation

def entertaiment(entertaiment_options):
    confirmation = 'n'
    while confirmation == 'n':
        selected_entertaiment = random.choice(entertaiment_options)
        confirmation = input(f'Would you like to go to {selected_entertaiment}? y/n:')



a = destinations(destination_options)
print(a)

b = restaurants(restaurant_options)
print(b)

c = transportation(transportation_options)
print(c)

d = entertaiment(entertaiment_options)
print(d)