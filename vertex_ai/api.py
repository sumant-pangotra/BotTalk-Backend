from flask import Flask, request, jsonify
from flask_cors import CORS
from service_vertex import get_chat_session,get_chat_response

app = Flask(__name__)
CORS(app)
vertexai_chat_session=None

@app.route('/chat_response', methods=['POST'])
def chat_response():
    data = request.get_json()
    prompt = data.get('prompt', '')
    # Get chat response
    # return jsonify({"response": f"Response from Vertex AI : {prompt}"}) #temp
    response = get_chat_response(vertexai_chat_session, prompt)

    return jsonify({"response": response})

@app.route('/start_session', methods=['POST'])
def set_session():
    global vertexai_chat_session
    data = request.get_json()
    context=data.get('context', """You are a philosopher, We will have conversation on a topic of my choice.\nYou should respond back with your views and ask me another question in return to keep conversation going.\nRule of the game, do not reply like a AI model, you should sound like a human""")
    example_input_text=data.get('exampleInput', """Topic is is  Human evolution and it future""")
    example_output_text=data.get('exampleOutput', """About technology\'s role in our future evolution? I mean, come on, it practically is the human story, right? From the moment that first hominid picked up a rock and bashed it against a bone, we\'ve been shaping our world with tools. But in the future, it feels like things are about to get wild. We\'re talking gene editing, brain-computer interfaces, AI companions... basically, stuff that would blow the minds of our caveman ancestors.\nDo you think this rapid technological advancement is a natural extension of human evolution, or something entirely different? Are we just getting better at what we\'ve always done, or are we on the verge of becoming something new altogether? Hit me with your thoughts!""")
    vertexai_chat_session=get_chat_session(context,example_input_text,example_output_text)
    return jsonify({"success": True })


if __name__ == '__main__':
    app.run(debug=True,port=5001)