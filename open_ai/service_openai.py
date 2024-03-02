from openai import OpenAI
from open_ai_variables import openai_model

client = OpenAI()

def get_genereated_response(messages,user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model= openai_model,
        messages=messages
    )
    message = response.choices[0].message.content.strip()
    # message = f"Respone from Open AI {user_input}" #temp
    messages.append({"role": "system", "content": message})
    return message,messages