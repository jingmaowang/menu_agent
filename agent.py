from openai import OpenAI
from langchain.prompts import PromptTemplate
from judgeval.tracer import Tracer, wrap


rag_prompt = PromptTemplate.from_template("""
You are a culinary expert. Given the Italian dish "{dish}", and the background information below:

{context}

Please generate a concise explanation that includes:
- English name
- Main ingredients
- Preparation method
- Cultural or historical background (if possible)

Use the provided context as your primary source. You may supplement with general culinary knowledge if the context is brief or lacks detail, but do not contradict it. If uncertain, indicate that the information is inferred or not explicitly known.
Dish: {dish}
""")


llm = wrap(OpenAI(
    api_key="sk-xxxx", # input your key
    base_url="https://api.deepseek.com" # change your llm
))

tracer = Tracer(
    project_name="xxx",#input your project_name
    api_key="xxxx", # input your key
    organization_id="xxxx"# input your key
)

@tracer.observe(span_type="function")
def generate_dish_explanation_rag(dish: str, context_docs: list) -> str:
    context = "\n".join([doc.page_content for doc in context_docs])
    prompt = rag_prompt.format(dish=dish, context=context)

    response = llm.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
