from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
        template="""Please summarize the research paper {paper_input} with the following specification:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
- include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
- use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "insufficient information available" instead of guessing or making assumptions.
Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
        input_variables=["paper_input", "style_input", "length_input", "user_input"],
        validate_template=True    
)

prompt_template.save('prompt_template.json')