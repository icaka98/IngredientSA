import json
import pandas as pd
import numpy
from unidecode import unidecode
import matplotlib.pyplot as plt

with open('../data/full_format_recipes.json', 'r') as f:
    recipe_dict = json.load(f)

dictionary = {}

recipe_dict = filter(None, recipe_dict)
all_ingredients = []
ratings = {}

#extract the only the needed info form the dataset
i = 0
for recipe in recipe_dict:
    if recipe['rating'] == None:
        continue

    title = recipe['title']

    if title in dictionary.keys():
        title = title + " " + str(i)


    dictionary[title] = recipe['categories']
    all_ingredients += recipe['categories']

    ratings[title] = recipe['rating']
    #print(recipe['categories'])
    i+=1

#create distribution
histogram_values = {}
total = 0
for title in ratings:
    rating = ratings[title]

    if rating == 0:
        continue

    if rating not in histogram_values.keys():
        histogram_values[rating] = 0

    histogram_values[rating] += 1
    total += 1

labels = []
for key in histogram_values.keys():
    labels.append(str(key))
#print(histogram_values)
plt.xlabel("ratings")
plt.ylabel("count")
plt.bar(histogram_values.keys(), histogram_values.values(), 0.5, color='g', tick_label = labels)
#plt.show()

for rating in histogram_values:
    histogram_values[rating] /= total
    print(str(rating) + " " + str(histogram_values[rating]))

rating_keys = list(histogram_values.keys())
frequencies = list(histogram_values.values())

for title in ratings:
    if ratings[title] == 0:
        ratings[title] = numpy.random.choice(rating_keys, p = frequencies)

#sorting out the duplicates
all_ingredients = list(dict.fromkeys(all_ingredients))
for ingr in all_ingredients:
    print(ingr)
#all_ingredients.sort()


non_ingredients = ["Sauté","Sandwich", "Fruit", "Vegetable", "Kid-Friendly", "Cookie", "Food Processor", "Bake", "Bastille Day","New Year's Eve", "Dried Fruit", "Winter", "Chill", "Bon Appétit" , "Soup/Stew", "Dairy", "Gourmet", "New York", "Low Fat", "Low Cal","High Fiber", "Dinner", "Healthy", "Simmer", "Pescatarian", "Dairy Free", "Peanut Free", "Tree Nut Free", "Soy Free",  "Side","Vegetarian", "Quick & Easy", "Fall", "California", "Summer", "Salad", "Easter", "Spring", "Boil", "Wheat/Gluten-Free", "No Sugar Added","No-Cook", "Cocktail Party", "Stir-Fry", "Picnic", "Lunch", "Sugar Conscious", "Thanksgiving", "Breakfast", "Cake", "Dessert","Tropical Fruit", "Party", "Birthday", "Low Carb", "Father's Day", "Massachusetts", "Sauce", "Brunch", "Christmas","Mother's Day", "New Year's Day", "Jam or Jelly", "Kidney Friendly", "Braise", "Capers", "Self", "Low Sodium", "Leafy Green""Family Reunion", "Super Bowl", "Shower", "Condiment/Spread", "Fry", "Pan-Fry", "Herb", "Advance Prep Required", "Paleo","Spice", "Blender", "Roast", "Vegan", "Back to School", "Poker/Game Night", "Australia", "Casserole/Gratin", "Deep-Fry","Grill", "Grill/Barbecue", "Alcoholic", "Cocktail", "Drink", "Backyard BBQ", "Freeze/Chill", "Appetizer", "Oscars", "Christmas Eve","Engagement Party", "Potluck", "Cilantro", "Mixer", "One-Pot Meal", "HarperCollins", "Quick and Healthy", "Santa Monica", "Fourth of July","Cornmeal", "Microwave", "Salad Dressing", "Double Boiler", "Valentine's Day", "Anniversary", "Poultry", "Low/No Sugar", "Meat", "Kansas","Condiment", "Portland", "Oregon", "Frozen Dessert", "Lunar New Year", "Fat Free", "Non-Alcoholic", "St. Patrick's Day", "Punch", "30 Days of Groceries","Root Vegetable", "Oktoberfest", "Sour Cream", "Seafood", "Wedding", "Shavuot", "Steam", "Low Cholesterol", "Ice Cream Machine","Kentucky Derby", "Passover", "Kosher for Passover", "House & Garden", "Spirit", "Wok", "Whole Wheat", "Buffet", "Marinate", "Date","22-Minute Meals", "Halloween", "Ramadan", "Seattle", "Washington", "Parade", "Friendsgiving", "Low Sugar", "Weelicious","Candy Thermometer", "Pittsburgh", "Pennsylvania", "Dallas", "Texas", "Aperitif", "Cookies", "Florida", "Margarita", "Wisconsin", "Hot Drink","Raw", "Washington, D.C.", "Spain", "Monterey Jack", "cookbooks", "Macaroni and Cheese", "Edible Gift", "Ireland", "Michigan","No Meat, No Problem", "San Francisco", "Game", "snack", "snack week", "Pressure Cooker", "Los Angeles", "Connecticut", "House Cocktail","Labor Day", "Flaming Hot Summer", "Cook Like a Diner", "Omelet", "Denver", "Ohio", "Mexico", "Organic", "Utah", "Slow Cooker", "North Carolina","Freezer Food", "Entertaining", "South Carolina", "Rhode Island", "Stock", "Drinks", "Pie", "Minnesota", "Buffalo", "Missouri", "Brooklyn","Chicago", "Illinois", "#CAKEWEEK", "New Mexico", "Sandwich Theory", "Hollywood", "New Jersey", "Dip", "Persian New Year", "3-Ingredient Recipes","Indiana", "New Orleans", "Louisiana", "Kitchen Olympics", "Tennessee", "Flat Bread", "Canada", "Pot Pie", "Chile", "Columbus", "Boston","Italy", "Haiti", "Japan", "Virginia", "Yonkers", "Maryland"]
categories = all_ingredients[568:]
non_ingredients += categories
print(len(non_ingredients))

#remove the non-ingredient categories from the list with ingredients
for name in dictionary:
    to_remove = []
    for ingr in dictionary[name]:
        if ingr in non_ingredients:
            to_remove.append(ingr)
    for removable in to_remove:
        dictionary[name].remove(removable)
    #print(dictionary[name])

df = pd.DataFrame(columns=['Name', 'Rating', 'Ingredients'])

i = 0
for name in dictionary:
    leng = len(dictionary[name])

    # remove recipies with 1 or 0 ingredients
    if leng < 2:
        continue

    for j in range(0, leng):
        #print(j)
        dictionary[name][j] = unidecode(dictionary[name][j])
    df.loc[i] = [name] + [str(ratings[name])] + [', '.join(dictionary[name])]

    i+=1


export_csv = df.to_csv (r'../data/epirecipes.csv', index = None, header=True)

print (df)