import sqlite3

DB_NAME = "card_new.db"

def get_connection():
    con = sqlite3.connect(DB_NAME)
    return con

def create_card_table():
    con = get_connection()
    create_table = """CREATE TABLE CARD_FORMAT(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UUID VARCHAR(400) NOT NULL
    )"""
    con.execute(create_table)
    con.close()

card_info = "B4 70 64"

def insert_card_table(card):
    add_data_stmt = '''INSERT INTO CARD_FORMAT(UUID) VALUES (?)'''
    con = get_connection()
    con.execute(add_data_stmt, (card,))
    con.commit()
    con.close()

# con = get_connection()
# create_card_table()

# insert_card_table(card_info)

def read_from_file(uuid):
    select_stmt = '''SELECT UUID FROM CARD_FORMAT WHERE UUID=?'''
    con = get_connection()
    cur = con.cursor()
    cur.execute(select_stmt, (uuid,))
    rows = cur.fetchall()
    con.close()
    if len(rows) == 0:
        print(f"[py:log] UUID not found: {uuid}")
        return False
    else:
        print(f"[py:log] UUID found: {uuid}")
        return True

read_from_file(card_info)