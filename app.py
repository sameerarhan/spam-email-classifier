import streamlit as st
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model and vectorizer using joblib
spam_classifier = joblib.load('spam_classifier.pkl')
tfidf_vectorizer = joblib.load('tfidf_transformer.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Streamlit app
def main():
    st.title("Spam Email Classifier")
    email_text = st.text_area("Enter the email text:")

    if st.button("Classify"):
        # Preprocess the email text
        email_text_processed = [email_text]

        email_vec = vectorizer.transform(email_text_processed)
        email_tfidf = tfidf_vectorizer.transform(email_vec)

        # Make predictions
        prediction = spam_classifier.predict(email_tfidf)

        if prediction[0] == 0:
            st.success("The email is classified as Not Spam.")
        else:
            st.error("The email is classified as Spam.")

if __name__ == "__main__":
    main()
