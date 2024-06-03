from llama import get_response

history = []

while True:
    user_input = input("> Digite sua pergunta: ")
    history.append(user_input)
    resposta = get_response(user_input, history)
    history.append(resposta)
    print(f"> {resposta} \n")