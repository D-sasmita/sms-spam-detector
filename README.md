# sms-spam-classifier

A Streamlit web app that classifies SMS messages as spam or not spam using a TF-IDF vectorizer and a trained Naive Bayes model.

## Live demo

Add your Streamlit Cloud URL here once deployed: `https://your-app-name.streamlit.app`

## How it works

1. The app loads a pre-trained Multinomial Naive Bayes model and a TF-IDF vectorizer, both saved with pickle.
2. When you enter a message, the vectorizer converts it into numeric features based on word frequency.
3. The model predicts whether those features match spam or normal message patterns.
4. The app displays the result along with a confidence score.

## Model performance

The model was trained and evaluated on the SMS Spam Collection dataset.

| Metric | Score |
|---|---|
| Accuracy | 97.1% |
| Precision | 100% |

Precision was prioritized over accuracy during model selection, since misclassifying a real message as spam is worse than letting an occasional spam message through.

## Tech stack

- Python
- scikit-learn (TF-IDF, Multinomial Naive Bayes)
- Streamlit (web interface)
- NLTK (text preprocessing)

## Running locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/D-sasmita/sms-spam-detector.git
cd sms-spam-detector
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the local URL Streamlit prints in your terminal, usually `http://localhost:8501`.

## Project structure

```
spamguard/
├── app.py              # Streamlit app
├── model.pkl           # Trained Naive Bayes model
├── vectorizer.pkl      # Fitted TF-IDF vectorizer
├── requirements.txt    # Python dependencies
└── README.md
```

## Features

- Real-time spam classification with confidence score
- Example message buttons to quickly test the app
- History of recent checks within the session

## Future improvements

- Add more training data to improve generalization on short or ambiguous messages
- Try additional models (SVM, ensemble methods) and compare performance
- Add a feedback mechanism so users can flag misclassifications
