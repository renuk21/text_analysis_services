from flask import Flask, request, jsonify
from app_config import SERVICES
import logging

app = Flask(__name__)
app.config['app.json.sort_keys'] = False

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    """
    Analyzes a piece of text using a specified service and returns the result.

    The input data should be provided in a JSON object in the request body, with the following fields:
    - 'service': A string indicating the name of the service to use.
    - 'text': A string containing the text to be analyzed.

    Returns a JSON object containing the result of the analysis, with a field named 'result'. The type and format
    of the result depends on the service being used.

    If the 'service' or 'text' field is missing from the request data, a JSON object with an 'error' field is returned
    with a 400 status code.

    If the specified service name is not found in the SERVICES dictionary, a JSON object with an 'error' field is returned
    with a 400 status code.

    If the specified text is not valid, a JSON object with an 'error' field is returned
    with a 400 status code.
    """
    data = request.json

    service_name = data.get('service')
    text = data.get('text')

    if not service_name:
        return jsonify({'error': 'Service name is missing.'}), 400

    if not text:
        return jsonify({'error': 'Text is missing.'}), 400

    if service_name in SERVICES:
        function = SERVICES[service_name]
        try:
            result = function(text)
        except Exception as e:
            logging.error('Error at %s', exc_info=e)
            return jsonify({'error': 'Invalid text! Only strings should be passed to the text input.'}), 400
    else:
        return jsonify({'error': f'Service "{service_name}" not found.'}), 400

    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run()
