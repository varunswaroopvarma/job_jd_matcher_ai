import re
import nltk
from nltk.corpus import stopwords

# Download required data (only once)
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)

# NLTK stopwords
stop_words = set(stopwords.words("english"))

# Extra unwanted keywords from your list + generic filler words
bad_keywords = {
    "criteria", "quick", "tech", "stream", "transparent", "submitted", "industry",
    "reputed", "learner", "candor", "shares", "written", "contributes", "trending",
    "decision", "standards", "authorities", "strategically", "noc", "challenges",
    "characteristics", "agile", "information", "communicator", "desired", "ability",
    "critical", "backlogs", "solver", "good", "existing", "cgpa", "thinker",
    "specialization", "speaks", "constructively", "committed", "eligibility",
    "prioritizes", "enthusiast", "processes", "minded", "candidate", "date",
    "preferred", "humble", "students", "receptive", "analytical", "tools",
    "verbal", "leadership", "offer", "percentage", "issuance", "institutes",
    "current", "respectful", "year", "maker", "focused", "active",
    # Short numbers/words
    "1st", "2nd", "3rd", "4th"
}

# Merge stopwords and bad keywords
all_stopwords = stop_words.union(bad_keywords)

def clean_and_extract_keywords(text):
    """Clean text and return meaningful keywords only"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#]", " ", text)  # keep programming skills like c++, c#, python3
    words = text.split()
    keywords = [w for w in words if w not in all_stopwords and len(w) > 2]
    return set(keywords)

def match_jd_resume(resume_text, jd_text):
    """Compare Resume with Job Description and return similarity % and HTML highlights"""
    resume_keywords = clean_and_extract_keywords(resume_text)
    jd_keywords = clean_and_extract_keywords(jd_text)

    if not jd_keywords:
        return 0, ""

    common = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    similarity = round((len(common) / len(jd_keywords)) * 100, 2)

    # Generate HTML with color highlights
    highlights = []
    for kw in jd_keywords:
        if kw in common:
            highlights.append(f"<span class='matched'>{kw}</span>")
        else:
            highlights.append(f"<span class='missing'>{kw}</span>")

    return similarity, " ".join(highlights)
