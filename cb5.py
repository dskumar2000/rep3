import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Web scraping
@st.cache_data(show_spinner="Scraping website...")
def scrape_website(url):
    try:
        resp = requests.get(url, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")
        texts = [
            el.get_text(separator=" ", strip=True)
            for el in soup.find_all(['p', 'li', 'h1', 'h2', 'h3'])
        ]
        return "\n".join(texts)
    except Exception as e:
        return ""

st.title("Harriss Consultancy: Web Q&A (RAG Demo)")

if not openai_api_key:
    st.error("Please set your OPENAI_API_KEY in a .env file or environment variable.")
    st.stop()

if st.button("Scrape & Index Website"):
    with st.spinner("Scraping and indexing content..."):
        content = scrape_website("https://harrissces.com/")
        if not content:
            st.error("Failed to scrape website.")
        else:
            splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
            chunks = splitter.split_text(content)
            embeddings = OpenAIEmbeddings(api_key=openai_api_key)
            vector_store = FAISS.from_texts(chunks, embeddings)
            retriever = vector_store.as_retriever(search_kwargs={"k": 4})
            llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o", temperature=0.2)
            qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
            st.session_state["qa_chain"] = qa_chain
            st.success(f"Website indexed in {len(chunks)} chunks.")

if "qa_chain" in st.session_state:
    query = st.text_input("Ask a question about harrissces.com:")
    if query:
        with st.spinner("Generating answer..."):
            answer = st.session_state["qa_chain"].run(query)
            st.subheader("Answer from Website")
            st.write(answer)
else:
    st.info("Click the 'Scrape & Index Website' button to begin.")

