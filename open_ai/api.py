from flask import Flask, request, jsonify
from flask_cors import CORS
from service_openai import get_genereated_response
from os import environ

app = Flask(__name__)
CORS(app)
@app.route('/generate_response', methods=['POST'])
def get_ai_respone():
    data = request.get_json()
    messages = data.get('history', [])
    user_input = data.get('input', '')
    message,history=get_genereated_response(messages,user_input)
    return jsonify({
        "message": message,
        "history": history
    })

if __name__ == '__main__':
    app.run(debug=True,port=int(environ.get("OPEN_AI_PORT","5000")))