from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

llm.client.headers = {"Authorization": f"Bearer {hf_token}"}


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
    human_template_str = "{user_prompt}"

    prompt = PromptTemplate.from_template(template.format(system_prompt = sys_template_str,
                                                          user_prompt = human_template_str,
                                                          history = "Considere o histórico recente de conversas: {history}"))
    

    print(prompt)

    session = prompt | llm 
    resposta = session.invoke({"user_prompt" : user_prompt,
                               "history" : history})

    return resposta