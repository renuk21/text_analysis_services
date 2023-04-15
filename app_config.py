from bigram_analysis_service.bigram_analysis import get_bigram_analysis_result
from word_count_analysis_service.word_count_analysis import get_word_count_analysis_result

# Map of service names and corresponding functions to be called
SERVICES = {
    
    'bigram': get_bigram_analysis_result,
    'word-count': get_word_count_analysis_result

    # Add other services and functions here
}