from flask import Flask, render_template, request

app = Flask(__name__)

# Correct answers (change these to match YOU!)
correct_answers = {
    "q1": "b",
    "q2": "c",
    "q3": "c",
    "q4": "b",
    "q5": "c"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    score = 0

    for key in correct_answers:
        if request.form.get(key) == correct_answers[key]:
            score += 1

    return render_template("result.html", score=score, total=len(correct_answers))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


