from langchain_community.vectorstores.faiss import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema.document import Document
import pandas as pd
import os

class MenuRetriever:
    def __init__(self, csv_path: str, index_dir="faiss_index"):
        self.df = pd.read_csv(csv_path)
        self.df['Italian'] = self.df['Italian'].str.strip().str.lower()

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )

        if os.path.exists(index_dir):
            self.vectorstore = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
        else:
            docs = [
                Document(
                    page_content=f"{row['Italian']}: {row['English']}",
                    metadata={"Italian": row['Italian']}
                )
                for _, row in self.df.iterrows()
            ]
            self.vectorstore = FAISS.from_documents(docs, embedding=embeddings)
            self.vectorstore.save_local(index_dir)

    def retrieve(self, query: str, top_k: int = 3):
        query = query.strip().lower()
        return self.vectorstore.similarity_search(query, k=top_k)
