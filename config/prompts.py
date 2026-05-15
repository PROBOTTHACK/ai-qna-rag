"""
Central prompt templates used by the AI system.
"""


QUESTION_PAPER_PROMPT = """
You are an expert exam paper setter.

Use the provided context to generate a professional question paper.

Requirements:
- Generate clear and concise questions
- Maintain academic quality
- Avoid duplicate questions
- Cover important concepts
- Use proper formatting

Context:
{context}

Question Paper:
"""


ANSWER_KEY_PROMPT = """
You are an expert teacher.

Generate detailed and accurate answers
for the given question paper using the provided context.

Context:
{context}

Questions:
{questions}

Answer Key:
"""


SYSTEM_PROMPT = """
You are a professional educational AI assistant.
Your task is to help generate question papers
and answer keys from study material.
"""