from flask import request, render_template, Blueprint, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
import db
from sessioncheck import is_logged

serve_quiz_blueprint = Blueprint("serve_quiz", __name__)

from results import results_blueprint


@serve_quiz_blueprint.route("/<user_id>/quiz", methods=["GET", "POST"])
@is_logged
def quiz(user_id):
    if user_id == str(session['user_id']):
        quiz = "quiz1"
        session_id = 123456
        min_question = 1
        max_question = 10
        current_question = int(db.get_current_question(session_id, quiz))
        print(f"Current question -> {current_question}")

        if current_question <= max_question:
            current_question = int(db.get_current_question(session_id, quiz))
            data = db.serve_question(quiz, current_question)
            question_prompt = data.get("question")[0]
            option_a = data.get("choices")[0]
            option_b = data.get("choices")[1]
            option_c = data.get("choices")[2]
            option_d = data.get("choices")[3]

            #the back button will send a get request and execute this logic as oppose to the exiting logic for submitting answers
            if request.method == "GET" and current_question>min_question:
                    current_question = current_question - 1
                    db.update_curr_question(current_question)
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

            if request.method == "POST": # checks for type of request
                if "quiz_choice" in request.form: #checks to see if answer was selected 
                    # if an answer was selected, make adjustments to backend 
                    if "choice_a" in request.form["quiz_choice"]:
                        db.insert_session_answer(session_id, current_question, option_a)

                    elif "choice_b" in request.form["quiz_choice"]:
                        db.insert_session_answer(session_id, current_question, option_b)


                    elif "choice_c" in request.form["quiz_choice"]:
                        db.insert_session_answer(session_id, current_question, option_c)


                    elif "choice_d" in request.form["quiz_choice"]:
                        db.insert_session_answer(session_id, current_question, option_d)

                else:
                    #if answer was selected, do nothing
                    pass
                
                #increment counter and serve quiz page, if current_question > 10, calculate results and sent to /results
                current_question = current_question + 1
                db.insert_session_counter(session_id, current_question)
                if current_question > max_question:
                    print("finished test")
                    return redirect(url_for("results.results_blueprint"))
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

            # elif request.method == "POST" and "choice_a" in request.form["quiz_choice"]:
            #     print(type(request.form["quiz_choice"]))
            #     db.insert_session_answer(session_id, current_question, option_a)
            #     current_question = current_question + 1
            #     db.insert_session_counter(session_id, current_question)
            #     if current_question > max_question:
            #         print("finished test")
            #         return redirect(url_for("results"))
            #     else:
            #         data = db.serve_question(quiz, current_question)
            #         question_prompt = data.get("question")[0]
            #         option_a = data.get("choices")[0]
            #         option_b = data.get("choices")[1]
            #         option_c = data.get("choices")[2]
            #         option_d = data.get("choices")[3]
            #         return render_template(
            #             "quiz.html",
            #             current_question=current_question,
            #             question_prompt=question_prompt,
            #             option_a=option_a,
            #             option_b=option_b,
            #             option_c=option_c,
            #             option_d=option_d,
            #         )

            # elif request.method == "POST" and "choice_b" in request.form["quiz_choice"]:
            #     db.insert_session_answer(session_id, current_question, option_b)
            #     current_question = current_question + 1
            #     db.insert_session_counter(session_id, current_question)
            #     if current_question > max_question:
            #         print("finished test")
            #         return redirect(url_for("results"))
            #     else:
            #         data = db.serve_question(quiz, current_question)
            #         question_prompt = data.get("question")[0]
            #         option_a = data.get("choices")[0]
            #         option_b = data.get("choices")[1]
            #         option_c = data.get("choices")[2]
            #         option_d = data.get("choices")[3]
            #         return render_template(
            #             "quiz.html",
            #             current_question=current_question,
            #             question_prompt=question_prompt,
            #             option_a=option_a,
            #             option_b=option_b,
            #             option_c=option_c,
            #             option_d=option_d,
            #         )

            # elif request.method == "POST" and "choice_c" in request.form["quiz_choice"]:
            #     db.insert_session_answer(session_id, current_question, option_c)
            #     current_question = current_question + 1
            #     db.insert_session_counter(session_id, current_question)
            #     if current_question > max_question:
            #         print("finished test")
            #         return redirect(url_for("results"))
            #     else:
            #         data = db.serve_question(quiz, current_question)
            #         question_prompt = data.get("question")[0]
            #         option_a = data.get("choices")[0]
            #         option_b = data.get("choices")[1]
            #         option_c = data.get("choices")[2]
            #         option_d = data.get("choices")[3]
            #         return render_template(
            #             "quiz.html",
            #             current_question=current_question,
            #             question_prompt=question_prompt,
            #             option_a=option_a,
            #             option_b=option_b,
            #             option_c=option_c,
            #             option_d=option_d,
            #         )

            # elif request.method == "POST" and "choice_d" in request.form["quiz_choice"]:
            #     db.insert_session_answer(session_id, current_question, option_d)
            #     current_question = current_question + 1
            #     db.insert_session_counter(session_id, current_question)
            #     if current_question > max_question:
            #         print("finished test")
            #         return redirect(url_for("results"))
            #     else:
            #         data = db.serve_question(quiz, current_question)
            #         question_prompt = data.get("question")[0]
            #         option_a = data.get("choices")[0]
            #         option_b = data.get("choices")[1]
            #         option_c = data.get("choices")[2]
            #         option_d = data.get("choices")[3]
            #         return render_template(
            #             "quiz.html",
            #             current_question=current_question,
            #             question_prompt=question_prompt,
            #             option_a=option_a,
            #             option_b=option_b,
            #             option_c=option_c,
            #             option_d=option_d,
            #         )



        if current_question > max_question:
            print("finished test")
            return redirect(url_for("results.results_blueprint"))

        return render_template(
            "quiz.html",
            current_question=current_question,
            question_prompt=question_prompt,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
        )
    else:
        flash('You are not logged in to take this exam as the proper user', 'danger')
        return redirect(url_for('login_page.login'))