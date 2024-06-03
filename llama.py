from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm_name = os.getenv("LLM_NAME")

llm = LlamaCpp(model_path=f"models/{llm_name}", 
               max_tokens=None,
               n_ctx=512,
               stop=["<|eot_id|>"],
               verbose=False)


template = """
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        {system_prompt}
        <|eot_id|>
        <|start_header_id|>user<|end_header_id|>
        {user_prompt}
        <|eot_id|>
        <|start_header_id|>system<|end_header_id|>
        {history}
        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        """

def get_response(user_prompt, history):
    sys_template_str = "Você é um assistente virtual especializado em design de código. Responda a pergunta do usuário em no máximo 2 sentencas."

    prompt = PromptTemplate.from_template(template.format(system_prompt = sys_template_str,
                                                          user_prompt = "{user_prompt}",
                                                          history = "Considere o histórico recente de conversas: {history}"))
    

    print(prompt)

    session = prompt | llm 
    resposta = session.invoke({"user_prompt" : user_prompt,
                               "history" : history})

    return resposta