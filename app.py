import streamlit as st
from menu_lookup import MenuRetriever
from agent import generate_dish_explanation_rag

st.set_page_config(page_title="Menu Agent", page_icon="🍝")

st.title("🍝 Menu Agent")
st.write("Enter an Italian dish name, and I'll explain it to you!")

retriever = MenuRetriever("menu_data.csv")

dish_input = st.text_input("Dish name (in Italian):", placeholder="e.g. Spaghetti alla Carbonara")

if st.button("Explain") and dish_input:
    with st.spinner("Retrieving and generating..."):
        context_docs = retriever.retrieve(dish_input)
        if context_docs:
            explanation = generate_dish_explanation_rag(dish_input, context_docs)
            st.success("✅ Retrieved and generated!")
            st.markdown(explanation)
        else:
            st.warning("⚠️ No similar dish found.")
