from flask import Flask, render_template, request, Blueprint
from werkzeug.utils import secure_filename
from csv import reader
import os
import db

upload_test_blueprint = Blueprint("upload_test", __name__)


script_dir = os.path.dirname(__file__)
rel_path = f"./questions/"
UPLOAD_FOLDER = os.path.join(script_dir, rel_path)
app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

## allows users to upload quiz
@upload_test_blueprint.route("/create_test", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        user_filename = request.files["file"].filename
        file_ext = user_filename[-4:]

        # check if the post request has the file part
        if "file" not in request.files:
            status = "Error: No file part"
            return render_template("create_test.html", status=status)

        file = request.files["file"]

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == "":
            status = "Error: No file was selected"
            return render_template("create_test.html", status=status)

        elif file and file_ext != ".csv":
            status = "Error: Incorrect file type!"
            return render_template("create_test.html", status=status)

        elif file and file_ext == ".csv":
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            csv_reader(filename)
            status = "successful upload"
            return render_template("create_test.html", status=status)

    return render_template("create_test.html")


def csv_reader(filename):
    # skip first line i.e. read header first and then iterate over each row od csv as a list
    # with open(f"./{filename}.csv", "r") as read_obj:
    script_dir = os.path.dirname(__file__)
    rel_path = f"./questions/{filename}"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, "r") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)  # next() skips the first line
        num_rows = 1
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                quiz_id = row[0]
                question_number = row[1]
                question_prompt = row[3]
                choice_a = row[4]
                choice_b = row[5]
                choice_c = row[6]
                choice_d = row[7]
                answer = row[2]
                num_rows += 1

                db.insert_questions(quiz_id, question_number, question_prompt, answer)

                db.insert_choice(
                    quiz_id, question_number, choice_a, choice_b, choice_c, choice_d
                )

    return print("finished uploading to database!")


# csv_reader("quiz1")