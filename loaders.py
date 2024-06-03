from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("https://arxiv.org/pdf/2210.07342")
docs = loader.load()

docs_in_str = [doc.page_content for doc in docs]

print(docs_in_str)

from llama import get_response

r = get_response("quais são os benefícios do CDD? considere esse texto como base: {docs_in_str}", None)

print(r)
import sys; sys.exit(0)


from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode([docs_in_str])
print(embeddings[0][0:5])
# [3, 384]


from retriever import _store
_store(docs_in_str[0], embeddings[0])