from bnlp import CleanText
from bnlp import BengaliCorpus as corpus

def clean_text(text):
    stopwords = corpus.stopwords

    clean_text = CleanText(
    fix_unicode=True,
    unicode_norm=True,
    unicode_norm_form="NFKC",
    remove_url=True,
    remove_email=True,
    remove_emoji=True,
    remove_number=False,
    remove_digits=False,
    remove_punct=False
    )

    clean_text = clean_text(text)
    clean_text = " ".join([word for word in clean_text.split() if word not in stopwords])

    return clean_text