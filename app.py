from flask import Flask, render_template, request
from matcher import match_jd_resume
from utils import extract_text_from_pdf, extract_text_from_txt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    similarity_score = None
    highlights_html = ""  # This will contain matched/missing keywords in HTML

    if request.method == "POST":
        resume_text = ""
        jd_text = request.form.get("jd", "")

        # Handle uploaded resume file
        if "resume" in request.files:
            file = request.files["resume"]
            if file and file.filename.lower().endswith(".pdf"):
                resume_text = extract_text_from_pdf(file)
            elif file and file.filename.lower().endswith(".txt"):
                resume_text = extract_text_from_txt(file)

        if resume_text and jd_text:
            similarity_score, highlights_html = match_jd_resume(resume_text, jd_text)

    return render_template(
        "index.html",
        similarity_score=similarity_score,
        highlights_html=highlights_html
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
