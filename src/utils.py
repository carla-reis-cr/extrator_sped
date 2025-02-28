import re

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def read_arquive(directory):
    with open(directory, "r") as arquive:
     text = arquive.read()
    
    return text