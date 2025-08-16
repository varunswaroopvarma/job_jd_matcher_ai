from flask import Flask, render_template, request
from matcher import match_jd_resume
from utils import extract_text_from_file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        jd_text = request.form["jd"]

        resume_text = extract_text_from_file(resume_file)

        score, missing_keywords = match_jd_resume(resume_text, jd_text)

        return render_template(
            "index.html",
            score=round(score * 100, 2),
            missing_keywords=missing_keywords,
            jd=jd_text,
            resume_text=resume_text
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
