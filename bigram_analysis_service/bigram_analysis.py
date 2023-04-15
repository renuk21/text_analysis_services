from collections import Counter
from shared_resources.preprocess_text import preprocess_text


def get_bigram_analysis_result(text):
    """
    Identifies the most frequently occurring pairs of words (bigrams) in the text.

    Args:
        text (str): The input text.

    Returns:
        A list of the most frequently occurring bigrams in the text, sorted in descending order by frequency.
    """
    # get tokenized text from the input 
    words = preprocess_text(text)

    # Create list of bigrams
    bigrams = [tuple(words[i:i+2]) for i in range(len(words) - 1)]
   
    # Count the occurrences of each bigram
    bigram_counts = dict(Counter(bigrams).most_common(10))

    # sort the bigrams by frequency
    sorted_bigrams = dict(sorted(bigram_counts.items(), key=lambda x:x[1], reverse=True))
    
    # isolate the bigrams from the dictionary
    bigrams_list = [list(bigram) for bigram,freq in sorted_bigrams.items()]

    # Return the list of most common bigrams
    return bigrams_list