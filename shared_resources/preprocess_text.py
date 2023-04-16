import re
import contractions

def preprocess_text(text:str)->list[str]:
    """
    Performs text preprocessing

    Args:
        text (str): The input text.

    Returns:
        A list of tokens (words)
    """
    # Remove contractions
    text = contractions.fix(text)   

    # Convert text to lowercase and remove all non-alphanumeric characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

    # Split text into words
    words = text.split()

    return words
