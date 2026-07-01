def process_text(text):
    import nltk
    import re
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tonkenize
    from nltk.stem import PorterStemmer

    ps = PorterStemmer()
    
    text = text.lower()
    cleaned_text = re.sub(r"[^a-z\s]", "" , text)
    token = print(word_tonkenize(text))
  


    en_stopwords = stopwords.words("english")
    stopped_words = " ".join([word for word in text.split() if word.lower() not in en_stopwords])
    for word in stopped_words:
        stem = ps.stem(word)
    print(stem)

    return{
        "Cleaned text" : cleaned_text,
        "Filtered text" : stopped_words,
        "Token" : token,
        "Stemmed words" : stem
    }

