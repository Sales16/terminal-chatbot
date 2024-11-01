# Terminal Chatbot com Groq e Llama3

Este projeto é um chatbot de terminal que utiliza a API do Groq para eficiência e o modelo Llama3 para processamento de linguagem natural. O chatbot responde exclusivamente em português e utiliza um prompt padrão para guiar as respostas.

## Descrição

O chatbot responde a perguntas e interações no terminal, processando respostas em português com o modelo de linguagem Llama3. Com suporte da API do Groq para otimização e eficiência, o chatbot é ideal para interações simples e rápidos testes de inteligência artificial.

## Requisitos

- Chave de API do Groq
- Bibliotecas Python:
    - groq
    - langchain

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/terminal-chatbot.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd terminal-chatbot
    ```
3. Instale as dependências:
    ```bash
    pip install groq langchain
    ```

## Configuração da API

Para conseguir a chave da API, siga os passos abaixo para configurar:

1. Acesse o [console da Groq](https://console.groq.com/keys).
2. Faça login na sua conta.
3. Vá até a seção API Keys (chaves de API).
4. Crie uma nova chave, copie o valor gerado e cole no 

``` bash 
api_key = "SUA_CHAVE_API_AQUI"
````

## Uso

Execute o script principal:
```bash
python chatbot.py
```
