from collections import Counter
from shared_resources.preprocess_text import preprocess_text

def get_word_count_analysis_result(text):
    """
    Counts the occurrences of each word in the text.

    Args:
        text (str): The input text.

    Returns:
        A dictionary where the keys are words and the values are the number of occurrences of each word in the text.
    """
    # get tokenized text from the input 
    words = preprocess_text(text)

    # Count the occurrences of each word
    word_counts = dict(Counter(words))
    
    # Return the dictionary of word counts
    return dict(sorted(word_counts.items(), key=lambda x:x[1], reverse=True))
