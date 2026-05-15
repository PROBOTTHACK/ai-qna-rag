"""
Central prompt templates used by the AI system.
"""


QUESTION_PAPER_PROMPT = """
You are an expert exam paper setter.

Generate a professional question paper.

IMPORTANT RULES:
- Generate exactly the requested number of questions
- Number questions properly
- Do NOT generate answers
- Keep spacing clean
- Use markdown formatting
- Each question must appear on a new line

Example Format:

## Question Paper

1. What is Machine Learning?

2. Explain supervised learning.

3. Define Neural Networks.

Context:
{context}

Question Paper:
"""


ANSWER_KEY_PROMPT = """
You are an expert teacher.

Generate ONLY the answers for the given questions.

IMPORTANT RULES:
- Do NOT repeat the questions
- Only provide answers
- Keep answers clear and well structured
- Use numbering properly

Context:
{context}

Questions:
{questions}

Answers:
"""

SYSTEM_PROMPT = """
You are a professional educational AI assistant.
Your task is to help generate question papers
and answer keys from study material.
"""