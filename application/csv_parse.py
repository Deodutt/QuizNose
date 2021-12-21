from csv import reader
import os
import db


def csv_reader(filename):
    # skip first line i.e. read header first and then iterate over each row od csv as a list
    # with open(f"./{filename}.csv", "r") as read_obj:
    script_dir = os.path.dirname(__file__)
    rel_path = f"./questions/{filename}.csv"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, "r") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)  # next() skips the first line
        num_rows = 1
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                quiz_number = row[0]
                question_number = f"q{num_rows}"
                question_prompt = row[2]
                choice_a = row[3]
                choice_b = row[4]
                choice_c = row[5]
                choice_d = row[6]
                answers = row[1]
                num_rows += 1

                db.insert_questions(
                    quiz_number, question_number, question_prompt, answers
                )

                db.insert_choice(question_number, choice_a)
                db.insert_choice(question_number, choice_b)
                db.insert_choice(question_number, choice_c)
                db.insert_choice(question_number, choice_d)
                print("finished parsing")
    return