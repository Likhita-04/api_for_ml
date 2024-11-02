
---

# Diabetes Prediction API

This project is a **Diabetes Prediction API** developed using **FastAPI**. The API receives input data regarding a patient's health metrics and predicts whether the patient is diabetic based on a pre-trained machine learning model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

## Overview

The Diabetes Prediction API uses a **machine learning model** to predict diabetes based on user input parameters like glucose levels, blood pressure, BMI, and age. This REST API allows developers to integrate diabetes prediction functionality into applications seamlessly.

## Features

- **Diabetes Prediction**: Accepts input data about the patient's health metrics and predicts the likelihood of diabetes.
- **CORS Middleware**: Enabled to allow cross-origin requests for flexible integration with frontend applications.
- **JSON Input and Output**: Accepts JSON input and provides a JSON response, making it easy to use with web and mobile applications.

## Technologies Used

- **FastAPI**: Framework for building the API.
- **Pydantic**: For data validation of input parameters.
- **pickle**: For loading the pre-trained machine learning model.
- **JSON**: For input data processing and output.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction-api.git
   ```

2. Change into the project directory:
   ```bash
   cd diabetes-prediction-api
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the saved model file (`diabetes_model.sav`) is present in the project directory.

5. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

## Usage

1. With the server running, make POST requests to the API endpoint to get diabetes predictions.
2. The API expects a JSON body with the following fields:
   - `Pregnancies` (int)
   - `Glucose` (int)
   - `BloodPressure` (int)
   - `SkinThickness` (int)
   - `Insulin` (int)
   - `BMI` (float)
   - `DiabetesPedigreeFunction` (float)
   - `Age` (int)

3. Example request (using `curl`):
   ```bash
   curl -X POST "http://127.0.0.1:8000/diabetes_prediction" -H "Content-Type: application/json" -d '{
       "Pregnancies": 2,
       "Glucose": 120,
       "BloodPressure": 70,
       "SkinThickness": 20,
       "Insulin": 85,
       "BMI": 28.1,
       "DiabetesPedigreeFunction": 0.627,
       "Age": 50
   }'
   ```

4. The API will return a message indicating whether the person is diabetic or not.

## Endpoints

- **`/diabetes_prediction`**: Accepts a POST request with JSON data of health metrics and returns a prediction.

## Future Enhancements

- Improve the accuracy of the prediction model by training on larger datasets.
- Add more endpoints to predict other health conditions.
- Integrate user authentication for secure access to the API.

## Acknowledgments

This project utilizes FastAPI for developing a lightweight and high-performance API, along with a pre-trained machine learning model to predict diabetes.

---
