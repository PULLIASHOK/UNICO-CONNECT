import pytesseract from PIL import image
import spacy

nlp=spacy.load("en_core_web_sm")
image_path="C:\Users\ADMIN\OneDrive\Pictures\Screenshots\Screenshot 2024-05-23 192011.png"
text=pytesseract.image.to_string(Image.open(image_path))
print("Extracted Text:")
print(text)

doc=nlp(text)
print("\nEntities")
for ent in doc.ents:
    print(f"{ent.text} ({ent.lebel_})")
