import MySQLdb
from datetime import datetime, timedelta
import aws_param as aws

db_name = "final"
## connection
db = MySQLdb.connect(
    host= aws.get_ssm_parameter("/QUIZNOSE/DB_ENDPOINT") ,  # your host, usually localhost #"database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com"
    user= aws.get_ssm_parameter("/QUIZNOSE/DB_USER"),  # your username
    passwd= aws.get_ssm_parameter("/QUIZNOSE/DB_PASS"),  # your password #"KuraLabs#123"
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
        f"CREATE TABLE IF NOT EXISTS {table_name} (user_id INT NOT NULL, username VARCHAR(30) NOT NULL, fullname VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL, password VARCHAR(30) NOT NULL, confirmed tinyint(1) DEFAULT 0);"
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

def insert_all_quiz_data(ans_dict):
    cur = db.cursor()
    session_id = 22222
    for i in range(len(ans_dict)):
        key = str(i+1)
        ans = ans_dict[key]
        col = 'answer_'+key
        cur.execute(f"UPDATE sessions SET {col}= '{ans}' WHERE session_id = {session_id};")
        db.commit()


test_dict = {'1': 'test1', '2': 'test2', '3': 'test3', '4': 'test1', '5': 'test2', '6': 'test3'} 

# insert_session(22222,"quiz1",'','','','','','','','','','','','','')
# for i in range(3):
#         key = str(i+1)
#         ans = test_dict[key]
#         print(key)

insert_all_quiz_data(test_dict)

