# SMS Spam Classifier

A Streamlit web app that classifies SMS messages as **spam or not spam** using a **TF-IDF vectorizer** and a trained **Multinomial Naive Bayes** model.

## Live Demo

[**Try the SMS Spam Classifier →**](https://sms-spam-detector-cmifw8qt3scwrfeb2xackh.streamlit.app/)

## How It Works

1. The app loads a pre-trained **Multinomial Naive Bayes model** and a fitted **TF-IDF vectorizer**, both saved using Pickle.
2. When you enter an SMS message, the TF-IDF vectorizer converts the text into numerical features.
3. The trained Naive Bayes model uses these features to predict whether the message is **spam or not spam**.
4. The app displays the prediction along with a confidence score.

## Model Performance

The model was trained and evaluated on the **SMS Spam Collection dataset**.

| Metric | Score |
|---|---:|
| Accuracy | 97.1% |
| Precision | 100% |

Precision was prioritized over accuracy during model selection because misclassifying a legitimate message as spam is worse than allowing an occasional spam message through.

## Tech Stack

- **Python**
- **scikit-learn** — TF-IDF and Multinomial Naive Bayes
- **Streamlit** — Web interface and deployment
- **NLTK** — Text preprocessing
- **Pickle** — Model and vectorizer serialization

## Running Locally

Clone the repository:

```bash
git clone https://github.com/D-sasmita/sms-spam-detector.git
cd sms-spam-detector

Install the dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

Open the local URL displayed in your terminal, usually:
http://localhost:8501
 ```  
Project Structure
 ```  
sms-spam-detector/
├── app.py            #Streamlit application
├── model.pkl         
  # Trained Multinomial Naive Bayes model
├── vectorizer.pkl     
 # Fitted TF-IDF vectorizer
├── requirements.txt   
 # Python dependencies
└── README.md
 ```  
