from flask import Flask, request, Response, stream_with_context, jsonify

from ai_model import translate_zh_to_en, translate_en_to_zh, summarize_text

app = Flask(__name__)

@app.route('/translate/zh2en', methods=['POST'])
def zh2en():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = translate_zh_to_en(text)
    return Response(stream_with_context(generate(result)), content_type="text/event-stream")


@app.route('/translate/en2zh', methods=['POST'])
def en2zh():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = translate_en_to_zh(text)
    return Response(stream_with_context(generate(result)), content_type="text/event-stream")


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = summarize_text(text)
    return Response(stream_with_context(generate(result)), content_type="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True)
