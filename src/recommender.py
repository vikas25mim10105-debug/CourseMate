from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def build_recommender(df):
    text=df["domain"].fillna("")+" "+df["level"].fillna("")+" "+df["keywords"].fillna("")
    v=TfidfVectorizer(stop_words="english")
    return v,v.fit_transform(text)
def recommend(df,vectorizer,matrix,skill,interest,level,top_n=5):
    user=vectorizer.transform([f"{skill} {interest} {level}"])
    scores=cosine_similarity(user,matrix).flatten()
    out=df.copy(); out["similarity"]=scores
    return out.sort_values("similarity",ascending=False).head(top_n)
