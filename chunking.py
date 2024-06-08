import spacy

nlp = spacy.load("en_core_web_sm")

def sentence_chunking(text, max_chunk_size=512):
    doc = nlp(text)
    chunks = []
    chunk = ""
    
    for sent in doc.sents:
        if len(chunk) + len(sent.text) > max_chunk_size:
            chunks.append(chunk.strip())
            chunk = sent.text
        else:
            chunk += " " + sent.text
    
    if chunk:
        chunks.append(chunk.strip())
    
    return chunks
