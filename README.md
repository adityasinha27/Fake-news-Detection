# Fake News Detection System

This project is a machine learning-based Fake News Detection system that classifies news articles as "Real" or "Fake." The system uses Natural Language Processing (NLP) techniques along with a machine learning model to identify the credibility of a news article.

### Prerequisites

Before running the project, make sure to have the following installed:
- Python 3.6 or higher
- pip (Python package installer)

#!/bin/bash

# Clone the repository (skip if already cloned)
echo "Cloning the repository..."
# git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection || exit

# Create a virtual environment (optional but recommended)
echo "Setting up virtual environment..."
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # For Linux/macOS
# venv\Scripts\activate  # For Windows (uncomment this line for Windows)

# Install required dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Prepare the Dataset (Ensure the dataset file news.csv is available)
echo "Preparing the dataset..."
# Preprocess data script should be added if it exists
# python preprocess_data.py

# Train the model (Ensure that the training script is available)
echo "Training the model..."
# Assuming Fake News Detection.ipynb is used for training, not a Python script
# You can either run Jupyter Notebook commands or a Python script here:
jupyter nbconvert --to script "Fake News Detection.ipynb"

# Now train the model using the converted script (adjust paths and code as necessary)
python fake_news_detection_script.py

# Evaluate the model (This can also be done through a script if you have a separate evaluation script)
echo "Evaluating the model..."
# python evaluate_model.py  # Adjust if you have a separate evaluation script

# Run the Flask app (Ensure the app.py is available)
echo "Starting the Flask app..."
python app.py
