# 📄 Research Paper Summarizer — LangChain + Groq

A Streamlit app that generates clear, customizable summaries of popular AI/ML research papers using **LangChain** and **Groq**-hosted LLMs. Pick a paper, choose an explanation style and length, and get a tailored summary — complete with math, code intuition, and analogies where relevant.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-green)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

---

## 📌 Overview

This project lets a user select a well-known research paper (e.g. *Attention is All You Need*, *BERT*, *GPT-3*) along with a desired **explanation style** (beginner-friendly, technical, mathematical, code-oriented, etc.) and **summary length**. It then runs a structured LangChain prompt through a Groq-hosted LLM to produce a tailored summary — including relevant equations, simplified code intuition, and analogies, while explicitly avoiding hallucinated details when information isn't available.

---

## ✨ Features

- 🧠 LLM-powered paper summarization via **Groq** (e.g. `openai/gpt-oss-20b`, `openai/gpt-oss-120b`)
- 🎛️ Choose explanation **style** and **length** from dropdowns
- 📐 Includes relevant math and simplified code explanations where applicable
- 🧩 Uses relatable analogies to simplify complex concepts
- 🚫 Avoids guessing — responds with *"insufficient information available"* when the paper doesn't cover something
- 💾 Reusable, serialized prompt template (`prompt_template.json`) built with LangChain's `PromptTemplate`
- ⚙️ Configurable model via environment variable, with sensible fallbacks

---

## 🏗️ Tech Stack

| Component        | Technology                          |
|-------------------|--------------------------------------|
| Framework          | LangChain (`langchain-core`, `langchain-groq`) |
| LLM Provider       | Groq                                 |
| UI                 | Streamlit                            |
| Config             | python-dotenv                        |
| Language           | Python 3.10+                         |

---

## 📂 Project Structure

```
project-root/
├── prompt_ui.py            # Main Streamlit app — collects user input, runs the chain, displays output
├── prompt_generator.py     # Builds and saves the LangChain PromptTemplate to prompt_template.json
├── prompt_template.json    # Serialized prompt template (loaded at runtime by prompt_ui.py)
├── temperature.py          # Standalone script for initializing/testing a ChatGroq model instance
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed — see below)
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root (same folder as `prompt_ui.py`):
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_MODEL=openai/gpt-oss-20b
   ```

   - `GROQ_API_KEY` is **required**. Get one from [console.groq.com](https://console.groq.com).
   - `GROQ_MODEL` is **optional**. If not set, the app falls back to `openai/gpt-oss-20b`, then tries `qwen/qwen3.8-27b` and `openai/gpt-oss-120b` as backups.

   > ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

---

## 🚀 Usage

### 1. Generate the prompt template (only needed once, or after editing the prompt)

```bash
python prompt_generator.py
```

This creates/updates `prompt_template.json`, which the app loads at runtime.

### 2. Run the Streamlit app

```bash
streamlit run prompt_ui.py
```

Then, in the browser window that opens:
1. Select a research paper from the dropdown
2. Choose an explanation style
3. Choose a summary length
4. Click **Summarize**

---

## 🧠 How It Works

1. `prompt_generator.py` defines a structured `PromptTemplate` with instructions for style, length, math inclusion, and analogies, and serializes it to `prompt_template.json`.
2. `prompt_ui.py` loads that template with LangChain's `load_prompt`, collects the user's selections via Streamlit widgets, and builds a chain:
   ```python
   chain = prompt_template | build_model(model_name)
   ```
3. The chain is invoked with the selected paper, style, and length, sending a fully-formed prompt to the Groq-hosted LLM.
4. The model's response is displayed directly in the app.

---

## 🧪 Example

**Selections:**
- Paper: `Attention is All You Need`
- Style: `Beginner friendly`
- Length: `Short (1-2 paragraphs)`

**Output:** A concise, beginner-friendly summary of the Transformer architecture, with simplified explanations of self-attention and any relevant equations from the paper.

---

## 🗺️ Roadmap

- [ ] Add support for uploading custom PDF papers instead of a fixed list
- [ ] Add streaming responses in the UI
- [ ] Add conversational follow-up questions (multi-turn memory)
- [ ] Deploy on Streamlit Community Cloud

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

**Your Name**
📧 your.email@example.com
🔗 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com/your-username)
