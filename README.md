# Cat vs Dog Classifier

This project is a **Cat vs Dog Image Classifier** built using TensorFlow and Streamlit. It allows users to upload images of cats or dogs, and the model predicts which category the image belongs to. The app is built using Streamlit for the user interface and TensorFlow for the machine learning model.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To run this project locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/coder021/cat-dog-classifier.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install TensorFlow (if not in `requirements.txt`):
    ```bash
    pip install tensorflow
    ```

4. Run the app:
    ```bash
    streamlit run cat.py
    ```

Your app will be live on `localhost:8501`.

## Usage

1. Go to the **Streamlit app** URL (if deployed on Streamlit Cloud) or `localhost:8501` (if running locally).
2. Upload an image of a cat or dog.
3. The model will classify the image as either a **cat** or a **dog** and display the result.
4. View the confidence score of the classification.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- TensorFlow for providing the tools to build machine learning models.
- Streamlit for providing the easy-to-use interface for deploying apps.
