import re
import string
import nltk
from nltk.corpus import stopwords

# download stopwords kalau belum ada
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Membersihkan teks tweet:
    - lowercase
    - hapus URL, mention, hashtag
    - hapus tanda baca & angka
    - hapus stopwords
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)   # hapus URL
    text = re.sub(r"@\w+", "", text)             # hapus mention
    text = re.sub(r"#\w+", "", text)             # hapus hashtag
    text = re.sub(r"\d+", "", text)              # hapus angka
    text = text.translate(str.maketrans("", "", string.punctuation))

    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)