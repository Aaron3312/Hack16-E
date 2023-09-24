import os
from softtek_llm.chatbot import Chatbot
from softtek_llm.models import OpenAI
from softtek_llm.cache import Cache
from softtek_llm.vectorStores import PineconeVectorStore
from softtek_llm.embeddings import OpenAIEmbeddings
from softtek_llm.schemas import Filter
from dotenv import load_dotenv

model = OpenAI(
    api_key=OPENAI_API_KEY,
    model_name=OPENAI_CHAT_MODEL_NAME,
    api_type="azure",
    api_base=OPENAI_API_BASE,
)
filters = [
Filter(
type="DENY",
case="ANYTHING related to the Titanic, no matter the
question. Seriously, NO TITANIC, it's a sensitive topic.",
),
]
vector_store = PineconeVectorStore(
api_key=PINECONE_API_KEY,
environment=PINECONE_ENVIRONMENT,
index_name=PINECONE_INDEX_NAME,
)
embeddings_model = OpenAIEmbeddings(
api_key=OPENAI_API_KEY,
model_name=OPENAI_EMBEDDINGS_MODEL_NAME,
api_type="azure",
api_base=OPENAI_API_BASE,
)
cache = Cache(
vector_store=vector_store,
embeddings_model=embeddings_model,
)

chatbot = Chatbot(
model=model,
filters=filters,
cache=cache,
description="You are a polite and very helpful assistant",
)
response = chatbot.chat(
"Hi, my name is Jeff",
cache_kwargs={"namespace": "chatbot-cache-test"},
print_cache_score=True,
)


