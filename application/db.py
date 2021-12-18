import MySQLdb

# connection
db = MySQLdb.connect(
    host="database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com",  # your host, usually localhost
    user="admin",  # your username
    passwd="KuraLabs#123",  # your password
    db="final",
)  # name of the data base


def list_tables(db_table):
    cur = db.cursor()
    cur.execute(f"SHOW TABLES FROM {db_table};")
    result = cur.fetchall()
    return result


def create_table(new_name):
    cur = db.cursor()
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {new_name} (quiz_id VARCHAR(20) NOT NULL, question_number INT NOT NULL, choice_a TEXT NOT NULL, choice_b TEXT NOT NULL, choice_c TEXT NOT NULL, choice_d TEXT NOT NULL);"
    )
    result = cur.fetchall()
    return print(f"The table '{new_name}' was successfully created!")


def delete_table(target):
    cur = db.cursor()
    cur.execute(f"DROP TABLE {target};")
    result = cur.fetchall()
    return print(f"The table '{target}' was successfully deleted!")

#create questions table
def create_questions():
    cur.execute(f"CREATE TABLE IF NOT EXISTS questions (quiz_id VARCHAR(20) NOT NULL, q_id VARCHAR(20) NOT NULL, q TEXT NOT NULL, ans VARCHAR(20) NOT NULL);")
    return print (f"The table 'questions' was successfully created!")

#create choices table
def create_choices():
    cur.execute(f"CREATE TABLE IF NOT EXISTS choices ( q_id VARCHAR(20) NOT NULL, choice VARCHAR(20) NOT NULL);")
    return print (f"The table 'choices' was successfully created!")

#create quiz table
def create_quizes():
    cur.execute(f"CREATE TABLE IF NOT EXISTS quizes (quiz_id VARCHAR(20) NOT NULL);")
    return print (f"The table 'quizes' was successfully created!")

#create results table
def create_results():
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS results (quiz_id varchar(10) NOT NULL, a varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL, b varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, c varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, d varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL, grade float DEFAULT NULL);"
    )

    return print (f"The table 'results' was successfully created!")

def insert_q(quiz_id, q_id, q, ans):
    cur.execute("INSERT INTO questions VALUES(%s,%s,%s,%s);",(quiz_id, q_id, q, ans))
    print("successful insert")

def insert_choice(q_id,choice):
    cur.execute("INSERT INTO choices VALUES(%s,%s); ",(q_id,choice))
    print("successful insert")

def insert_quiz(quiz_id):
    cur.execute("INSERT INTO quizes VALUES(%s); ",(quiz_id))
    print("successful insert")

def query_data(table):
    cur.execute(f"SELECT*FROM {table};")
    result = cur.fetchall()
    print(result)

db.commit()

create_questions()
create_choices()
create_quizes()

insert_q("quiz1","q1","What is 2+2?","4")
insert_q("quiz1", "q2", "What belongs to AWS?", "EC2")

#insert_quiz("quiz1")

insert_choice("q1", "4")
insert_choice("q1", "5")
insert_choice("q1", "6")
insert_choice("q2", "S33")
insert_choice("q2", "Google")
insert_choice("q2", "EC2")

query_data("choices")
