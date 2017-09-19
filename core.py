#!/usr/bin/python
# -*-coding: utf-8 -*-
# -*- coding: utf-8 -*-

import random
from datetime import datetime
import sys
import subprocess
import MySQLdb


# Function Define
def find_str(s, char):
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index + len(char)] == char:
                    return index

            index += 1
    return -1


def print_done():
    answerdone = ['Progress Successfully', 'Successfully Command', 'Perfectly Finish']
    result = random.choice(answerdone)
    print(result)


# Function Define

if len(sys.argv) < 2:
    print("argument not found terminated")
    sys.exit(0)  # If no argument terminated then
mode = 3

# database connect
db = MySQLdb.connect("colonel-tech.com", "parton", "^)!)^!#$)!", "parton")
cur = db.cursor()
# database connect


# define input argument
input = sys.argv[1]

# define input argument
t2s = ''
status = 0
NAME = "chloe"

if status == 0:
    input = input.lower()
    if 'command' in input and NAME in input:
        status = 1
        input = input.replace('command', '')
        # Going add command
        if 'add' in input:
            input = input.replace('add', '')
            pos_endadd = find_str(input, "as")
            command_add = input[:pos_endadd]
            input = input.replace(command_add, "")
            input = input.replace("as", "")
            input = input.replace(" ", "")
            command_out = "!c" + input
            time = datetime.now().strftime('%H:%M:%S')
            date = datetime.now().strftime('%Y-%m-%d')
            try:
                cur.execute(
                    "INSERT INTO command (cmd_in,cmd_out,device_mode,time_add,date_added) VALUES (%s,%s,%s,%s,%s)",
                    (command_add, command_out, mode, time, date))
                db.commit()
                print_done()
            except Exception as e:
                t2s += str("SQL Query Error Add Command")
                # t2s += str(e)
                db.rollback()
        elif 'destroy' in input:
            input = input.replace('destroy', '')
            input = input.replace(' ', '')
            try:
                strto = "DELETE FROM `command` WHERE cmd_in= "+ input
                cur.execute(strto, str(input))
                print (strto)
                db.commit()
                print_done()
            except Exception as e:
                t2s += str("Command Not Found")
                # t2s += str(e)
                db.rollback()
        elif 'replace' in input:
            input = input.replace('replace', '')
            input = input.replace("!c", "")
            pos_endadd = find_str(input, "as")
            old_cmd = input[:pos_endadd]
            input = input[pos_endadd + 1:]
            input = input.replace("as", "")
            new = "!c" + input
            time = datetime.now().strftime('%H:%M:%S')
            date = datetime.now().strftime('%Y-%m-%d')
            try:
                cur.execute("UPDATE command SET `cmd_out`=%s,`time_add`=%s,`date_added`=%s WHERE `cmd_in`=%s",
                            (new, time, date, old_cmd))
                db.commit()
                print_done()
            except Exception as e:
                t2s += str("SQL Query Error Replace Command")
                # t2s += str(e)
                db.rollback()
    elif NAME in input:
        input = input.replace(NAME, "")
        if input:
            chk_ary = input.split()
            checkstr = "SELECT * FROM command WHERE `cmd_in` LIKE "

            size = len(chk_ary)
            i = 0
            for tmp in chk_ary:
                checkstr += "\'%" + tmp + "%\'"
                if i + 1 != int(size):
                    checkstr += " OR `cmd_in` LIKE "
                i += 1
            checkstr += ""
            try:
                cur.execute(checkstr)
                state = cur.fetchone()
                if (state):
                    input = input.replace(str(state[1]), '')
                    callstr = "python controller.py " + "\"" + str(state[2]) + input + "\""
                    callback = subprocess.Popen(callstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    t2s = str(callback.communicate()[0])
                else:
                    t2s = ''
            except Exception as e:
                print(e)
                print(checkstr)
t2s = t2s.replace("\\r", '')
t2s = t2s.replace("\'b\'", '')
t2s = t2s.replace("b\'", '')
t2s = t2s.replace("b\"", '')
t2s = t2s.replace("\'", '')
t2s = t2s.replace("\\n", '')
t2s = t2s.replace("\"", '')
print(t2s)
