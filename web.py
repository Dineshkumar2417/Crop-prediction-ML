import streamlit as st
import pickle
import pandas as pd
import numpy as np

# 1. Page Config (Browser tab par icon aur naam ke liye)
st.set_page_config(page_title="AgriSmart - Crop Predictor", page_icon="🌱", layout="wide")

# 2. Custom CSS (Button aur Layout ko sundar banane ke liye)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Load
model = pickle.load(open('crop_model.pkl', 'rb'))

# --- SIDEBAR (Inputs yahan shift kar diye hain) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2917/2917995.png", width=100)
st.sidebar.title("Parameters")
st.sidebar.markdown("Mitti aur Mausam ki jankari yahan bharein:")

N = st.sidebar.number_input("Nitrogen (N)", min_value=0, value=50)
P = st.sidebar.number_input("Phosphorus (P)", min_value=0, value=50)
K = st.sidebar.number_input("Potassium (K)", min_value=0, value=50)
temp = st.sidebar.number_input("Temperature (°C)", value=25.0)
humidity = st.sidebar.number_input("Humidity (%)", value=50.0)
pH = st.sidebar.number_input("pH Level (0-14)", value=7.0)
rain = st.sidebar.number_input("Rainfall (mm)", value=100.0)

button = st.sidebar.button("Predict Best Crop")

# --- MAIN PAGE ---
st.title('🌾 AgriSmart: Precision Farming')
st.markdown("---")

if button:
    # Prediction Logic
    features = np.array([[N, P, K, temp, humidity, pH, rain]])
    prediction = model.predict(features)
    final_crop = prediction[0].lower()
    
    # Confidence Score nikalna
    proba = model.predict_proba(features)
    confidence = np.max(proba) * 100

    # Layout Columns for Result
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Result")
        st.success(f"### The Best Crop is: **{final_crop.upper()}**")
        st.metric(label="Prediction Confidence", value=f"{confidence:.2f}%")
        
        if confidence < 60:
            st.warning("⚠️ **Low Confidence Alert**: The model is not highly certain about this recommendation. This usually happens when input values are extreme or unusual (like the Humidity 200% in your case!). Please double-check your inputs or consider the alternatives in the chart.")
        else:
            st.info("✅ **Reliable Prediction**: The environmental conditions strongly align with the requirements for this crop.")

        st.info("Based on the provided parameters, this crop has the highest probability of a successful harvest.")

    with col2:
        # Images Dictionary
        crop_images = {
            "rice": "https://images.unsplash.com/photo-1586201375761-83865001e31c",
            "maize": "https://images.unsplash.com/photo-1551754655-cd27e38d2076",
            "chickpea": "https://images.unsplash.com/photo-1515544832961-292431dfd20a",
            "kidneybeans": "https://images.unsplash.com/photo-1585914924626-45adbc930e1b",
            "pigeonpeas": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec",
            "mothbeans": "https://images.unsplash.com/photo-1514333860578-831e5f8f85f5",
            "mungbean": "https://images.unsplash.com/photo-1543325064-0a3733027b4b",
            "blackgram": "https://images.unsplash.com/photo-1626082896492-766af4eb6501",
            "lentil": "https://images.unsplash.com/photo-1545114197-0098f98ec893",
            "pomegranate": "https://images.unsplash.com/photo-1615485240388-349f5068962c",
            "banana": "https://images.unsplash.com/photo-1603833665858-e61d17a86224",
            "mango": "https://images.unsplash.com/photo-1553279768-865429fa0078",
            "grapes": "https://images.unsplash.com/photo-1533616688419-b7a585564566",
            "watermelon": "https://images.unsplash.com/photo-1587049633562-ad3672b77492",
            "muskmelon": "https://images.unsplash.com/photo-1571151605030-949169677332",
            "apple": "https://images.unsplash.com/photo-1560806887-1e4cd0b6bcd6",
            "orange": "https://images.unsplash.com/photo-1547514701-42782101795e",
            "papaya": "https://images.unsplash.com/photo-1517282003759-f9ba326884a4",
            "coconut": "https://images.unsplash.com/photo-1559181567-c3190ca9959b",
            "cotton": "https://images.unsplash.com/photo-1594132176008-0917d5964033",
            "jute": "https://images.unsplash.com/photo-1626105374439-6880579e0001",
            "coffee": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
        }

        if final_crop in crop_images:
            st.image(crop_images[final_crop], caption=f"Beautiful {final_crop.upper()} field", use_container_width=True)

    # --- Chart ---
    st.divider()
    st.subheader("📊 Analysis of Top 5 Crop Candidates")
    
    crop_names = model.classes_
    prob_df = pd.DataFrame({
        "Crop": crop_names,
        "Probability": proba[0]
    })
    
    top5 = prob_df.sort_values(by="Probability", ascending=False).head(5)
    st.bar_chart(data=top5.set_index("Crop"))

else:
    # Home Screen jab tak button click nahi hota
    st.image("https://images.unsplash.com/photo-1464226184884-fa280b87c399", use_container_width=True)
    st.warning("👈 Please enter soil details in the sidebar and click Predict!")