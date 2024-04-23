# Delhi House Price Prediction

This repository contains a machine learning model developed to predict house prices in Delhi, India. The model utilizes various regression algorithms, including Linear Regression, Decision Tree, and Lasso Regression, to accurately estimate house prices based on input features.

## Project Summary

**Data Cleaning and Preprocessing:** The dataset was cleaned and preprocessed. This involved handling missing values, encoding categorical variables, and scaling numerical features.
**Feature Engineering:** Outliers were identified and removed to prevent them from skewing the model's predictions.
**Model Training:** Multiple regression models were trained using the preprocessed data. This included experimenting with different algorithms and techniques to find the most suitable model for the task.
**Hyperparameter Tuning:** Grid Search Cross-Validation (CV) was employed to fine-tune the hyperparameters of the selected models. This process helped optimize the models' performance and generalization ability.
**Deployment on AWS:** The final model was deployed on Amazon Web Services (AWS) EC2. A FastAPI server was integrated with the deployed model to handle prediction requests efficiently.

## Repository Structure

### Model
**7K-delhi:** Contains the dataset with 8k rows of data features.
**columns.json:** JSON file containing the column names used for data preprocessing.
**delhi_house_price_prediction.joblib:** Serialized machine learning model file.
**delhi_house_price_prediction.ipynb:** Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.

### Server folder 
**README.md:** Provides an overview of the project, its objectives, and key achievements.
**columns.json:** JSON file containing the column names used for data preprocessing.
**delhi_house_price_prediction.joblib:** Serialized machine learning model file.
**app.py:** FastAPI server code for handling prediction requests.
**requirements.txt:** File listing all required Python dependencies for running the project.

## Usage
To use the deployed model for house price prediction:

Clone this repository to your local machine.
Navigate to the server directory.
Install the required Python dependencies listed in requirements.txt.
Start the FastAPI server by running **uvicorn main:app --host 0.0.0.0 --port 8000** in the terminal.
Send HTTP POST requests to the /get-me-data endpoint with input data in the specified format to receive predictions.