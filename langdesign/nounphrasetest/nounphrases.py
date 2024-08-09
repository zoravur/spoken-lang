import spacy
import sys

# load the english model
nlp = spacy.load("en_core_web_sm")

def extract_complex_noun_phrases(text):
    doc = nlp(text)
    noun_phrases = []
    current_phrase = []
    
    for token in doc:
        if token.dep_ in ("det", "compound", "amod", "nummod") or token.pos_ == "NOUN":
            current_phrase.append(token.text)
        elif token.dep_ == "prep" and token.head.pos_ == "NOUN":
            current_phrase.append(token.text)
        elif token.dep_ == "pobj" and current_phrase:
            current_phrase.append(token.text)
        else:
            if current_phrase:
                noun_phrases.append(" ".join(current_phrase))
                current_phrase = []
    
    # add the last collected phrase if there is one
    if current_phrase:
        noun_phrases.append(" ".join(current_phrase))
    
    return noun_phrases

# example usage
text = sys.stdin.read()
noun_phrases = extract_complex_noun_phrases(text)
print(noun_phrases)
