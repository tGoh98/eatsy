# *Eatsy*

*Eatsy is a regression model that models what preferences are important to individual users and extrapolates this data to recommend a restaurant that satisfies the preferences for a group of users. It takes into account reviews on other online platforms and user-specific preferences and past experiences to find the perfect restaurant for everyone.* 

## Features
* Models with all the data in Yelp's open dataset that holds information on 200,000 businesses, over 6 million reviews, and 1.6 million users
* Implements machine learning techniques to predict the importance of certain preferences to a user
* Combines the importance of preferences of every user in a group optimally
* Uses a logistic regression model to calculate a score for each restaurant given a group of users
* Selects the top five restaurants that produce the highest scores for the group of users

## To run:
1. Install dependencies with ```pip install -r requirements.txt```
2. Start the server with ```python main.py```
3. The server should now be running at ```localhost:5000```

## Team
eatsy was created by Michael Sprintson ([michaelsprintson](https://github.com/michaelsprintson)), Timothy Goh ([tGoh98](https://github.com/tgoh98)), Sanghyeon Lee ([SangHyeonLee](https://github.com/sanghyeonlee)), and Yong Shin ([yowashi23](https://github.com/yowashi23)) for [TAMU Datathon 2019](https://tamudatathon.com). Read more about it in the [Devpost](https://devpost.com/software/eatsy).
