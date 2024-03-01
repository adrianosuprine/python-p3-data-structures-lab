spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food ['name'] for food  in spicy_foods ]
    return names
get_names(spicy_foods)



def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food  in spicy_foods if food['heat_level'] >= 5 ]
    return spiciest_foods
get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods :
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_bycuisine = [food for food in spicy_foods if food["cuisine"] == cuisine][0]
    return spicy_food_bycuisine
get_spicy_food_by_cuisine(spicy_foods,"American")



def print_spiciest_foods(spicy_foods):
    for food in spicy_foods :
          if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    total_heat = 0 
    for food in spicy_foods :
        heat = food["heat_level"]
        total_heat += heat
        average_heat = total_heat / len(spicy_foods)
    return average_heat
            

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods 
create_spicy_food(spicy_foods, {"name":"Tujo","cuisine":"European","heat_level": 7})