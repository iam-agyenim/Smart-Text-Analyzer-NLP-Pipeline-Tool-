def process_text(text):
    import nltk
    from nltk.corpus import stopwords

    en_stopwords = stopwords.words("english")
    stopped_words = "Cleaned text : " + " " .join([word for word in text.split() if word.lower() not in en_stopwords])
    return(stopped_words)

