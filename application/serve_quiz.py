from flask import request, render_template, Blueprint
import db

serve_quiz_blueprint = Blueprint("serve_quiz", __name__)


@serve_quiz_blueprint.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz = "quiz1"
    session = 123456
    max_question = 10
    current_question = int(db.get_current_question(session, quiz))
    print(f"current question -> {current_question}")

    if current_question <= max_question:
        current_question = int(db.get_current_question(session, quiz))
        data = db.serve_question(quiz, current_question)
        question_prompt = data.get("question")[0]
        option_a = data.get("choices")[0]
        option_b = data.get("choices")[1]
        option_c = data.get("choices")[2]
        option_d = data.get("choices")[3]

        if request.method == "POST" and "choice_a" in request.form["quiz_choice"]:
            # update the question counter and record the answer user had
            db.insert_session_answer(session, current_question, option_a)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return render_template("tests_result.html")
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
            db.insert_session_answer(session, current_question, option_a)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return render_template("tests_result.html")
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
            db.insert_session_answer(session, current_question, option_a)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return render_template("tests_result.html")
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
            db.insert_session_answer(session, current_question, option_a)
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            if current_question > max_question:
                print("finished test")
                return render_template("tests_result.html")
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
        return render_template("tests_result.html")

    return render_template(
        "quiz.html",
        current_question=current_question,
        question_prompt=question_prompt,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
    )