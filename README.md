# Autism Classifier 

## Overview 

This project is 2-fold. We first apply multiple machine learning algorithms to predict for autism spectrum disorder using prenatal drug exposures. 
Then, we deploy an optimized web-based integrative machine learning framework for predicting risk to autism spectrum disorder using prenatal drug exposures. 

## Run 

In a terminal or command window, navigate to the top-level project directory autism_web_server/. Then change directories into flaskr (where __init__.py 
file is stored) and run the following commands: 

FLASK_APP = __init__.py 

flask run 


## Dataset 

The modified dataset is EMR data taken through a large health maintenance organization in Israel (Meuhedet). The Meuhedet cohort used in this study includes EMR data 
on children born in Israel from January 1, 1997 through December 31, 2007, and their parents. Children were followed up for ASD diagnosis from birth to January 26, 2015. The 
analytic sample consisted of 1,397 ASD cases across 1,207 father-mother pairs and 94,741 controls across 34,913 mother-father pairs. 

#### Features 

162 features were selected as predictors to train models. These features included prescription and medication use, and medical histories (eg. number of medical contacts), sociodemographic 
characteristics (age, socioeconomic status). Prescription medications were represented by ATC Drug Codes, produced by the World Health Organization. 

## Models 

The three models that seem appropriate for the specific problem and will be evaluated are:

• Logistic Regression
• Gaussian Naive Bayes
• Support Vector Machines 
• Multilayer Perceptron 
• Random Forest 
• Extra Trees 
• K Nearest Neighbors 
• AdaBoost 
• Gradient Boost 

After evaluating their performance, we concluded that Logistic Regression is the most appropriate model. 

Below are Overall Receiver Operator Curves for all features (after 10 cross fold validation). 
![image!](file:///Users/chloeling3/Desktop/Screen%20Shot%202020-05-21%20at%2010.34.41%20AM.png)





## Feature Selection 


## Results 

By fine-tuning its parameters through recursive feature elimination, we were able to achieve:

Accuracy Score: 
Precision: 




We were also able to conclude on the five most important features.

#### Notes 
