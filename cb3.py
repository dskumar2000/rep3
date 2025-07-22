import streamlit as st
from PyPDF2 import PdfReader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize model and embeddings
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o", temperature=0.2)
embeddings = OpenAIEmbeddings()

st.title("DSK: PDF Reader and Q&A")

# PDF Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    raw_text = ""
    try:
        # Read and extract text from PDF
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {str(e)}")

    if not raw_text.strip():
        st.error("Could not extract any text from the uploaded PDF. "
                 "Please make sure the file is a valid PDF.")
    else:
        # Split extracted text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(raw_text)

        if not chunks:
            st.error("Could not split the text into chunks.")
        else:
            st.success(f"Loaded PDF into {len(chunks)} chunks.")
            # Create vector store
            vector_store = FAISS.from_texts(chunks, embeddings)
            retriever = vector_store.as_retriever(search_kwargs={"k": 5})

            # Build the retrieval QA chain
            qa = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=retriever
            )

            # Q&A interface
            query = st.text_input("Ask a question about the PDF:")
            if query:
                with st.spinner("Finding answer..."):
                    answer = qa.run(query)
                    st.subheader("Answer:")
                    st.write(answer)