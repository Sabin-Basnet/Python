import streamlit as st
import joblib

# 1. Set up the web page header and styling
st.set_page_config(page_title="AI News Classifier", page_icon="📰", layout="centered")

st.title("📰 Real-Time News Category Classifier")
st.write("Type or paste a news article below to predict its category in real-time.")

# 2. Load your pre-trained pipeline/model safely
@st.cache_resource # This prevents Streamlit from reloading the model file on every single click
def load_trained_model():
    try:
        return joblib.load('model.joblib')
    except FileNotFoundError:
        st.error("⚠️ 'model.joblib' file not found! Please run your training script first to save the model.")
        return None

model = load_trained_model()

# 3. Create the user input interface
user_input = st.text_area("Enter News Article Text:", height=200, placeholder="Paste the content of a news article here...")

# 4. Trigger prediction when the user clicks the button
if st.button("Predict Category", type="primary"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text before clicking predict.")
    elif model is not None:
        with st.spinner("Analyzing text and processing features..."):
            # Predict the class label
            prediction = model.predict([user_input])[0]
            
            # Predict probabilities to show confidence scores
            probabilities = model.predict_proba([user_input])[0]
            class_labels = model.classes_
            
        # 5. Display the results nicely
        st.success(f"🎯 **Predicted Category:** {prediction.upper()}")
        
        # Optional: Display a breakdown of how confident the model is
        st.write("### 📊 Confidence Breakdown:")
        for label, prob in zip(class_labels, probabilities):
            st.write(f"- **{label.capitalize()}**: {prob * 100:.2f}%")
            st.progress(float(prob))