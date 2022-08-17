import random

destination_options = ['Tokyo', 'Berlin', 'Paris', 'Brussels', 'Barcelona', 'Dublin', 'Seoul']
restaurant_options = ['local food restaurant', 'high end restaurant', 'convinience store', 'café', 'food truck', 'tavern']
transportation_options = ['train', 'bus', 'bicycle', 'subway', 'car rental', 'taxi']
entertaiment_options = ['museums', 'theater', 'markets', 'concerts', 'picnic']

def get_random_selection(list_of_options, string_output, result_text):
    confirmation = 'n'
    while confirmation == 'n':
        selected_choice = random.choice(list_of_options)
        confirmation = input(f'{string_output} {selected_choice}? y/n ')
    print(f'{result_text} {selected_choice}')
    return selected_choice


def final_day_trip(destination, restaurant, transportation, entertaiment):
    confirmation = 'n'
    while confirmation == 'n':
        confirmation = input('Would you like to complete your day trip? y/n: ')
        if confirmation != 'n':
            break
        ask_for_update = input('Type which option would you like to change? destination/restaurant/transportation/entertaiment: ')
        if ask_for_update == 'destination':
            destination = get_random_selection(destination_options, 'Would you like the destination of', 'Your destination is')
        elif ask_for_update == 'restaurant':
            restaurant = get_random_selection(restaurant_options, 'Would you like to eat at', 'Your foodie match is')
        elif ask_for_update == 'transportation':
            transportation = get_random_selection(transportation_options, 'Would you like to move through the city in', 'Your transportation mode is')
        elif ask_for_update == 'entertaiment':
            entertaiment = get_random_selection(entertaiment_options, 'Would you like to go to', 'Enjoy your time in the')
    result = f'Your next trip will be in {destination}, you can enjoy the city via {transportation} and going to {entertaiment}. When feeling hungry you can go to a {restaurant}.'
    print(result)

my_destination = get_random_selection(destination_options, 'Would you like the destination of', 'Your destination is')

my_restaurant = get_random_selection(restaurant_options, 'Would you like to eat at', 'Your foodie match is')

my_transportation = get_random_selection(transportation_options, 'Would you like to move through the city in', 'Your transportation mode is')

my_entertaiment = get_random_selection(entertaiment_options, 'Would you like to go to', 'Enjoy your time in the')

final_day_trip(my_destination, my_restaurant, my_transportation, my_entertaiment)