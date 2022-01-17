from re import L
import MySQLdb
from datetime import datetime, timedelta

db_name = "final"
## connection
db = MySQLdb.connect(
    host="database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com",  # your host, usually localhost
    user="admin",  # your username
    passwd="KuraLabs#123",  # your password
    db=db_name,
)  # name of the data base


def list_tables(db_table):
    cur = db.cursor()
    cur.execute(f"SHOW TABLES FROM {db_table};")
    result = cur.fetchall()
    db.commit()
    return result


def create_table(new_name):
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {new_name} (quiz_id VARCHAR(20) NOT NULL, question_number INT NOT NULL, choice_a TEXT NOT NULL, choice_b TEXT NOT NULL, choice_c TEXT NOT NULL, choice_d TEXT NOT NULL);"
    )
    result = cur.fetchall()
    db.commit()
    return print(f"The table '{new_name}' was successfully created!")


def delete_table(target):
    cur = db.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {target};")
    result = cur.fetchall()
    db.commit()
    return print(f"The table '{target}' was successfully deleted!")


## create questions table
def create_questions_table():
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (quiz_id VARCHAR(20) NOT NULL, question_num INT NOT NULL, question_prompt TEXT NOT NULL, answer TEXT NOT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


# insert data into tables
def insert_questions(quiz_id, question_num, question_prompt, answer):
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s);",
        (quiz_id, question_num, question_prompt, answer),
    )
    db.commit()
    return print(
        f"The values '{quiz_id}', '{question_num}', '{question_prompt}', '{answer}', was successfully inserted!"
    )


## create choices table
def create_choices_table():
    table_name = "choices"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (quiz_id VARCHAR(20) NOT NULL, question_num INT NOT NULL, choice_a TEXT NOT NULL, choice_b TEXT NOT NULL, choice_c TEXT NOT NULL, choice_d TEXT NOT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


def insert_choice(quiz_id, question_num, choice_a, choice_b, choice_c, choice_d):
    table_name = "choices"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s,%s,%s);",
        (quiz_id, question_num, choice_a, choice_b, choice_c, choice_d),
    )
    db.commit()
    return print(
        f"The values '{quiz_id}', '{question_num}', '{choice_a}', '{choice_b}', '{choice_c}','{choice_d}', was successfully inserted!"
    )


## create users table
def create_users_table():
    table_name = "users"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (user_id INT NOT NULL, username VARCHAR(30) NOT NULL, fullname VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL, password TEXT NOT NULL, confirmed tinyint(1) DEFAULT 0);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


def insert_users(user_id, username, fullname, email, password, confirmed):
    table_name = "users"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s,%s,%s);",
        (user_id, username, fullname, email, password, confirmed),
    )
    db.commit()
    return print(
        f"The values '{user_id}', '{username}', '{fullname}', '{email}', '{password}','{confirmed}', was successfully inserted!"
    )


## create results table
def create_results_table():
    table_name = "results"
    value = None
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (username VARCHAR(30) NOT NULL, quiz_id VARCHAR(20) NOT NULL, quiz_timestamp VARCHAR(50), session_id INT NOT NULL, score FLOAT);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


def insert_results(username, quiz_id, quiz_timestamp, session_id, score):
    table_name = "results"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s,%s);",
        (username, quiz_id, quiz_timestamp, session_id, score),
    )
    db.commit()
    return print(
        f"The values '{username}', '{quiz_id}', '{session_id}', was successfully inserted!"
    )


## create session table
def create_session_table():
    table_name = "sessions"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (session_id VARCHAR(30) NOT NULL, quiz_id VARCHAR(20) NOT NULL, quiz_start VARCHAR(30) NOT NULL, quiz_expire VARCHAR(30) NOT NULL, current_question INT NOT NULL, answer_1 TEXT NULL, answer_2 TEXT NULL, answer_3 TEXT NULL, answer_4 TEXT NULL, answer_5 TEXT NULL, answer_6 TEXT NULL, answer_7 TEXT NULL, answer_8 TEXT NULL, answer_9 TEXT NULL, answer_10 TEXT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


def insert_session(
    session_id,
    quiz_id,
    quiz_start,
    quiz_expire,
    current_question,
    answer_1,
    answer_2,
    answer_3,
    answer_4,
    answer_5,
    answer_6,
    answer_7,
    answer_8,
    answer_9,
    answer_10,
):
    quiz_start = ""  # datetime.datetime.now()
    quiz_expire = ""  # quiz_start + timedelta(hours=2)
    table_name = "sessions"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
        (
            session_id,
            quiz_id,
            quiz_start,
            quiz_expire,
            current_question,
            answer_1,
            answer_2,
            answer_3,
            answer_4,
            answer_5,
            answer_6,
            answer_7,
            answer_8,
            answer_9,
            answer_10,
        ),
    )
    db.commit()
    return print(
        f"The values '{session_id}', '{quiz_id}', '{quiz_start}', '{quiz_expire}', '{current_question}', was successfully inserted!"
    )


def insert_session_answer(session_id, current_question, answer):
    table_name = "sessions"
    answer_column = f"answer_{current_question}"
    cur = db.cursor()
    cur.execute(
        f"UPDATE {table_name} SET {answer_column} = '{answer}' WHERE session_id = {session_id};"
    )
    db.commit()
    return print(f"The values '{answer}', was successfully inserted into {session_id}!")


def update_curr_question(questionnum):
    session_id = 123456
    cur = db.cursor()
    cur.execute(
        f"UPDATE sessions SET current_question = {questionnum} WHERE session_id = {session_id};"
    )


def insert_session_counter(session_id, current_question):
    table_name = "sessions"
    cur = db.cursor()
    cur.execute(
        f"UPDATE {table_name} SET current_question = '{current_question}' WHERE session_id = {session_id};"
    )
    db.commit()
    return print(
        f"The values '{current_question}', was successfully inserted into {session_id}!"
    )


# query all tables
def query_entire_table(table):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {table};")
    result = list(cur.fetchall())
    # print(f"First Entry fetch: {list(result[1])}")
    db.commit()
    return print(f"Query Results: {result}")


## Delete a table
# delete_table("questions")
# delete_table("choices")
# delete_table("users")
# delete_table("results")
# delete_table("sessions")
# create_questions_table()
# create_choices_table()
# create_users_table()
# create_results_table()
# create_session_table()

# Insert once
# insert_users(
#     1017, "ricardo", "Ricardo Deodutt", "RicardoDeodutt@gmail.com", "KuraLabs#123", 0
# )
# insert_results("ricardo", "quiz1", "", 123456, 0)
# insert_session(123456, "quiz1", "", "", 1, "", "", "", "", "", "", "", "", "", "")


## Creating tables
# create_questions_table()
## insert_questions(quiz_id, question_num, question_prompt, answer)
# insert_questions(
#     "quiz1",
#     "1",
#     "Why is AWS more economical than traditional data centers for applications with varying compute workloads?",
#     "Amazon EC2 instances can be launched on demand when needed",
# )

# create_choices_table()
## insert_choice(quiz_id, question_num, choice_a, choice_b, choice_c, choice_d)
# insert_choice(
#     "quiz1",
#     "1",
#     "Amazon EC2 costs are billed on a monthly basis.",
#     "Amazon EC2 costs are billed on a monthly basis.",
#     "Amazon EC2 instances can be launched on demand when needed",
#     "Users can permanently run enough instances to handle peak workloads",
# )


# create_users_table()
## insert_users(user_id, username, fullname, email, password, confirmed)
# insert_users(
#     1017, "ricardo", "Ricardo Deodutt", "RicardoDeodutt@gmail.com", "KuraLabs#123", 0
# )


# create_results_table()
## insert_results(username, quiz_id, quiz_timestamp, session_id, score)
# insert_results("ricardo", "quiz1", "", 123456, 0)

# create_session_table()
## insert_session(session_id,quiz_id,quiz_start,quiz_expire,current_question,answer_1,answer_2,answer_3,answer_4,answer_5,answer_6,answer_7,answer_8,answer_9,answer_10)
# insert_session(123456, "quiz1", "", "", 1, "", "", "", "", "", "", "", "", "", "")


## insert_session_answer(session_id, current_question, answer)
# insert_session_answer(
#     123456, 1, "Amazon EC2 instances can be launched on demand when needed"
# )


## Query an entire table
# query_entire_table("questions")
# query_entire_table("choices")
# query_entire_table("users")
# query_entire_table("results")
# query_entire_table("sessions")


def query_answer(quiz_id, question_num):
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"SELECT answer FROM questions WHERE quiz_id ='{quiz_id}' AND question_num = '{question_num}';"
    )
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


# print(query_answer("quiz1", 10))


def query_question(quiz_id, question_num):
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"SELECT question_prompt FROM {table_name} WHERE quiz_id ='{quiz_id}' AND question_num = '{question_num}';"
    )
    db.commit()
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


# print(query_question("quiz1", 1))


# grab list of choices for variable question
# need to think of a way to query the choices when we also query for the quiz. consider adding quiz_id to this table
def query_choices(quiz_id, question_num):
    table_name = "choices"
    cur = db.cursor()
    cur.execute(
        f"SELECT choice_a, choice_b, choice_c, choice_d FROM {table_name} where quiz_id = '{quiz_id}' AND question_num = '{question_num}';"
    )
    db.commit()
    result = list(cur.fetchall()[0])
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i])
    return returnlist


# print(query_choices("quiz1", 10))


# creating dictionary output for html
def serve_question(quiz_id, question_num):
    out = {"question": None, "choices": None, "answer": None}
    out["question"] = query_question(quiz_id, question_num)
    out["choices"] = query_choices(quiz_id, question_num)
    out["answer"] = query_answer(quiz_id, question_num)
    return out


# print(serve_question("quiz1", 10))


def get_current_question(session_id, quiz_id):
    table_name = "sessions"
    cur = db.cursor()
    cur.execute(
        f"SELECT current_question FROM {table_name} where session_id = '{session_id}' AND quiz_id = '{quiz_id}';"
    )
    result = list(cur.fetchall())
    print(result)
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist[-1]


# print(get_current_question(123456, "quiz1"))


def get_user_answer(session_id, quiz_id, question_number):
    table_name = "sessions"
    answer_column = f"answer_{question_number}"
    cur = db.cursor()
    cur.execute(
        f"SELECT {answer_column} FROM {table_name} where session_id = '{session_id}' AND quiz_id = '{quiz_id}';"
    )
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist[0]


def get_actual_answer(quiz_id, question_number):
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"SELECT answer FROM {table_name} where question_num = '{question_number}' AND quiz_id = '{quiz_id}';"
    )
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist[0]


def update_total_score(session_id, quiz_id, total_score):
    table_name = "results"
    cur = db.cursor()
    cur.execute(
        f"UPDATE {table_name} SET score = '{total_score}' WHERE session_id = {session_id} AND quiz_id = '{quiz_id}';"
    )
    db.commit()
    return print(
        f"The values Score '{total_score}', was successfully inserted into {session_id}!"
    )


def testing():
    delete_table("questions")
    delete_table("choices")
    delete_table("users")
    delete_table("results")
    delete_table("sessions")
    create_questions_table()
    create_choices_table()
    create_users_table()
    create_results_table()
    create_session_table()
    insert_users(
        1017,
        "ricardo",
        "Ricardo Deodutt",
        "RicardoDeodutt@gmail.com",
        "KuraLabs#123",
        0,
    )
    insert_results("ricardo", "quiz1", "", 123456, 0)
    insert_session(123456, "quiz1", "", "", 1, "", "", "", "", "", "", "", "", "", "")


# testing()
# insert_session(123456, "quiz1", "", "", 1, "", "", "", "", "", "", "", "", "", "")