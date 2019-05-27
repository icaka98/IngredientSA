import re
import pandas as pd

from unidecode import unidecode

f = open("../data/bg_data.txt","r")
contents = f.read()


x = re.sub("\(.*?\)|<p>|<br/>|</p>", "", str(contents))
print(x)
arr = x.split("\n")

dishes = {}
name = ""
for i in range(0, len(arr)):
    #empty string
    if arr[i] == '':
        continue

    if "to taste" in arr[i]:
        continue

    #check if it's a dish name
    if arr[i][0].isupper():
        name = arr[i]
        dishes[name] = []
        continue
    else:
        #remove stop words
        ingredient = re.sub(
            ",.*|[0-9]|/|\.|big|medium|clove|glove|bunch|gallon|can|cup|ml|tbsp|tablespoon|teaspoon|-|lb|long|fresh|pinch|of|pack|tsp|sprinkle|cleaned|and|some|chopped|spoonful|half",
            "", arr[i])
        ingredient = re.sub("\A\s*", "", ingredient)
        ingredient = re.sub("^s |^ful |^a ", "", ingredient)

        dishes[name].append(ingredient.strip())


df = pd.DataFrame(columns=['Name', 'Rating', 'Ingredients'])

i = 0
for name in dishes:
    length = len(dishes[name])

    for j in range(0, length):
        #print(j)
        dishes[name][j] = unidecode(dishes[name][j])
    df.loc[i] = [name] + ["0.0"] + [', '.join(dishes[name])]

    i+=1


export_csv = df.to_csv (r'../data/balkan_recipes.csv', index = None, header=True)

print (df)
