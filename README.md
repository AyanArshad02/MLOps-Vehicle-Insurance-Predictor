# Vehicle Insurance Prediction - ML and MLOps

This project demonstrates a complete **Machine Learning (ML)** pipeline and **MLOps** workflow designed to predict whether a vehicle will purchase insurance based on certain vehicle-related attributes. The model is built, trained, and deployed using industry-standard MLOps practices, and the prediction service is exposed via a simple web interface.

## Highlights

- **End-to-End Machine Learning Pipeline**: From data preprocessing to model training and deployment, this project covers the entire ML workflow.
- **MLOps Practices**: The project follows best practices in **MLOps** to manage the lifecycle of machine learning models, from training to deployment, ensuring seamless integration with a web interface.
- **Prediction Service**: The trained model is served via a FastAPI-based web service to make real-time predictions using the deployed model.

## Technology Stack

- **Machine Learning Framework**: Scikit-learn for model training and evaluation.
- **Pipeline Management**: The project includes well-defined pipelines for data processing, model training, and model prediction.
- **MLOps**: Docker for containerization, FastAPI for model serving, and clear separation between training and serving.
- **Backend Framework**: FastAPI (used only to expose the model via API for real-time predictions).
- **Web Server**: Uvicorn (ASGI server for FastAPI).

## Problem Overview

In this project, we predict whether a vehicle is likely to purchase insurance based on its details. The features considered for prediction include:

- Gender, Age, Driving License status, and other vehicle attributes.
- Historical data about vehicle damage and insurance status.

## Features

- **Model Training**: The app allows for retraining of the prediction model based on updated data.
- **Prediction API**: After training, users can submit their vehicle data through a form to get predictions about the likelihood of purchasing insurance.
- **Model Deployment**: The trained model is deployed using FastAPI to serve predictions in real time.

## ML and MLOps Flow

### 1. Data Collection and Preprocessing

- The data is collected and preprocessed, ensuring it is cleaned and ready for training.
- Missing values are handled, and features are transformed to be suitable for machine learning algorithms.

### 2. Model Training Pipeline

- A **scikit-learn** model is trained using the preprocessed data.
- **Model Evaluation**: Various machine learning evaluation techniques are applied to ensure the model’s performance is robust and accurate.
- The pipeline can be triggered from the `/train` endpoint, which will initiate the retraining process.

### 3. Model Prediction

- After the model is trained, the `/` endpoint accepts user input, runs it through the model, and returns a prediction of whether the vehicle is likely to purchase insurance.
- The prediction pipeline is seamlessly integrated with FastAPI to expose the model as a web service.

### 4. MLOps Deployment

- The trained model and the FastAPI service are packaged and deployed using Docker.
- The Docker container ensures consistency across environments and simplifies deployment.
- **Continuous Integration/Continuous Deployment (CI/CD)**: This project could be extended with CI/CD pipelines to automate model retraining, validation, and deployment processes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AyanArshad02/MLOps-Vehicle-Insurance-Predictor.git
   cd MLOps-Vehicle-Insurance-Predictor
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. To run the application locally:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

4. Alternatively, you can run the app in a Docker container:
   ```bash
   docker build -t vehicle-insurance-prediction .
   docker run -p 8000:8000 vehicle-insurance-predictio
   ```

5. Access the application: Open your browser and go to http://localhost:8000

## Endpoints

### 1. `/train` (GET)
- **GET**: Initiates the model retraining process using the latest data. This endpoint is responsible for running the model training pipeline.

### 2. `/` (GET & POST)
- **GET**: Displays the main form where users input vehicle data.
- **POST**: Submits the form data for prediction and returns the result, either `Response-Yes` or `Response-No`, based on the model’s output.

## Project Structure

- `app.py`: FastAPI app that exposes the model for prediction and triggers training.
- `src/constants.py`: Configuration constants such as host and port for the app.
- `src/pipeline`: Contains data preprocessing, model training, and prediction pipeline.
- `templates`: HTML templates for rendering the user interface.
- `static`: Static files like CSS for the frontend interface.

## MLOps Features

### Model Training Pipeline
- The model training pipeline automates the process of training the machine learning model with preprocessed data. After training, the model is serialized and saved for serving predictions.

### Model Serving (via FastAPI)
- FastAPI is used to serve the model and provide a user interface for data input. It connects directly with the trained model to return predictions without needing to reload or retrain.

### Dockerization
- The application, along with the model, is containerized using Docker to ensure easy deployment and scalability. This eliminates the "works on my machine" issue and allows for deployment across different environments.

