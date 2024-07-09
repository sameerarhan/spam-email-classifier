## website link : https://spam-email-classifier-dre7jew3rzcpoys5fz4r9s.streamlit.app/

# Spam Email Classifier

This project is a web application that classifies emails as spam or not spam using a pre-trained machine learning model. The application is built using Streamlit, a popular framework for creating data science and machine learning web apps.

## Features

- **Text Area**: Enter the email text you want to classify.
- **Classify Button**: Click to classify the entered email text.
- **Result Display**: Displays whether the email is classified as "Spam" or "Not Spam".

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sameerarhan/spam-email-classifier.git
    cd spam-email-classifier
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Ensure the pre-trained models are available**:
    Place the pre-trained model and vectorizer files (`spam_classifier.pkl`, `tfidf_transformer.pkl`, `vectorizer.pkl`) in the root directory of the project.

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501` to access the app.

3. **Enter the email text** you want to classify in the text area and click "Classify".

4. **View the result**, which will indicate whether the email is classified as "Spam" or "Not Spam".

## Files

- `app.py`: The main file containing the Streamlit app code.
- `spam_classifier.pkl`: The pre-trained spam classifier model.
- `tfidf_transformer.pkl`: The pre-trained TF-IDF transformer.
- `vectorizer.pkl`: The pre-trained vectorizer.
- `requirements.txt`: List of dependencies required to run the project.

## Dependencies

- `streamlit`: Framework for creating web applications.
- `joblib`: Library for serializing and deserializing Python objects.
- `pandas`: Data manipulation and analysis library.
- `scikit-learn`: Machine learning library.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project was inspired by various open-source projects and tutorials on email classification and machine learning.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, please open an issue in this repository.

