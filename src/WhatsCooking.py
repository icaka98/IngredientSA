import json
from matplotlib import pyplot as plt
import pandas as pd


with open('../data/train.json', 'r') as f:
    train = json.load(f)

with open('../data/test.json', 'r') as f:
    test = json.load(f)

all_dishes = {}
for dish in train:
    id = dish['id']
    all_dishes[id] = dish['ingredients']


for dish in test:
    id = dish['id']
    all_dishes[id] = dish['ingredients']

#deleting a file
filename = "../data/whatscooking.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")

f.close()

###Plotting distribution of ingredients
train_df = pd.read_json('../data/train.json')
plt.hist(train_df['ingredients'].str.len(),bins=max(train_df['ingredients'].str.len()),color='g', edgecolor = 'black')
plt.gcf().set_size_inches(12,8)
plt.ylabel("count of recipes")
plt.xlabel("number of ingredients")
plt.title('Ingredients in a Dish Distribution')
plt.show()


def cleanbrackets(param):
    if "(" in param:
        start = param.index("(")
        end = param.index(")")
        to_be_removed = param[start:end + 1]
        param = param.replace(to_be_removed , '')

    return param


with open('../data/whatscooking.csv','a') as fd:

    fd.write("Name,Rating,Ingredients\n")
    i = 0
    for id in all_dishes:
        #check for 1 ingredient
        if len(all_dishes[id]) < 2:
            continue
        i+=1
        ingredients_str = "\""

        ingredients_str += cleanbrackets(all_dishes[id][0])
        for j in range(1, len(all_dishes[id])):
            ingredients_str += ", " + cleanbrackets(all_dishes[id][j])

        csvRow = str(id) + ",0.0," + ingredients_str + "\"" + "\n"
        fd.write(csvRow)

print(i)
