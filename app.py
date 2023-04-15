from flask import Flask, request, jsonify
from bigram_analysis_service import bigram_analysis 
from word_count_analysis_service import word_count_analysis

app = Flask(__name__)
app.config['app.json.sort_keys'] = False

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    data = request.json

    service = data.get('service')
    text = data.get('text')

    if not service:
        return jsonify({'error': 'Service name is missing.'}), 400

    if not text:
        return jsonify({'error': 'Text is missing.'}), 400

    if service == 'bigram':
        result = bigram_analysis.get_bigram_analysis_result(text)
    elif service == 'word-count':
        result = word_count_analysis.get_word_count_analysis_result(text)
    else:
        return jsonify({'error': f'Service "{service}" not found.'}), 400

    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run()
