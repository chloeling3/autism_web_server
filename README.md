# A web-based integrated machine learning framework for autism spectrum disorder prediction 

Chloe Ling (MSc.), Bin Lin (MSc., PharmD.), Avner Schlessingler (phD). 

Department of Pharmacological Sciences, Icahn School of Medicine at Mount Sinai, New York, US. 

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

#### Target Variable 

Risk score calculation for autism quantified through the receiver operator curve statistic. 

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

<img width="484" alt="Screen Shot 2020-05-21 at 10 34 41 AM" src="https://user-images.githubusercontent.com/31297724/82570601-d1a20780-9b4f-11ea-9cb4-f8d4b6ce059b.png">

Receiver Operator Curve of Logistic Regression model on top 20 features (deployed this model to the web server) 

<img width="266" alt="Screen Shot 2020-05-21 at 10 43 26 AM" src="https://user-images.githubusercontent.com/31297724/82570777-0910b400-9b50-11ea-8f84-20275ec967e4.png">

Classifier Performance Metrics after 10 Cross fold Validation 

<img width="431" alt="Screen Shot 2020-05-21 at 10 43 42 AM" src="https://user-images.githubusercontent.com/31297724/82570854-25145580-9b50-11ea-8982-9463bd4660cc.png">

<img width="441" alt="Screen Shot 2020-05-21 at 10 45 30 AM" src="https://user-images.githubusercontent.com/31297724/82570922-3fe6ca00-9b50-11ea-9048-922e2478895a.png">


## Feature Selection 

A comparison of feature selection methods ran on optimized Logistic Regression classifier. We extracted 4 different methods: 
• Filter Method (ANOVA) 
• Recursive Feature Elimination (RFE) 
• Feature Importance (Wrapper method) 
• Lasso Regression 

** Selected Recursive feature elimination(Wrapper Method) as the method to select top drug performers for autism classification. 

<img width="543" alt="Screen Shot 2020-05-21 at 10 47 34 AM" src="https://user-images.githubusercontent.com/31297724/82571146-8b00dd00-9b50-11ea-99d9-227682c7ae09.png">

## Results 

By fine-tuning its parameters through recursive feature elimination, we were able to achieve the following metrics: 

Logistic regression classifier accuracy (training set): 0.750
Logistic regression classifier accuracy (test set): 0.959

Logistic Regression Mean ROC AUC (Training Set): 0.726 (+/- 0.043)
Logistic Regression Mean ROC AUC (Testing Set): 0.678

We were also able to conclude on the 20 most important features (medications) used for prediction analysis.

Fitting estimator with 21 features.
['missing_p', 'count_drugs_scaled.y', 'C07A.x', 'C07F.x', 'C08D.x', 'M09A.x', 'V04C.x', 'H01C.x', 'B02B.y', 'C01C.y', 'S02D.y', 'C01B.y', 'S01F.y', 'C05B.y', 'N04B.y', 'V04C.y', 'H01A.y', 'A03C.y', 'G03A.y', 'C01A.y']

## Deploying the model onto the web 

The optimized model was deployed onto the web utilizing Python Flask. 

<img width="908" alt="form page" src="https://user-images.githubusercontent.com/31297724/82571448-f8147280-9b50-11ea-8d66-ff6707a6d0ec.png">




#### Notes 

This research was supported by the following institutions: 
Department of Pharmacological Sciences, Icahn School of Medicine at Mount Sinai, New York, US. 
Department of Community Mental Health University of Haifa, Haifa, Israel 
Department of Psychiatry, Icahn School of Medicine at Mount Sinai, New York, US 
Department of Environmental Medicine and Public Health, Icahn School of Medicine at Mount Sinai, New York, US 

