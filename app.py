from flask import Flask, render_template, redirect, url_for
from surveys import satisfaction_survey

app = Flask(__name__)

# Initialize the list to store user response
responses = []

@app.route('/')
def start_page():
    #Info about survey
    title= satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    # Render the survey start page with instructions and title
    return render_template('start.html', title=title, instructions=instructions)


@app.route("/questions/<int:question_id>")
def show_question(question_id):
    """ Show the current question. """
    if question_id != len(responses):
        return redirect(url_for("show_question", question_id=len(responses)))
    
    question = satisfaction_survey.questions[question_id]

    return render_template("question.html", question=question, question_id=question_id, survey=satisfaction_survey)


if __name__=="__main__":
    app.run(debug=True)

