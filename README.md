# 🌾 AgriSmart: Crop Recommendation System

An Intelligent Machine Learning web application that recommends the most suitable crops to farmers based on soil and environmental parameters.

## 🚀 Live Demo
https://crop-prediction-ml-predict-your-crop.streamlit.app/

## 🛠️ Tech Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Data Handling:** Pandas, Numpy
- **Web Interface:** Streamlit
- **Deployment:** GitHub & Streamlit Cloud

## 📊 Features
- **High Accuracy:** Achieved **99.3% accuracy** on the test dataset.
- **Confidence Metrics:** Shows the probability score for each prediction.
- **Visual Analysis:** Displays a Bar Chart of the Top 5 recommended crops.
- **Dynamic UI:** Includes real-time image previews of recommended crops.
- **Error Handling:** Notifies users if environmental inputs are extreme or unrealistic.

## 📂 Project Structure
- `app.py`: Training script for the ML model.
- `web.py`: Streamlit frontend dashboard.
- `crop_model.pkl`: Serialized model file.
- `requirements.txt`: List of dependencies.
