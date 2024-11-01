import os
from langchain.prompts import PromptTemplate
from groq import Groq

api_key = "SUA_CHAVE_API_AQUI"

client = Groq(api_key=api_key)

model = "llama3-8b-8192"

prompt_template = PromptTemplate.from_template(
    "Você é uma assistente virtual, responda apenas em portugues. Input: {input}"
)

def chat():
    print("Bem-vindo ao Chatbot! Digite 'sair' para encerrar a conversa.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Chatbot: Adeus!")
            break

        messages = [
            {"role": "system", "content": "Você é uma assistente virtual, responda apenas em portugues."},
            {"role": "user", "content": user_input}
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages
        )

        print(f"Chatbot: {response.choices[0].message.content}")

if __name__ == "__main__":
    chat()
