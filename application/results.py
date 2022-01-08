from flask import(
    Flask,
    render_template,
    Blueprint

)
from flask.scaffold import _matching_loader_thinks_module_is_package

import db
from sessioncheck import is_logged



app = Flask(__name__, template_folder="templates", static_url_path="/static")


results_blueprint = Blueprint("results_page", __name__)


@results_blueprint.route("/results", methods = ['GET', 'POST'])
@is_logged
def results():
    quiz = "quiz1"
    session_id = 123456
    max_question = 10
    total_score = 0
    db.update_total_score(session_id, quiz, total_score)

    for number in range(1, max_question + 1):
        # question_number = number
        # question_prompt = db.query_question(quiz, number)[0]
        user_answer = str(db.get_user_answer(session_id, quiz, number)).strip()
        actual_answer = str(db.get_actual_answer(quiz, number)).strip()

        if user_answer == actual_answer:
            total_score += 1
            db.update_total_score(session_id, quiz, total_score)
        else:
            print(f"{number} is incorrect!")

    return render_template("tests_result.html", total_score=total_score)