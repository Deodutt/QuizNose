import MySQLdb
import config, os

db_name = "final"
## connection
db = MySQLdb.connect(
    host="database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com",  # your host, usually localhost
    user="admin",  # your username
    passwd="KuraLabs#123",  # your password
    db=db_name,
)  # name of the data base

# query all tables
def query_entire_table(table):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {table};")
    result = list(cur.fetchall())
    # print(f"First Entry fetch: {list(result[1])}")
    db.commit()
    return print(f"Query Results: {result}")


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

########## For loading all questions at once #############

# grab list of choices for variable question
#need to think of a way to query the choices when we also query for the quiz. consider adding quiz_id to this table
def query_choices2(q_id):
    table_name = "choices"
    cur = db.cursor()
    cur.execute(f"SELECT choice_a,choice_b,choice_c,choice_d FROM {table_name};")
    result = list(cur.fetchall())
    # print(f"First Entry fetch: {list(result[1])}")
    db.commit()
    # return print(f"{q_id} Results: {result}")
    # returnlist = []
    # for i in range(len(result)):
    #     returnlist.append(result[i][0])
    return result

def query_question2(q_id):
    cur = db.cursor()
    cur.execute(f"SELECT question_prompt FROM questions WHERE quiz_id ='{q_id}';")
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


def query_ans2(q_id):
    cur = db.cursor()
    cur.execute(f"SELECT answer FROM questions WHERE quiz_id ='{q_id}';")
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist

def grab_question2(quiz_num):
    out = {"question": None, "choices": None, "ans": None}
    out["question"] = query_question2(quiz_num)
    out["choices"] = query_choices2(quiz_num)
    out["ans"] = query_ans2(quiz_num)
    return out

