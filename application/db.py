import MySQLdb

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
    cur.execute(f"DROP TABLE {target};")
    result = cur.fetchall()
    db.commit()
    return print(f"The table '{target}' was successfully deleted!")


## create questions table
def create_questions_table():
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (quiz_id VARCHAR(20) NOT NULL, q_id VARCHAR(20) NOT NULL, q TEXT NOT NULL, ans VARCHAR(20) NOT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


## create choices table
def create_choices_table():
    table_name = "choices"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} ( q_id VARCHAR(20) NOT NULL, choice VARCHAR(20) NOT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


## create quiz table
def create_quizzes_table():
    table_name = "quizzes"
    cur = db.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS quizzes (quiz_id VARCHAR(20) NOT NULL);")
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


## create results table
def create_results_table():
    table_name = "results"
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} (quiz_id varchar(10) NOT NULL, a varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL, b varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, c varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, d varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, grade float DEFAULT NULL);"
    )
    db.commit()
    return print(f"The table '{table_name}' was successfully created!")


# insert data into tables
def insert_questions(quiz_id, q_id, q, ans):
    table_name = "questions"
    cur = db.cursor()
    cur.execute(
        f"INSERT INTO {table_name} VALUES(%s,%s,%s,%s);", (quiz_id, q_id, q, ans)
    )
    db.commit()
    return print(
        f"The values '{quiz_id}', '{q_id}', '{q}', '{ans}', was successfully inserted!"
    )


def insert_choice(q_id, choice):
    table_name = "choices"
    cur = db.cursor()
    cur.execute(f"INSERT INTO {table_name} VALUES(%s,%s); ", (q_id, choice))
    db.commit()
    return print(f"The values '{q_id}', '{choice}', was successfully inserted!")


def insert_quizzes(quiz_id):
    table_name = "quizzes"
    cur = db.cursor()
    cur.execute("INSERT INTO quizzes(quiz_id) VALUES(%s);", (quiz_id))
    db.commit()
    return print(f"The values '{quiz_id}', was successfully inserted!")


# query functions
# Testing query functionality
def query_entire_table(table):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {table};")
    result = list(cur.fetchall())
    # print(f"First Entry fetch: {list(result[1])}")
    db.commit()
    return print(f"Query Results: {result}")


# grab list of choices for variable question
def query_choices(q_id):
    table_name = "choices"
    cur = db.cursor()
    cur.execute(f"SELECT choice FROM {table_name} WHERE q_id ='{q_id}';")
    result = list(cur.fetchall())
    # print(f"First Entry fetch: {list(result[1])}")
    db.commit()
    # return print(f"{q_id} Results: {result}")
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


def query_question(q_id):
    cur = db.cursor()
    cur.execute(f"SELECT q FROM questions WHERE q_id ='{q_id}';")
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


def query_ans(q_id):
    cur = db.cursor()
    cur.execute(f"SELECT ans FROM questions WHERE q_id ='{q_id}';")
    result = list(cur.fetchall())
    returnlist = []
    for i in range(len(result)):
        returnlist.append(result[i][0])
    return returnlist


## Creating tables
# print("creating tables")
# delete_table("questions")
# delete_table("choices")
create_questions_table()
create_choices_table()
# create_quizzes_table()
# create_results_table()
# print(f"Created Table List: {list_tables(db_table = db_name)}\n")


# ## Inserting questions
# print("inserting questions")
# insert_questions("quiz1", "q1", "What is 2+2?", "4")
# insert_questions("quiz1", "q2", "What belongs to AWS?", "EC2")

# #There is a bug with inserting quiz_ids. may need to remake this module
# ## Inserting quizzes
# print("inserting quiz")
# insert_quizzes("quiz1")

# # Insert values to choices
# print("inserting choices")
# insert_choice("q1", "2")
# insert_choice("q1", "4")
# insert_choice("q1", "6")
# insert_choice("q1", "0")
# insert_choice("q2", "S33")
# insert_choice("q2", "Google")
# insert_choice("q2", "EC2")


# ## Query an entire table
# query_entire_table("questions")
# query_entire_table("choices")
# query_entire_table("quizzes")
# query_entire_table("results")

# ## Query all choices on a specific question
# query_choices("q1")
# query_choices("q2")

# creating dictionary output for html
def grab_question(q_num):
    out = {"question": None, "choices": None, "ans": None}
    out["question"] = query_question(q_num)
    out["choices"] = query_choices(q_num)
    out["ans"] = query_ans(q_num)
    return out


# print(grab_question("q1"))

## Delete a table
# delete_table("questions")
# delete_table("choices")
# delete_table("quizzes")
# delete_table("results")
# print(f"Final List: {list_tables(db_table = db_name)}\n")
