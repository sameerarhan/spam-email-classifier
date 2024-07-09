import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model and vectorizer
with open('spam_classifier.pkl', 'rb') as f:
    spam_classifier = pickle.load(f)

with open('tfidf_transformer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit app
def main():
    st.title("Spam Email Classifier")
    email_text = st.text_area("Enter the email text:")

    if st.button("Classify"):
        # Preprocess the email text
        email_text_processed = [email_text]

        email_vec = vectorizer.transform(email_text_processed)
        email_tfidf = tfidf_vectorizer.transform(email_vec)

        email_tfidf = email_tfidf.reshape(1, -1)
        
        # Make predictions
        prediction = spam_classifier.predict(email_tfidf)

        if prediction[0] == 0:
            st.success("The email is classified as Not Spam.")
        else:
            st.error("The email is classified as Spam.")

if __name__ == "__main__":
    main()
