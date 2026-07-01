import nltk

from text_processor import process_text
nltk.download("stopwords")
nltk.download("punkt")

Input_box  = input("Enter your paragraph here: ")
result  = process_text(Input_box)

print(result)

