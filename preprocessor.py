import re


# --- Preprocess the Data ---
def preprocess_content(text):
    text = text.replace('\xa0', ' ')
    text = text.replace('\n', ' ')
    text = re.sub(' +', ' ', text)
    text = re.sub(r'(?<=[a-z])([A-Z][a-z]+)', r'\n\1', text)
    text = re.sub(r'\d+TS', '', text)
    text = re.sub(r'\{\d+(\.\d+)?\}', '', text)
    content = re.sub(r'\{.*?\}', '', text)
    content = re.sub(r'\s+', ' ', text)
    content = content.strip()
    return content


