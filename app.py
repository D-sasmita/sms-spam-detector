import streamlit as st
import pickle

# Page setup
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

# Load model and vectorizer
@st.cache_resource
def load_artifacts():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_artifacts()

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
with st.sidebar:
    st.header("About")
    st.write(
        "This app classifies SMS text as Spam or Not Spam using a "
        "trained Naive Bayes model with TF-IDF features."
    )
    st.divider()
    st.subheader("Try an example")
    example_spam = "Congratulations! You have won a cash prize of ₹50,000. Claim now!"
    example_ham = "Hey, are we still meeting at 6pm today?"

    if st.button("Load spam example", use_container_width=True):
        st.session_state.message_input = example_spam
    if st.button("Load normal example", use_container_width=True):
        st.session_state.message_input = example_ham

    st.divider()
    if st.session_state.history:
        if st.button("Clear history", use_container_width=True):
            st.session_state.history = []

# Main content
st.title("📩 SMS Spam Detector")
st.caption("Paste any SMS text below to check if it's spam.")

message = st.text_area(
    "Enter your SMS",
    height=120,
    key="message_input",
    placeholder="Type or paste a message here..."
)

col1, col2 = st.columns([1, 3])
with col1:
    predict_clicked = st.button("Predict", type="primary", use_container_width=True)

if predict_clicked:
    if message.strip():
        transformed_text = vectorizer.transform([message])
        prediction = model.predict(transformed_text)[0]

        # Confidence score, if the model supports it
        confidence = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(transformed_text)[0]
            confidence = proba[prediction] * 100

        label = "Spam" if prediction == 1 else "Not Spam"
        st.session_state.history.insert(0, (message, label, confidence))

        if prediction == 1:
            st.error(f"🚫 **Spam**" + (f" — {confidence:.1f}% confidence" if confidence else ""))
        else:
            st.success(f"✅ **Not Spam**" + (f" — {confidence:.1f}% confidence" if confidence else ""))
    else:
        st.warning("Please enter an SMS.")

# History
if st.session_state.history:
    st.divider()
    st.subheader("Recent checks")
    for msg, label, conf in st.session_state.history[:5]:
        icon = "🚫" if label == "Spam" else "✅"
        conf_text = f" ({conf:.1f}%)" if conf else ""
        with st.expander(f"{icon} {label}{conf_text} — {msg[:50]}{'...' if len(msg) > 50 else ''}"):
            st.write(msg)