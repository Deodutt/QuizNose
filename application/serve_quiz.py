from flask import request, render_template, Blueprint
from flask.helpers import url_for
from werkzeug.utils import redirect
import db

serve_quiz_blueprint = Blueprint("serve_quiz", __name__)


@serve_quiz_blueprint.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz = "quiz1"
    session = 123456
    min_question = 1
    max_question = 10
    current_question = int(db.get_current_question(session, quiz))
    print(f"Current question -> {current_question}")

    if current_question <= max_question:
        current_question = int(db.get_current_question(session, quiz))
        data = db.serve_question(quiz, current_question)
        question_prompt = data.get("question")[0]
        option_a = data.get("choices")[0]
        option_b = data.get("choices")[1]
        option_c = data.get("choices")[2]
        option_d = data.get("choices")[3]

        if request.method == "GET" and current_question>min_question:
                current_question = current_question - 1
                db.update_curr_question(current_question)
            # if current_question == min_question:
            #     return redirect(url_for("quiz"))
            # else:
                data = db.serve_question(quiz, current_question)
                question_prompt = data.get("question")[0]
                option_a = data.get("choices")[0]
                option_b = data.get("choices")[1]
                option_c = data.get("choices")[2]
                option_d = data.get("choices")[3]
                return render_template(
                    "quiz.html",
                    current_question=current_question,
                    question_prompt=question_prompt,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                )

        if request.method == "POST" and "choice_a" in request.form["quiz_choice"]:
            db.insert_session_answer(session, current_question, option_a)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return redirect(url_for("results"))
            else:
                data = db.serve_question(quiz, current_question)
                question_prompt = data.get("question")[0]
                option_a = data.get("choices")[0]
                option_b = data.get("choices")[1]
                option_c = data.get("choices")[2]
                option_d = data.get("choices")[3]
                return render_template(
                    "quiz.html",
                    current_question=current_question,
                    question_prompt=question_prompt,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                )

        elif request.method == "POST" and "choice_b" in request.form["quiz_choice"]:
            db.insert_session_answer(session, current_question, option_b)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return redirect(url_for("results"))
            else:
                data = db.serve_question(quiz, current_question)
                question_prompt = data.get("question")[0]
                option_a = data.get("choices")[0]
                option_b = data.get("choices")[1]
                option_c = data.get("choices")[2]
                option_d = data.get("choices")[3]
                return render_template(
                    "quiz.html",
                    current_question=current_question,
                    question_prompt=question_prompt,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                )

        elif request.method == "POST" and "choice_c" in request.form["quiz_choice"]:
            db.insert_session_answer(session, current_question, option_c)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return redirect(url_for("results"))
            else:
                data = db.serve_question(quiz, current_question)
                question_prompt = data.get("question")[0]
                option_a = data.get("choices")[0]
                option_b = data.get("choices")[1]
                option_c = data.get("choices")[2]
                option_d = data.get("choices")[3]
                return render_template(
                    "quiz.html",
                    current_question=current_question,
                    question_prompt=question_prompt,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                )

        elif request.method == "POST" and "choice_d" in request.form["quiz_choice"]:
            db.insert_session_answer(session, current_question, option_d)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return redirect(url_for("results"))
            else:
                data = db.serve_question(quiz, current_question)
                question_prompt = data.get("question")[0]
                option_a = data.get("choices")[0]
                option_b = data.get("choices")[1]
                option_c = data.get("choices")[2]
                option_d = data.get("choices")[3]
                return render_template(
                    "quiz.html",
                    current_question=current_question,
                    question_prompt=question_prompt,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                )

    if current_question > max_question:
        print("finished test")
        return redirect(url_for("results"))

    return render_template(
        "quiz.html",
        current_question=current_question,
        question_prompt=question_prompt,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
    )