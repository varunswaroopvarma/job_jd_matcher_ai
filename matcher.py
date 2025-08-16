import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jd_resume(resume_text, jd_text):
    """
    Compare resume and job description using cosine similarity.
    Returns: (similarity_score, missing_keywords)
    """
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    resume_words = set(re.findall(r'\b\w+\b', resume_text))
    jd_words = set(re.findall(r'\b\w+\b', jd_text))

    missing_keywords = jd_words - resume_words

    vectorizer = CountVectorizer().fit([resume_text, jd_text])
    vectors = vectorizer.transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return similarity, missing_keywords
