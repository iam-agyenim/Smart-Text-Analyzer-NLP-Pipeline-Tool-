# Smart-Text-Analyzer-NLP-Pipeline-Tool-

A lightweight Natural Language Processing (NLP) project that takes raw text input and processes it through a full preprocessing pipeline including tokenization, stopword removal, stemming, and regex-based pattern extraction.

This project demonstrates fundamental NLP concepts using Python and NLTK.

---

## Features

* Text cleaning and normalization
* Tokenization using NLTK
* Stopword removal
* Word stemming (Porter Stemmer)
* Regex-based pattern extraction (emails, numbers, URLs)
* Simple command-line interface

---

## Project Structure

```text
Smart-Text-Analyzer/
│
├── main.py                  # Entry point of the application
├── text_processor.py       # NLP preprocessing pipeline
├── regex_extractor.py      # Regex pattern extraction
├── sentiment.py            # (Optional) sentiment analysis module
├── utils.py                # Helper functions
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .gitignore
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/iam-agyenim/Smart-Text-Analyzer-NLP-Pipeline-Tool-
cd Smart-Text-Analyzer
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK resources

```python
import nltk
nltk.download("stopwords")
nltk.download("punkt")
```

---

## ▶ Usage

Run the program:

```bash
python main.py
```

Enter a paragraph when prompted:

```text
Enter your paragraph here: Artificial Intelligence is changing the world...
```

---

##  Example Output

```text
Cleaned Text: artificial intelligence changing world enabling machines learn data
Tokens: ['artificial', 'intelligence', 'changing', 'world']
Stemmed Words: ['artifici', 'intellig', 'chang', 'world']
Extracted Emails: []
Extracted Numbers: []
```

---

##  Concepts Used

* Natural Language Processing (NLP)
* Tokenization
* Stopword Removal
* Stemming (Porter Stemmer)
* Regular Expressions (Regex)
* Python text processing

---

##  Requirements

* Python 3.8+
* NLTK

Install dependencies:

```bash
pip install nltk
```

---

##  Future Improvements

* Add Lemmatization (WordNetLemmatizer)
* Add Sentiment Analysis (VADER or ML model)
* Add Streamlit web interface
* Add TF-IDF keyword extraction
* Support file uploads (.txt, .csv)

---

##  Author

Built by a Computer Science student exploring NLP and AI systems.

---

##  Why this project matters

This project demonstrates the core building blocks of real-world NLP systems used in:

* Chatbots
* Search engines
* AI assistants
* Text classification systems

