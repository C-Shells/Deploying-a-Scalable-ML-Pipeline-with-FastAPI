# Model Card  

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf  

## Model Details  
Model type:  RandomForestClassifier through scikit-learn  
Version: 1.0  
Training Environment:  Python 3.13.9, scikit-Learn, FASTAPI  
Author:  Chelli Kluchesky - WGU D501 Project 2  
Hyperparameters:  n_estimators=100, max_depth=None, random_state=42  

## Intended Use  
The purpose of this model is to predict whether someone earns more or less than 50k annually.  
The intended users are the Udacity project reviewers.  

## Training Data  
The source is from the census data found at UC Irvine https://archive.ics.uci.edu/dataset/20/census+income

Size of the raw data is 32,561 rows with 15 categorical and continuous features.  
The features are:  age, workclass, fnlgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, salary  

## Evaluation Data  
Split: 80/20 training/testing split  
Processing:  OneHotEncoder for categorical features, LabelBinarizer for labels  


## Metrics
_Please include the metrics used and your model's performance on those metrics._  
Precision:  0.7419  
Recall:  0.6384  
F1:  0.6863  


## Ethical Considerations  
There is a risk of bias in the data since it is census data and reflects socioeconomic patterns.  Race, education, and sex may be biased.  
This data is from 1994 and would now be outdated for current decision making.


## Caveats and Recommendations
This model was trained using United States census data and may not work for global data.  
This model is used for educational purposes only through Udacity's ML DevOps class and was prepared by a student.

