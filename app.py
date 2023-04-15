from flask import Flask, request, jsonify
from app_config import SERVICES

app = Flask(__name__)
app.config['app.json.sort_keys'] = False

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    data = request.json

    service_name = data.get('service')
    text = data.get('text')

    if not service_name:
        return jsonify({'error': 'Service name is missing.'}), 400

    if not text:
        return jsonify({'error': 'Text is missing.'}), 400

    if service_name in SERVICES:
        function = SERVICES[service_name]
        result = function(text)
    else:
        return jsonify({'error': f'Service "{service_name}" not found.'}), 400

    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run()
