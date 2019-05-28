<h1 align='center'>
  Sentiment Analysis on Ingredients 
  <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Markdownify" width='135'>
  </a>
</h1>

![Ingredients](Ingredients.jpg "Ingredients")

## Novel Idea
Often people find themselves in a situation when they wonder if adding a certain component to a meal will improve or worsen its taste. This problem leads to the question of whethera specific ingredient combination tastes delicious or disgusting. This research scrapes and brings together several datasets about various recipes from  worldwide cuisines. Each recipe has a list of ingredients. The goal of this paper is to create a model that can evaluate correctly the tastiness of the ingredient combination. Thus, we call th idea Sentiment Analysis on Ingredients. Imagine people using ingredients to express opinions:

<h3 align='center'>I absolutely loved the movie! It was beef, rice and vinegar!</h3>
<h3 align='center'>This movie is cactus, frog legs and dark chocolate!</h3>

## Data
We gathered data from various sources, so that it represents as many cuisine specific ingredients as possible.
What would happen if you put tzatziki into your orange juice when you don't have tzaziki in your vocabulary?

![Model](bow.PNG "BoW model")
![Model](tfidf.PNG "Tf-idf model")
![Model](w2v.PNG "Word2vec model")
![Model](w2vt.PNG "Word2vec Tf-idf model")

Another issue was negative examples generation (aim for balanced dataset).
We created recipes with random ingredients sampled from over 8000 different types with a specific length distribution.

One lovely negative recipe worth mentioning:

cactus, morcilla, nonfat buttermilk, soybean sprouts, nectarines, spaghetti, northern beans, black pepper, banana, ton skins, black pepper, pasta sauce, spray, english cucumber, oyster mushrooms, tomato sauce, frogs legs, spam

## Problem
The main problem was how to represent those lists of ingredients in order to best suit our task.

## Models
This research implements four models which reach the following results: 

<img src="juice.jpg" alt="drawing" width="50" height="50"/><img src="juice.jpg" alt="drawing" width="50" height="50"/>
<img src="juice.jpg" alt="drawing" width="50" height="50"/>
<img src="juice.jpg" alt="drawing" width="50" height="50"/>
<img src="juice.jpg" alt="drawing" width="50" height="50"/>

![Model](juice.jpg =50x20 "Orange")
![Model](plus.png =50x20 "Tf-idf model")
![Model](tz.jpg "Word2vec model")
![Model](equal.png "d")
![Model](sick.svg "d")


## Research Future
Our research can find further use in the following areas:
1. <b>Food recommendation systems</b>
2. <b>Recipe generation systems</b>
3. <b>Food industry awareness</b>
