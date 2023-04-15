import re
import contractions

def preprocess_text(text):
    # Remove contractions
    text = contractions.fix(text)   

    # Convert text to lowercase and remove all non-alphanumeric characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

    # Split text into words
    words = text.split()

    return words
