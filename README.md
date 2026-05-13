# 🌾 AgriSmart: Precision Crop Recommendation System

AgriSmart is an end-to-end Machine Learning application designed to assist farmers in identifying the most suitable crops for their land based on soil composition and environmental factors.

## 🚀 Live Demo
Experience the live application here:
👉 [**AgriSmart Live App**](https://crop-prediction-ml-predict-your-crop.streamlit.app/)

## 📊 Key Highlights
- **High Precision:** Achieved an accuracy of **99.3%** using the **Random Forest Classifier** algorithm.
- **Interactive Dashboard:** Built a dynamic and responsive web interface using **Streamlit**.
- **Data-Driven Insights:** Analyzes Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.
- **Advanced Analytics:** Features a "Top 5 Crop Candidates" probability chart to provide alternative recommendations in low-confidence scenarios.
- **Visual Feedback:** Displays real-time images of the recommended crops for an enhanced user experience.

## 🛠️ Tech Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit Cloud & GitHub (CI/CD)

## 📂 Project Structure
- `web.py`: The main Streamlit application script.
- `app.py`: Logic for data preprocessing and model inference.
- `crop_model.pkl`: The trained and serialized machine learning model.
- `requirements.txt`: List of dependencies for a seamless cloud environment setup.

## ⚙️ Installation & Usage
1. Clone the repository: `git clone [YOUR_REPO_URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run web.py`
