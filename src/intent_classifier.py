from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from dataloader import chargerexemple
textes, etiquettes = chargerexemple()

pipe = Pipeline([
    ("vecteuri", TfidfVectorizer(analyzer="char_wb", ngram_range=(2,5)))
    ("classi", LogisticRegression(class_weight="balanced", max_iter=1000))
    ])

pipe.fit(textes, etiquettes)
pipe.predict(["salut"])
pipe.predict_proba(["proba"])
