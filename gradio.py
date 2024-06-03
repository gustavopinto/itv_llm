from llama import get_response
import main as gr


def ask_bot(message, history):
    return get_response(message)

chat = gr.ChatInterface(
        ask_bot,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Pergunte algo sobre para o SuperBot!", container=False, scale=7),
        title="SuperBot",
        description="Nosso SuperBot está pronto para atender suas perguntas!",
        theme="soft",
        cache_examples=True,
        retry_btn=None,
        undo_btn=None,
        submit_btn="Enviar",
        clear_btn="Limpar",
    )

chat.launch(share=True, server_name="0.0.0.0", server_port=7860)