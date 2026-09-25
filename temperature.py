import os
from pathlib import Path

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))


model = ChatGroq(model=os.getenv("GROQ_MODEL", "openai/gpt-oss-20b"), temperature=0.7)