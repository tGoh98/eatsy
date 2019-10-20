# *Me.nu*

*eatsy is a regression model that models what preferences are important to individual users and extrapolates this data to recommend a restaurant that satisfies the preferences for a group of users. It takes into account reviews on other online platforms and user-specific preferences and past experiences to find the perfect restaurant for everyone.* 

## Features
* Models with all the data in Yelp's open dataset that holds information on 200,000 businesses, over 6 million reviews, and 1.6 million users
* Implements machine learning techniques to predict the importance of certain preferences to a user
* Combines the importance of preferences of every user in a group optimally
* Uses a logistic regression model to calculate a score for each restaurant given a group of users
* Selects the top five restaurants that produce the highest scores for the group of users

## Menu Item Rating Algorithm 
We wrote this algorithm for our program to rate each dish from the menu input. It factors in the average rating, a correction factor for other reviewers' perceptions of the dish as positive or negative, as well as the tendency of better items to typically have more reviews overall. 
![Menu Item Rating Algorithm](https://github.com/michaelsprintson/me.nu/blob/master/hr9%20equation.PNG)

## How to run
1. Setup [Google Cloud Vision API](https://cloud.google.com/vision/docs/before-you-begin) for your project to enable optical character recognition (OCR) for menu scanning.
    1a. put the Google Vision Service Account Key in a file called <code>apikey.json</code> inside of the <code>menu_read</code> directory 
2. Setup [Google Cloud Maps Places API](https://developers.google.com/places/web-service/intro) to enable google review scraping
   2a. *please put the Google Maps API key in a file called <code>gmapsapikey.json</code> inside of the <code>menu_parse</code> directory
3. Install neccesary dependencies with ```pip install -r requirements.txt```
4. Start the server with ```python3 app.py```

## Team
eatsy was created by Michael Sprintson (michaelsprintson), Timothy Goh (tGoh98), Sanghyeon Lee (SangHyeonLee), and Yong Shin (yowashi23) for TAMU Datathon. Read more about it in the [Devpost](https://devpost.com/software/eatsy)..

![eatsy Logo](https://github.com/tGoh98/eatsy/static/images/logo.png)
