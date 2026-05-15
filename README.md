# 📝 AI Question Paper Generator

Generate exam questions from any PDF using Claude AI — built with Streamlit.

## Project Structure

```
qpgen/
├── app.py                      # Main Streamlit app (entry point)
├── modules/
│   ├── __init__.py
│   ├── pdf_loader.py           # PDF text extraction logic
│   └── question_generator.py  # Claude API / LLM logic
├── .env.example                # Template for your API key
├── requirements.txt
└── README.md
```

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your API key
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key
```

### 3. Run the app
```bash
streamlit run app.py
```

## How It Works

1. **Upload PDF** — pdfplumber extracts all text page by page
2. **Set Parameters** — choose total marks and number of questions
3. **Generate** — Claude reads the content and crafts a structured question paper
4. **Download** — save the paper as a `.txt` file

## Notes

- Works best with text-based PDFs (not scanned images)
- Minimum ~50 words of content required in the PDF
- API key is loaded from `.env` using `python-dotenv`