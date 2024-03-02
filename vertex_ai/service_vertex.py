import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair, ChatSession
import logging
from vertex_ai_variables import *

logging.info(f"Initializing Vertex AI Client project={GCP_PROJECT_ID},location={GCP_LOCATION},Model={VERTEX_AI_MODEL}")

vertexai.init(project=GCP_PROJECT_ID, location=GCP_LOCATION)
chat_model = ChatModel.from_pretrained(VERTEX_AI_MODEL)
parameters = {
    "candidate_count": vertex_candidate_count,
    "max_output_tokens": vertex_max_output_tokens,
    "temperature": vertex_temperature,
    "top_p": vertex_top_p,
    "top_k": vertex_top_k
}

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    response = chat.send_message(prompt,**parameters)
    return response.text

def get_chat_session(context,example_input_text,example_output_text):
    chat = chat_model.start_chat(
    context=context,
    examples=[
        InputOutputTextPair(
            input_text=example_input_text,
            output_text=example_output_text
        )])
    return chat