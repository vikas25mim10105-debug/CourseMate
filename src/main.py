from .data_loader import load_courses
from .recommender import build_recommender,recommend
def main():
    print("="*35); print("        CourseMate"); print(" AI Course Recommendation System"); print("="*35)
    df=load_courses(); v,m=build_recommender(df)
    skill=input("Enter your skill (e.g. Python): ").strip()
    interest=input("Enter your interest (e.g. Machine Learning): ").strip()
    level=input("Enter your preferred level (beginner/intermediate): ").strip().lower()
    result=recommend(df,v,m,skill,interest,level)
    print("\nRecommended Courses"); print("-"*35)
    for i,row in enumerate(result.itertuples(index=False),1):
        print(f"{i}. {row.course}")
        print(f"   Domain: {row.domain} | Level: {row.level}")
if __name__=="__main__": main()
