import json
from flask import Flask, render_template, request
import datetime

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)

with open("Mappings.json") as f:
    mappings = json.load(f)

with open("UserFeedback.json") as f:
    user_feedback = json.load(f)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", mappings=mappings)


@app.route("/feedback/<filename>", methods=["GET"])
def show_feedback_page(filename):
    if filename not in mappings:
        return render_template(
            "index.html", mappings=mappings, alert_message="Invalid Filename"
        )

    text = mappings[filename]
    words = text.split()

    return render_template("feedback.html", filename=filename, text=text, words=words)


@app.route("/feedback/<filename>", methods=["POST"])
def get_feedback(filename):
    text = request.form["text"]
    words = text.split()
    wrong_words = request.form.getlist("wrong_words")
    wrong_words = list(map(lambda index: words[int(index)], wrong_words))

    if filename not in user_feedback:
        user_feedback[filename] = []

    user_feedback[filename].append(
        {
            "text": text,
            "wrong_words": wrong_words,
            "submitted_at": datetime.datetime.now().isoformat(),
        }
    )

    with open("UserFeedback.json", "w", encoding="utf-8") as f:
        json.dump(user_feedback, f, ensure_ascii=False)

    return render_template(
        "index.html", mappings=mappings, alert_message="Feedback Submitted Successfully"
    )


if __name__ == "__main__":
    app.run(debug=True)
