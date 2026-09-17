from src.data_loader import load_courses
from src.recommender import build_recommender,recommend
def test_dataset():
    df=load_courses()
    assert len(df)>=10
    assert {"course","domain","level","keywords"}.issubset(df.columns)
def test_recommendation():
    df=load_courses(); v,m=build_recommender(df)
    r=recommend(df,v,m,"Python","Machine Learning","beginner")
    assert len(r)==5
    assert r["similarity"].between(0,1).all()
