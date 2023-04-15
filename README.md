# text_analysis_services
Microservices platform for multiple text analysis services

# multiple_text_analysis_services
Microservices platform for multiple text analysis services

## Services

1. **Bigram Analysis Service:** Identifies the most frequently occurring pairs of words (bigrams) in the text.
2. **Word Count Analysis Service:** Counts the occurrences of each word in the text.

## Example Usage:

### Request:

POST /analyze-text

{   
  "service": "bigram",    
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."   
}

### Response:

HTTP 200 OK

{   
  "result": [    ["quick", "brown"],    
    ["brown", "fox"],    
    ["fox", "jumps"],    
    ["jumps", "over"],    
    ["over", "the"],   
    ["the", "lazy"],    
    ["lazy", "dog"],    
    ["the", "quick"],    
    ["dog", "again"],    
    ["again", "and"]    
  ]    
}

### Request:

POST /analyze-text

{ 
  "service": "word-count",    
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."     
}

### Response:

HTTP 200 OK

{    
  "result": {    
    "the": 4,    
    "quick": 2,    
    "brown": 2,    
    "fox": 2,    
    "jumps": 2,    
    "over": 2,    
    "lazy": 2,    
    "dog": 2,    
    "again": 2,    
    "and": 1    
  }    
}

### To run the app
 $`python3 app.py`

### To run tests
 $`python3 -m unittest discover tests`