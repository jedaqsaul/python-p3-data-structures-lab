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
   names=[]
   for food in spicy_foods:
       names.append(food['name'])
   return names
print(get_names(spicy_foods))




def get_spiciest_foods(spicy_foods):
   result=[]
  
   for food in spicy_foods:
       if food["heat_level"]>5:
          
         result.append(food)
   return result

print(get_spiciest_foods(spicy_foods))
print('xxxxxxxxxxxxxxxxxxxxx')


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

print('tihoiheoihiehfioehfoiehfiehfiohefioehfohefoihefohe')
print(get_spicy_food_by_cuisine(spicy_foods, 'American'))
print(get_spicy_food_by_cuisine(spicy_foods, 'Thai'))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total=0
    for food in spicy_foods:
      total+= food['heat_level']
    return total // len(spicy_foods)
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, {
   'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}))
