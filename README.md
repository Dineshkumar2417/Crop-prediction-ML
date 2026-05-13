# 🌾 AgriSmart: Precision Agriculture Assistant

AgriSmart ek intelligent Machine Learning application hai jo soil data aur weather conditions ko analyze karke kisaano ko batata hai ki kaunsi fasal (crop) unke liye sabse behtar hogi.

## 🚀 Live Demo
Aap is project ka live version yahan dekh sakte hain:
👉 [**AgriSmart Live App**](https://crop-prediction-ml-predict-your-crop.streamlit.app/)

## 📊 Key Features
- **High Accuracy:** Random Forest Classifier ka use karke **99.3% accuracy** achieve ki gayi hai.
- **Confidence Metrics:** Har prediction ke saath model ka confidence score dikhaya gaya hai.
- **Top 5 Analysis:** Agar confidence kam ho, toh model top 5 alternative options bhi dikhata hai.
- **Visual Previews:** Recommended crop ki image real-time mein load hoti hai.
- **Reliable Warnings:** Galat input (jaise 100% se zyada humidity) par system alert deta hai.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib
- **Web UI:** Streamlit
- **Version Control:** Git & GitHub

## 📂 Project Structure
- `web.py`: Streamlit dashboard ka frontend code.
- `app.py`: Model training aur data processing script.
- `crop_model.pkl`: Saved ML model file.
- `requirements.txt`: Deployment ke liye zaroori libraries ki list.

## ⚙️ How to Run Locally
1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run web.py`
