# Football results prediction:

This was a project i did for the subject INF161 at UIB. The goal of the project was to predict the results of football matches given the results from the previous year.
There is also basic web frontend where you can choose different teams and see how they will perform against each other 

### Libraries used:
* [Pandas](https://pandas.pydata.org/) For cleaning and managing data
* [Scikit-learn](https://scikit-learn.org/stable/) For machine learning models and workflow
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) For a simple frontend to interact with the model

### results:
* The best model i found was an Elastic net model.
  * This model got 1.19430 RMSE on [the final kaggle test](https://www.kaggle.com/competitions/inf161-innforing-i-data-science-2021/leaderboard).
  * This gave me the top score out of all the students in the contest. 
