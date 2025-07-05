import re
import requests

def load_document_text(url: str) -> str:
    """
    Загружает текстовый контент из Google Docs по ссылке.
    """
    # Извлекаем ID документа из URL
    match_ = re.search(r'/document/d/([a-zA-Z0-9-_]+)', url)
    if match_ is None:
        raise ValueError('Invalid Google Docs URL')
    
    doc_id = match_.group(1)

    # Загружаем документ в формате .txt
    response = requests.get(f'https://docs.google.com/document/d/{doc_id}/export?format=txt')
    response.raise_for_status()
    
    return response.text