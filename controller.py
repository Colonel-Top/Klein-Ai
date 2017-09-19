import os
import re
import random
import fileinput
from datetime import datetime
import json
import time
import sys
from random import randint
import MySQLdb
import win32com.client

t2s = ''
if len(sys.argv) < 2:
    print("argument not found terminated")
    sys.exit(0)  #
# If no argument terminated then

input = sys.argv[1]
db = MySQLdb.connect("colonel-tech.com", "parton", "^)!)^!#$)!", "parton")
cur = db.cursor()

if '!cregisterbike' in input:
    input = input.replace('!cregisterbike', '')
    input = input.replace('unlock', '')
    input = input.replace('code', '')
    input = input.replace('with', '')
    input = input.replace(' ', '')
    input = input.replace('an', '')
    input = input.replace('a', '')
    key = input[0:4]
    head = input[5:]
    try:
        cur = db.cursor()
        last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s", ([head])))
        row = cur.fetchone()
        if row:
            newkey = str(row[1])
            t2s += str("Already Exits OFO !")
            t2s += str(head)
            t2s += str("Unlock code is " + str(row[2]))
        else:
            last_result = (cur.execute("SELECT No FROM `record` ORDER BY No DESC LIMIT 1"))
            row = cur.fetchone()
            tmo = int(row[0]) + 1
            cur.execute("INSERT INTO record (No,bikeno,unlockcode) VALUES (%s,%s,%s)", (tmo, head, key))
            db.commit()
            last_result = (cur.execute("SELECT * FROM `record` ORDER BY No DESC LIMIT 1"))
            row = cur.fetchone()
            t2s += str("Added OFO Bike " + str(row[1]) + " as unlock code " + str(row[2]))
    except Exception as e:
        print(e)
        db.rollback()
elif '!cdeletebike' in input:
    input = input.replace('!cdeletebike', '')
    input = input.replace(' ', '')
    try:
        cur = db.cursor()
        t2s += str('Deleting OFO')
        last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s ", ([input])))
        row = cur.fetchone()
        if row:
            t2s += str("O F O Bike ")
            t2s += str(str(row[0]))
            t2s += str("Deleted")
            cur.execute("DELETE FROM record WHERE `bikeno` = %s ", ([input]))
            db.commit()
        else:
            result = "Non OFO Number like what you've entered"
    except Exception as e:
        print(e)
        t2s += str("Faild to Delete OFO")
        db.rollback()
elif '!camountofbike' in input:
    try:
        cur = db.cursor()
        last_result = (cur.execute("SELECT No FROM `record` ORDER BY No DESC LIMIT 1"))
        row = cur.fetchone()
        tmo = int(row[0])
        status = 1
        if row:
            t2s += str("Now Bike in database amount is " + str(tmo) + " bikes")
        else:
            t2s += str("Not Found Database Error")
    except Exception as e:
        print(e)
elif '!csearchbike' in input:
    input = input.replace('!csearchbike', '')
    try:
        input = input.replace('!csearchbike', '')
        input = input.replace('unlock', '')
        input = input.replace('code', '')
        input = input.replace('with', '')
        input = input.replace(' ', '')
        input = input.replace('an', '')
        input = input.replace('a', '')
        cur = db.cursor()
        last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s", ([input])))
        row = cur.fetchone()
        if row:
            t2s += str("OFO Bike ")
            t2s += str(str(row[1]))
            t2s += str("Unlock Code ")
            t2s += str(str(row[2]))
        else:
            t2s += str("OFO Bike Not Found")
    except Exception as e:
        print(e)
elif '!ccloseprogram' in input:
    t2s = '!shutdown'
elif '!keytyping' in input:
    input = input.replace("!keytyping",'')
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys(input)
else:
    t2s = 'nothing'
print(t2s)
