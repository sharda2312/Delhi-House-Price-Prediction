# Delhi House Price Prediction

This repository contains a machine learning model developed to predict house prices of different locations of Delhi, India. The model utilizes various regression algorithms, including Linear Regression, Decision Tree, and Lasso Regression, to accurately estimate house prices based on input features.

## Project Summary

1. **Data Cleaning and Preprocessing:** The dataset(Containing the dataset with 8k rows of data features.) was cleaned and preprocessed. This involved handling missing values, encoding categorical variables, and scaling numerical features.
2. **Feature Engineering:** Outliers were identified and removed to prevent them from skewing the model's predictions.
3. **Model Training:** Multiple regression models were trained using the preprocessed data. This included experimenting with different algorithms and techniques to find the most suitable model for the task.
4. **Hyperparameter Tuning:** Grid Search Cross-Validation (CV) was employed to fine-tune the hyperparameters of the selected models. This process helped optimize the models' performance and generalization ability.
5. **Deployment on AWS:** The final model was deployed on Amazon Web Services (AWS) EC2. A FastAPI server was integrated with the deployed model to handle prediction requests efficiently.

## Repository Structure

### Model
1. **7K-delhi:** Contains the dataset with 8k rows of data features.
2. **columns.json:** JSON file containing the column names used for data preprocessing.
3. **delhi_house_price_prediction.joblib:** Serialized machine learning model file.
4. **delhi_house_price_prediction.ipynb:** Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.

### Server folder 
1. **columns.json:** JSON file containing the column names used for data preprocessing.
2. **delhi_house_price_prediction.joblib:** Serialized machine learning model file.
3. **app.py:** FastAPI server code for handling prediction requests.
4. **requirements.txt:** File listing all required Python dependencies for running the project.

## Usage
To use the deployed model for house price prediction:

- Clone this repository to your local machine.
- Navigate to the server directory.
- Install the required Python dependencies listed in requirements.txt.
- Start the FastAPI server by running **uvicorn main:app --host 0.0.0.0 --port 8000** in the terminal.
- Send HTTP POST requests to the /get-me-data endpoint with to send data with input features.
      **json format post request example**

        {
        "location": "ahinsa khand 2, ghaziabad, delhi ncr",
        "area": 1500,
        "bath": 3,
        "bed": 2,
        "parking": true,
        "type": false
        }

- **columns.json** contains all the locations accepted by model.

- after sending the post request Send HTTP GET request to the /prediction endpoint to get predicted value as output.