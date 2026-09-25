
import os
from pathlib import Path
from pyexpat import model

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY is not set. Add it to your environment or .env file.")
    st.stop()

groq_model_candidates = [
    os.getenv("GROQ_MODEL"),
    "openai/gpt-oss-20b",
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b",
]

groq_model_candidates = [model for model in groq_model_candidates if model]


def build_model(model_name: str) -> ChatGroq:
    return ChatGroq(model=model_name, temperature=0.7, api_key=groq_api_key)

st.header("Research Tools")
#user_input=st.text_input("Enter your research question here")
paper_input=st.selectbox("Select a research paper Name", ["Attention is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis","Neural Ordinary Differential Equations","AlphaFold: Using AI for scientific discovery","DALL·E: Creating Images from Text","CLIP: Connecting Text and Images","Neural Radiance Fields (NeRF): Representing Scenes as Neural Networks","Transformers in Computer Vision: A Survey"])
style_input=st.selectbox("Select Explination Style", ["Beginnner  friendly", "Detailed Explanation", "Technical Explanation","code_oriented Explanation","Mathematical Explanation"])
length_input=st.selectbox("Select Length of the Summary", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

prompt_template=load_prompt("prompt_template.json")


if st.button("summarize"):
    chain=prompt_template | build_model(groq_model_candidates[0])
    result=chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    st.write(result.content)
    

    