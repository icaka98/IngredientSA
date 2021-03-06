<h1 align='center'>
  Sentiment Analysis on Ingredients 
  <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Markdownify" width='120'>
  </a>
</h1>

![Ingredients](images/Ingredients.jpg "Ingredients")

## Novel Idea
Often people find themselves in a situation when they wonder if adding a certain component to a meal will improve or worsen its taste. This problem leads to the question of whether a specific ingredient combination tastes delicious or disgusting. This research scrapes and brings together several datasets about various recipes from  worldwide cuisines. Each recipe has a list of ingredients. The goal of this paper is to create a model that can evaluate correctly the tastiness of the ingredient combination. Thus, we call th idea Sentiment Analysis on Ingredients. Imagine people using ingredients to express opinions:

<h3 align='center'>I absolutely loved the movie! It was beef, rice and vinegar!</h3>
<h3 align='center'>This movie is cactus, frog legs and dark chocolate!</h3>

</br>

<h4 align='center'>What would happen if you put tzatziki into your orange juice when you don't have tzaziki in your vocabulary?</h4>

</br>
</br>

<p align='center'>
<img src="images/orange.jpg" alt="drawing" width="100" height="100"/> <img src="images/plus.png" alt="drawing" width="100" height="100"/> <img src="images/tz.jpg" alt="drawing" width="100" height="100"/> <img src="images/equal.png" alt="drawing" width="100" height="100"/> <img src="images/sick.svg" alt="drawing" width="100" height="100"/>
</p>

</br>

<p align='center'>
<img src="images/tz.jpg" alt="drawing" width="100" height="100"/> <img src="images/plus.png" alt="drawing" width="100" height="100"/> <img src="images/garlic.png" alt="drawing" width="100" height="100"/> <img src="images/equal.png" alt="drawing" width="100" height="100"/> <img src="images/happy.svg" alt="drawing" width="100" height="100"/>
</p>

## Data
We gathered data from various sources (Kaggle datasets, scraping), so that it represents as many cuisine specific ingredients as possible.

Another issue was negative examples generation (aim for balanced dataset).
We created recipes with random ingredients sampled from over 8000 different types with a specific length distribution.

One lovely negative recipe worth mentioning:

cactus, nonfat buttermilk, soybean sprouts, nectarines, northern beans, banana, ton skins, black pepper, english cucumber, oyster mushrooms, tomato sauce, frogs legs, spam

## Models
This research implements four models which reach the following results: 

![Model](images/bow.PNG "BoW model")
![Model](images/tfidf.PNG "Tf-idf model")
![Model](images/w2v.PNG "Word2vec model")
![Model](images/w2vt.PNG "Word2vec Tf-idf model")

## Research Future
Our research can find further use in the following areas:
1. <b>Food recommendation systems</b>
2. <b>Recipe generation systems</b>
3. <b>Food industry awareness</b>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact
Hristo Minkov - minkov.h@gmail.com

Zhecho Mitev - zhecho15@yahoo.com

Codebase Link: [https://github.com/icaka98/IngredientSA](https://github.com/icaka98/IngredientSA)
