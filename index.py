#!/usr/bin/env python3

import serial
import sqlite3

DB_NAME = "card_new.db"

def get_connection():
    con = sqlite3.connect(DB_NAME)
    return con

ser = serial.Serial(
    port="/dev/ttyACM0",  # plz change this according to your port number
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

ser.flush()


def create_card_table():
    con = get_connection()
    create_table = """CREATE TABLE CARD_FORMAT(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UUID VARCHAR(400) NOT NULL
    )"""
    con.execute(create_table)
    con.close()
    
def populate_DB(card: str):
    con = get_connection()
    query = """INSERT INTO CARD_FORMAT(UUID) VALUES(?)"""
    con.execute(query, (card,))
    con.commit()
    con.close()
    print("DONEEEEEEEEEEe")


def readFile(uuid):
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


if __name__ == "__main__":
    # populate_DB("30 18 CB 73")
    # exit(0)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").rstrip()
            print(line)
            if line[0:14] == "[check-access]":
                print("Checking Access")
                isAllowed = readFile(line[14:].rstrip().lstrip())
                response = "granted" if isAllowed else "denied"
                ser.write(response.encode())
