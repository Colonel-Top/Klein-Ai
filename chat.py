#!/usr/bin/python
# -*-coding: utf-8 -*-
# -*- coding: utf-8 -*-
import gspread
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

if len(sys.argv) < 2:
    sys.exit(0)
#print("Done")
#message = "Debugging "
message = sys.argv[1]
#message = message.encode().decode("cp874")
#print (message)
now = datetime.now()
result = ''
from oauth2client.service_account import ServiceAccountCredentials
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


line_bot_api = LineBotApi('QWiSqwAAs1/FyPo+Rt+jKoxjjK+LbkQ1pC1zsmCO9s5g2YO9EFUsSKO90ABQpc8h31iecVkjMsG3IZ2J9xCcS5pHL0ph8nc81PIM+gJEFzkJpHIRBWiJQl7sh6dOuuApuPMC+aj1HjkT5iaHCXDJ5AdB04t89/1O/w1cDnyilFU=')
fo = open('control','r+')
strws = fo.read()
destinations =''
if (strws == '1'):
    destinations = 'C5c90aa2273d7093f30ca08a91066cd78'
elif (strws == '2'):
    destinations = 'Cacab1833e4e7009f49c15779e645f66c'
            
destination = 'Ufb00beda08083bcf402fbd2160b75574'
fo.close()
status = 0
group = 'C5c90aa2273d7093f30ca08a91066cd78'
# print ('Google API Connected')
def Login():
    #print ('Messenger API Connected')
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
    worksheet = sh.worksheet('Account')
    #print ('Google API Connected')
def OFOSheetLogin():
    #print ('Messenger API Connected')
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1uk5E7JUQ_75p-pi3FOsqHwgWDGpZhg7_hYf9rfrsrAc')
    worksheet = sh.worksheet('MainOFO')
    #print ('Google API Connected')
scope = ['https://spreadsheets.google.com/feeds']

bot_status = 0
bot_mode = 0
# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี', 'hello', 'hi ', 'greetings', 'sup', 'whats up', 're you here','หวัดดี']
chloeset = ['Chloe','อี้','โคล','chloe','โคอี']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?',
              'Always here']
backasgre_w = ['Thx', 'Thank', 'ขอบคุณโคลอี้', 'appreciate', 'ขอบใจโคลอี้','แต้งโคลอี้']
backasgre_f = ['Your welcome', 'With Pleasure :)', 'with Appreciated', 'Ya', 'Okay ^^', 'Welcome', 'Never mind :)']
menu_cmd = ['pen menu', 'pen Menu', 'เปิดเมนู', 'เรียกเมนู', 'show function', 'Show function', 'Show Menu', 'show menu',
            'Show menu']
simq_ask = ['ho are you', 'hat do you do', 'ho is your boss', 'ho am i', 'ell me a joke', 'ell me some joke','โคลอี้จ๋า','ถามได้ตอบได้','งอะแหละ','โบ้ะ','โบ๊ะ','ตึ่งโป้ะ','ตึ่งโปะ','ตึ่งโป๊ะ','อมึงแหละ','ตึงโป','โนว','ถามอะไรตอบได้','ด่ามึงอ','แกนั่นแหละ']
simq_ans = ['I am Chloe The Secretary of Colonel',
            'I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys', 'My Boss or my master is Colonel',
            'Some Human in this world', 'Joke ? google it :)', 'Ahh Nope','จ๋า ?','ได้','ตะลึ่งตึ่งโป้ะ','โพ่ง','โพ่ง','พ่าง','พ่าง','พ่าง','ตะลึงตึ่งโป้ะ','พ่าง','Noooo','ไมได้ แบร่','ตะลึงตึ่งโป๊ะ!','ตะลึงตึ่งโป๊ะ!']
randomfive = ['555+','5555+','55555+','5555+','55555+','555555+','55555+','555555+','5555555+','5555+','55555+','555555+','55555+',
'555555+','5555555+','555555+','5555555+','55555555+','55555+','555555+','5555555+','555555+','5555555+','55555555+','5555555+','55555555+','555555555+',]
bank_ask = ['eport accounts', 'ccount reports', 'om engr account', 'pdate account', 'heck amout account',
            'heck amout in account']
bank_ans = ['โอเคจ้า จะทำการอัพเดตให้เดี๋ยวนี้เลย', 'จ้า กำลังอัพเดตให้ละน้า', 'ได้เลยจ้า', 'ได้เลยจ้า แปปเดียวก็เสร็จละ',
            'ค่ะ ทำการตัดดอกเบี้ยทันทีค่ะ', 'ไดเลยจ้า ^^']
morning = ['Good morning','อรุณสวัสดิ์','สวัสดีตอนเช้า','กู้ดมอร์นิ่ง','goodmorning','อรุนสวัส','อรุณสวัส','good morning']
afternoon = ['Good afternoon','สวัสดีตอนบ่าย','กู้ดอาฟเตอร์นูนค้าาา','goodafternoon ^^','good afternoon','Goodafternoon']
night = ['Goodnight','Good night','ราตรีสวัสดิ','กู้ดไนท์','ฝันดี','อย่าลืมห่มผ้านะ','ราตรีสวัสดิ์','อากาศเปลี่ยนแปลงบ่อยดูแลสุขภาพนะ']
impressive_ask = ['สู้ๆนะ ^^','พรุ่งนี้ยังมีเสมอ สู้ๆจ้า','สู้ๆ :)','ชีวิตยังต้องเดินต่อไป สู้ๆนะ :)','คนเราพลาดกันได้ เป็นกำลังใจให้นะ','เป็นกำลังใจให้นะ สู้ๆ','ผ่านมันไปให้ได้ สู้ๆ ^^','ท้อได้ถอยได้ แต่ต้องตั้งหลักให้ได้แล้วสู้ต่อไป ^^','ดวงตะวันแม้ลับขอบฟ้ายังหวนคืนมาในวันฟ้าใหม่ ^^','สิ่งที่ผันผ่านคือกำลังใจ','แม้พายุโหมโถมชีวิตแรงเพียงใดแค่ก้าวต่อไปเดี๋ยวก็ถึงปลาบทาง','หากยังมัวอยู่เฉย ไฉนเลยจะถึงจุดหมาย :)','เจอขวากหนามจะต้องไม่ท้อ ต้องก้าวเดินต่อกว่าจะถึงจุดหมาย :)','ประสบการณ์สร้างคน อดทนแล้วสร้างงาน']
getint = ['hloe get interest now','โคลอี้ตัดดอกเบี้ย','ตัดดอกเบี้ยสิ']
# execfile('timeahead.py')
tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you', 'Yes, wait a second', 'Let me work on it', 'Here we go',
               'Alright here is it', 'Ya this one ^^']
# Class def
reinsult = ['กะหรี','กระหรี','สัส','สาส','บ้า','เวร','สาสสสส','สาดดด','ผี']
isinsult = '1'
president = ['ท้อ','ท่อ','ทอ','ท๊อ','ท๋อ','ปธ','ประ','ป่ระ','ปร่ะ','ป่ร่ะ','ปะ','ป่ะ','ป้ะ','ป๊ะ','ป๋ะ','ปท','พรหม','พรม','สุร','นท์','ทร์','พุท','พุธ','รรม','วงศ','วงส','วงษ','เมด','เม่ด','ป.ธ','ป,ธ','ป.ท','ปท','ป,ท','โคล','โคโ','โคอ','ท็อ','top','toop','เฮดภาค','แกนภาค','หัวภาค','ภาคคอม','ปิ่น','pin','Pin','PIN']
special = ['!','@','#','$','$','^','&','*','(',')','_','+','=','-','.',',','/','\\',' ']
whynot = ['ไม่น่าเชื่อถือพอค่ะ','ไม่น่ารักพอค่ะ','ไม่ดูดีพอค่ะ','ไม่อยากเชื่อค่ะ','คุณไม่ได้ผ่านเข้ารอบค่ะ','คุณน่ารักเกินไปค่ะ','คุณดูดีมากเกินไปค่ะ']
for tmp in president:
    if tmp in message:
        isinsult = '0'
# if you are not the author, echo
if 'ตัวอย่าง' in message :
	status = 1
# result = result)
# result =  bot_mode)
# result = bot_status)
# result = status)
# result = '-')
if status == 0:
    if 'วดฟ' in message:
        tmp = message
        try:
            filternumber = int(filter(str.isdigit,tmp))
        except:
            filternumber = 0
        filternumber +=1
        result = "วดฟ+"+str(filternumber)
        status = 1
    elif 'wtf' in message:
        tmp = message
        try:
            filternumber = int(filter(str.isdigit,tmp))
        except:
            filternumber = 0
        filternumber +=1
        result = "wtf+"+str(filternumber)
        status = 1
if status == 0:
    if '#$' in message:
        tmpo = message.replace('#$','')
        line_bot_api.push_message(destinations, TextSendMessage(tmpo))
        status = 1
if status == 0:
    if '/*-+' in message:
        tmpo = message.replace('/*-+','')
        line_bot_api.push_message('Ce76b2b3eaa43ddf57e5e05f940ad53fc', TextSendMessage(tmpo))
        status = 1
if status == 0:
   if 'กี่โมงแล้ว' in message:
       if 'โคลอี้' in message:
           result = "ขณะนี้เวลา: "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+ " ค่ะ"
           status = 1
if status == 0 :
    if 'โพ่ง' in message:
        result = message.replace('โพ่ง','พ่อง')
        status = 1
    if 'พ่าง' in message:
        result = message.replace('พ่าง','บ้านบึ้ม')
        status = 1
    if 'บ้านบึ้ม' in message:
        result = message.replace('บ้านบึ้ม','บึ้มพ่อง')
        status = 1
    if 'ฟวย' in message:
        result = 'Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas~'
        status = 1
    if 'ด่า'in message:
        if 'สามช่า' in message:
            result = 'ฟวย ฟวยๆ ฟวย ฟวย'
            status = 1
        if 'อจ' in message:
            result = ''
            status = 1
        if 'อาจา' in message :
            result = ''
            status = 1
    if 'กำลังใจ' in message :
        if 'ขอ' in message or 'ให้' in message:
            result = random.choice(impressive_ask)
            status = 1
    for tmp in morning:
        if tmp in message:
            result = random.choice(morning)
            result = result + " ค่ะ"
            status = 1
    for tmp in afternoon:
        if tmp in message:
            result = random.choice(afternoon)
            result = result + " ค่ะ"
            status = 1
    for tmp in night:
        if tmp in message:
            result = random.choice(night)
            result = result + " ค่ะ"
            status = 1
        
if status == 0:
    if 'เพิ่มการแจ้งเตือน:' in message:
        try:
            tmpgo = message
            message = message.replace('เพิ่มการแจ้งเตือน:','')
            #print(message+'done')
            gdate = message[0:10]
            jobhour = message[11:13]
            jobmin = message[14:16]
            content = message[11:]
            print('เพิ่มการแจ้งเตือน')
            print (content)
            # content.encode('utf-8')
            fo = open(gdate, 'a')
            fo.write(content + '\n')
            fo.close()
            fo = open('serverdate', 'a')
            fo.write(gdate + ',' + jobhour + ',' + jobmin + '\n')
            fo.close()
            result = 'เพิ่มตารางงาน,นัดหมายเรียบร้อยค่ะ'
            line_bot_api.push_message(destination, TextSendMessage(tmpgo))
        except Exception as e:
            print( e)
        bot_mode = 0
        bot_status = 0
        status = 1
if bot_mode == 2 and bot_status == 1 and status == 0:
    try:
        linetoremove = int(message[0])
        gdate = (now.strftime('%d-%m-%Y'))
        f = open(gdate, 'r+')
        d = f.readlines()
        tmpstring = ''
        for line in d:
            if line != linetoremove - 1:
                tmpstring += line
        f.close()
        os.remove(gdate)
        fo = open(gdate, 'a')
        fo.write(tmpstring)
        fo.close()
        result = 'ลบตารางงานดังกล่าวเรียบร้อย'
    except Exception as e:
        result = e
        result = 'การลบตารางเวลาล้มเหลว'
    bot_mode = 0
    bot_status = 0
    status = 1
if bot_status == 0 and status == 0:
    '''if 'a' in message:
        bot_mode = 1
        result = 'เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ \n\n31-12-2017:22:00:เนื้อหางาน'
        status = 1
    if 'A' in message:
        bot_mode = 1
        result = 'เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ \n\n31-12-2017:22:00:เนื้อหางาน'
        status = 1'''
    if 'รายการแจ้งเตือนวันนี้' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            result = 'รายการแจ้งเตือนวันนี้\n'+gdate +'\n'
            fo = open(gdate, "r+")
            for lines in fo:
            #print (lines)
                if '*' not in lines and '$' not in lines:
                    result += lines
                        # Close opend file
            fo.close()
            # Close opend file
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_status = 0
        bot_mode = 0
        status = 1
    if 'รายการแจ้งเตือนวันพรุ่งนี้' in message:
        try:
            gdate = str(now.day+1)+str(now.month)+str(now.year)
            # Open a file
            result = 'รายการแจ้งเตือนวันพรุ่งนี้\n'+gdate +'\n'
            fo = open(gdate, "r+")
            for lines in fo:
            #print (lines)
                if '*' not in lines and '$' not in lines:
                                #if str(curmin) in lines:
                    result += lines
                        # Close opend file
            fo.close()
            # Close opend file
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_status = 0
        bot_mode = 0
        status = 1
'''
    if 'c' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n' + gdate +'\n' + strws + '\nกรุณาใส่เลขหัวข้องานที่ต้องการจะลยเช่น 3'
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_mode = 2
        bot_status = 1
        status = 1
    if 'C' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n' + gdate+'\n' + strws + '\nกรุณาใส่เลขหัวข้องานที่ต้องการจะลยเช่น 3'
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_mode = 2
        bot_status = 1
        status = 1
    if 'D' in message:
        bot_mode = 0
        bot_status = 0
        status = 1
    if 'd' in message:
        bot_mode = 0
        bot_status = 0
        status = 1'''
if status == 0:
    for tmp in tellasc_cmd:
        if tmp in message:
            going = tmp.replace('tell all associate', '')
            stringtosend = 'result From Colonel : '
            stringtosend += strs(going)
            result = random.choice(tellasc_ans)
            # self.send(100002210119100,'result From Colonel : ' + going) #Aomsin
            # self.send(100001717587402,'result From Colonel : ' + going) #Beer
            # self.send(100000337186822,'result From Colonel : ' + going) #Pond
            result = stringtosend  # me
            status = 1
if status == 0:
    for tmp in greeting_w:
        if tmp in message:
            for asker in chloeset:
                if asker in message:
                    result = random.choice(greeting_f)
                    status = 1
if status == 0:
    for tmp in menu_cmd:
        if tmp in message:
            result = 'กรุณาเลือกฟังก์ชัน\n'+'a.เพิ่มงาน,ตารางนัดหมาย\nb.ตรวจสอบตารางเวลางาน\nc.ลบตารางเวลานัดหมาย\nd.เพื่อย้อนกลับ/ยกเลิก'
            bot_status = 1
            status = 1
if status == 0:
    if 'Ok' in message:
        result = '^^'
        status = 1
    elif 'ok' in message:
        result = '^^'
        status = 1
if status == 0:
    for tmp in getint:
        if tmp in message:
            scope = ['https://spreadsheets.google.com/feeds']
            result = random.choice(bank_ans)
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet('Account')
            cell = worksheet.acell('U31').value
            cell = cell.encode('utf-8')
            monthcell = now.month
            monthcell += 9
            # onthcell += 10
            for row in range(2, 31):  # Must be 31 in col or last parameter
                peruser = 0
                for col in range(8, 20):
                    tmp = worksheet.cell(row, col).value
                    #print(tmp)
                    if (tmp == '0'):
                        peruser += 1
                # print('Done Per loop')
                # print (peruser)
                if peruser >= 2 and worksheet.cell(row, monthcell).value == '':
                    interest = int(worksheet.cell(row, 22).value)
                    interest += 1
                # print (interest)
                    worksheet.update_cell(row, 22, interest)
                if worksheet.cell(row, monthcell).value == '':
                    worksheet.update_cell(row, monthcell, 0)
                if row == 8:
                    #print('Skip Safe')
                    continue
            status = 1

if status == 0:
    for tmp in backasgre_w:
        if tmp in message:
            result = random.choice(backasgre_f)
            status = 1
if status == 0:
    for tmp in bank_ask:
        if tmp in message:
            scope = ['https://spreadsheets.google.com/feeds']
            result = random.choice(bank_ans)
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet('Account')
            cell = worksheet.acell('U31').value
            cellavai = worksheet.acell('U32').value
            sendstr = 'ยอดรายรับ : '
            sendstr = sendstr + str(cell) + '\n' + 'ยอดพึงจ่ายได้ : ' + str(cellavai)
            result = sendstr
            status = 1
            # if status == 0:
            # result = "Sorry I don't know that \nYou can try: \nopen menu \nshow menu \nเรียกเมนู \nเปิดเมนู \nshow function"
if status == 0:
    if 'ขอเบอ' in message:
        if True:
            scope = ['https://spreadsheets.google.com/feeds']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
            worksheet = sh.worksheet('Sheet1')
            for row in range(2, 34):  # Must be 31 in col or last parameter
                tmp = ''
                tmp = (worksheet.cell(row, 6).value)
                tmp = tmp.encode('utf-8')
                if (tmp in message):
                    answer = str(worksheet.cell(row,7).value)
                    result += 'เบอร์'+ tmp +': ' + answer +'\n'
                    status =1
            if 'เมดี้' in message:
                result =  'เบอร์เมดี้: 09498959xx'
            status = 1
if status == 0:
    if 'ขอเลขนศ' in message:
  	    scope = ['https://spreadsheets.google.com/feeds']
  	    credentials = ServiceAccountCredentials.from_json_keyfile_name('ofocode.json', scope)
  	    gc = gspread.authorize(credentials)
  	    sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
  	    worksheet = sh.worksheet('Sheet1')
  	    for row in range(2, 34):  # Must be 31 in col or last parameter
  	      peruser = 0
  	      tmp = ''
  	      tmp = (worksheet.cell(row, 6).value)
  	      tmp = tmp.encode('utf-8')
  	      if (tmp in message):
  	        answer = str(worksheet.cell(row,2).value)
  	        result += 'เลขรหัสนศ. '+ tmp +': ' + answer+'\n'
  	        status = 1
		#break
  	    if 'เมดี้' in message:
                result =  'ไม่ให้ค่ะ'
                status = 1
if status == 0:
    if 'ofohelp' in message:
        result = 'OFO Shortcut Helper\n\n- To Register new ofo use: ofoa1234,10102\nWhere 1234 is Lock Code and 10102 is Bike Number usage: ofoa[pass][bike]\n-To find OFO Unlock Code use: ofo10102\nWhere 10102 is bike number usage: ofo[bike]\n-This System Troll By me Chloe~\n\nEnjoy ez gg OFO'
        status = 1
    if 'Ofohelp' in message:
        result = 'OFO Shortcut Helper\n\n- To Register new ofo use: ofoa1234,10102\nWhere 1234 is Lock Code and 10102 is Bike Number usage: ofoa[pass][bike]\n-To find OFO Unlock Code use: ofo10102\nWhere 10102 is bike number usage: ofo[bike]\n-This System Troll By me Chloe~\n\nEnjoy ez gg OFO'
        status = 1
if status == 0:
    if 'update' == message:
        result = "Add new Note System to MYSQL Database improve speed"
        status = 1;
if status == 0:
	if 'anote,' in message:
		message = message.replace('anote,','')
		days = message[0:2]
		months = message[3:5]
		years = message[6:10]
		note = message[11:]
		db = MySQLdb.connect("localhost","ofousr","ofocode","note_db",8886)
		try:
			cur = db.cursor()
			stringdate = years + '-' +  months + '-' + days
			print('Adding Note ...')
			cur.execute("INSERT INTO mainnote (date,note) VALUES (%s,%s)", (stringdate, note))
			last_result = (cur.execute("SELECT `No` FROM `mainnote` ORDER BY No DESC LIMIT 1"))
			state = cur.fetchone()
			result = 'Added Note['+str(state[0])+']'+': ' + '\nDate: '+stringdate + '\nNote: ' + note
			db.commit()
		except Exception as e:
			print(e)
			print('Faild to Add Note')
			db.rollback()
		status = 1
if status == 0:
    if 'fnote,' in message:
        message = message.replace('fnote,','')
        db = MySQLdb.connect("localhost","ofousr","ofocode","note_db",8886)
        try:
            cur = db.cursor()
            print('Finding Note ...')
            message = "%" + message + "%"
            last_result = (cur.execute("SELECT * FROM `mainnote` WHERE `note` LIKE %s ", ([message])))
            state = cur.fetchall()
            if state:
                for row in state:
                    print( '\n======= N O T E ' + str(row[0]) + ' =======\n')
                    print( 'Note['+ str(row[0])+']'+': ' + '\nDate: '+ str(row[1]) + '\nNote: ' + str(row[2]))
                    print ( '\n========= [' + str(row[0]) + '] =========\n\n')
            else:
                result = "Non Note like what you've entered"
        except Exception as e:
            print('Faild to Find Note')
            print(e)
        status = 1
if status == 0:
    if 'cnote' in message:
        message = message.replace('cnote','')
        db = MySQLdb.connect("localhost","ofousr","ofocode","note_db",8886)
        try:
            cur = db.cursor()
            print('Calling Note ...')
            last_result = (cur.execute("SELECT * FROM `mainnote` WHERE `No` = %s",([message])))
            state = cur.fetchall()
            if state:
                for row in state:
                    print( '\n======= N O T E ' + str(row[0]) + ' =======\n')
                    print( 'Note['+ str(row[0])+']'+': ' + '\nDate: '+ str(row[1]) + '\nNote: ' + str(row[2]))
                    print ( '\n========= [' + str(row[0]) + '] =========\n\n')
            else:
                result = "Non Note Number what you've entered"
        except Exception as e:
            print('Faild to Call Note')
            print(e)
        status = 1
if status == 0:
    if 'lastnote' in message:
        message = message.replace('lastnote','')
        db = MySQLdb.connect("localhost","ofousr","ofocode","note_db",8886)
        try:
            cur = db.cursor()
            print('Calling Note ...')
            message = "%" + message + "%"
            last_result = (cur.execute("SELECT * FROM `mainnote` ORDER BY No DESC LIMIT 1"))
            state = cur.fetchone()
            if state:
                result = 'Last Note['+ str(state[0])+']'+': ' + '\nDate: '+ str(state[1]) + '\nNote: ' + str( state[2])
            else:
                result = "Non Lastnote like what you've entered"
        except Exception as e:
            print('Faild to Call Note')
            print(e)
if status == 0:
    if 'dnote,' in message:
        message = message.replace('dnote,','')
        db = MySQLdb.connect("localhost","ofousr","ofocode","note_db",8886)
        try:
            cur = db.cursor()
            print('Deleting Note ...')
            last_result = (cur.execute("SELECT * FROM `mainnote` WHERE `No` = %s ", ([message])))
            state = cur.fetchone()
            if state:
                result = 'Deleted Note['+ str(state[0])+']'+': ' + '\nDate: '+ str(state[1]) + '\nNote: ' +  str(state[2])
                cur.execute("DELETE FROM mainnote WHERE `No` = %s ", (message))
                db.commit()
            else:
                result = "Non Note like what you've entered"
        except Exception as e:
            print(e)
            print('Faild to Delete Note')
            db.rollback()
if status == 0:
    if  'Ofoa' in message :
        message = message.replace('Ofoa', '')
        key = message[0:4]
        head = message[5:]
        db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
        try:
            cur = db.cursor()
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s",([head])))
            row = cur.fetchone()
            if row:
                newkey = str(row[1])
                print ("Already Exits OFO !")
                print( '\n===== O F O B I K E ' + head + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n===== E X I S T S [' + str(row[1]) + '] ======\n\n')
            else:
                last_result = (cur.execute("SELECT No FROM `record` ORDER BY No DESC LIMIT 1"))
                row = cur.fetchone()
                tmo = int(row[0])+1
                cur.execute("INSERT INTO record (No,bikeno,unlockcode) VALUES (%s,%s,%s)", (tmo,head, key))
                db.commit()
                last_result = (cur.execute("SELECT * FROM `record` ORDER BY No DESC LIMIT 1"))
                row = cur.fetchone()
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n======= A D D [' + str(row[1]) + '] =======\n\n')
        except Exception as e:
            print(e)
            db.rollback()
if status == 0:
    if  'ofoa' in message :
        message = message.replace('ofoa', '')
        key = message[0:4]
        head = message[5:]
        db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
        try:
            cur = db.cursor()
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s",([head])))
            row = cur.fetchone()
            if row:
                newkey = str(row[1])
                print ("Already Exits OFO !")
                print( '\n===== O F O B I K E ' + head + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n===== E X I S T S [' + str(row[1]) + '] ======\n\n')
            else:
                last_result = (cur.execute("SELECT No FROM `record` ORDER BY No DESC LIMIT 1"))
                row = cur.fetchone()
                tmo = int(row[0])+1
                cur.execute("INSERT INTO record (No,bikeno,unlockcode) VALUES (%s,%s,%s)", (tmo,head, key))
                db.commit()
                last_result = (cur.execute("SELECT * FROM `record` ORDER BY No DESC LIMIT 1"))
                row = cur.fetchone()
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n======= A D D [' + str(row[1]) + '] =======\n\n')
        except Exception as e:
            print(e)
            db.rollback()
if status == 0:
    if 'อาจารย์ TU100' in message:
        print("อาจารย์สุขพัฒน์ คงเพ็ชร์ (อ.แนล)")
if status == 0:
    if 'Ofod' in message:
        message = message.replace('Ofod', '')
        db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
        try:
            cur = db.cursor()
            print('Deleting OFO ...')
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s ", ([message])))
            row = cur.fetchone()
            if row:
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Deleting Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n===== W R O N G S [' + str(row[1]) + '] ======\n\n')
                cur.execute("DELETE FROM record WHERE `bikeno` = %s ", ([message]))
                db.commit()
            else:
                result = "Non OFO Number like what you've entered"
        except Exception as e:
            print(e)
            print("Faild to Delete OFO")
            db.rollback()
if status == 0:
    if 'ofod' in message:
        message = message.replace('ofod', '')
        db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
        try:
            cur = db.cursor()
            print('Deleting OFO ...')
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s ", ([message])))
            row = cur.fetchone()
            if row:
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Deleting Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print ( '\n===== W R O N G S [' + str(row[1]) + '] ======\n\n')
                cur.execute("DELETE FROM record WHERE `bikeno` = %s ", ([message]))
                db.commit()
            else:
                result = "Non OFO Number like what you've entered"
        except Exception as e:
            print(e)
            print("Faild to Delete OFO")
            db.rollback()
if status == 0:
    if 'ofostats' in message:
        try:
            db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
            cur = db.cursor()
            last_result = (cur.execute("SELECT No FROM `record` ORDER BY No DESC LIMIT 1"))
            row = cur.fetchone()
            tmo = int(row[0])
            status = 1
            if row:
                print( '\n===== O F O B I K E ' + ' =====\n')
                print(   ' Current Number \n OFO in Database : \n                  '+str(tmo)+' Bikes\n')
                print( '===== [ ' + "S T A T S" + ' ] ======')
            else:
                print( '\n====== O F O B I K E '+' =====\n')
                print(   '   NO : '+message+' : DATA !!!!! \n')
                print( '====== [ ' + "E m p t y" + ' ] ======\n\n')
        except Exception as e:
            print (e)
if status == 0:
    if 'ofo' in message:
        message = message.replace('ofo', '')
        try:
            message = message.replace('ofo', '')
            db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
            cur = db.cursor()
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s", ([message])))
            row = cur.fetchone()
            if row:
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print( '\n========== [' + str(row[1]) + '] ==========')
            else:
                print( '\n====== O F O B I K E '+' =====\n')
                print(   '   NO : '+message+' : DATA RECORD \n')
                print( '====== [ ' + "E m p t y" + ' ] ======\n\n')
        except Exception as e:
            print (e)
if status == 0:
    if 'Ofo' in message:
        message = message.replace('Ofo', '')
        try:
            message = message.replace('ofo', '')
            db = MySQLdb.connect("localhost", "ofousr", "ofocode", "ofo_db",8886)
            cur = db.cursor()
            last_result = (cur.execute("SELECT * FROM `record` WHERE `bikeno` = %s", ([message])))
            row = cur.fetchone()
            if row:
                print( '\n===== O F O B I K E ' + str(row[1]) + ' =====\n')
                print( 'Record['+ str(row[0])+']'+': ' + '\nBike Number: '+ str(row[1]) + '\nBike Unlock Code : [ ' + str(row[2])+' ]')
                print( '\n========== [' + str(row[1]) + '] ==========')
            else:
                print( '\n====== O F O B I K E '+' =====\n')
                print(   '   NO : '+message+' : DATA RECORD \n')
                print( '====== [ ' + "E m p t y" + ' ] ======\n\n')
        except Exception as e:
            print (e)
if status == 0:
    if 'ขอรหัสนศ' in message:
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
        worksheet = sh.worksheet('Sheet1')
        for row in range(2, 34):
            tmp = ''
            tmp = (worksheet.cell(row, 6).value)
            tmp = tmp.encode('utf-8')
            if (tmp in message):
                answer = str(worksheet.cell(row,2).value)
                result += 'เลขรหัสนศ. '+ tmp +' : ' + answer+'\n'
                status = 1
            if 'เมดี้' in message:
                result =  'ไม่ให้ค่ะ'
                status = 1
insult = ['ด่าอิ','ด่าแม่ง','ด่าไอ','ด่ามัน','ด่าอีก','ด่าาแม่ง','ด่ามันสิ','ด่ามันซิ','ด่าต่อไป','ด่าอย่าหยุด','ด่าอี','ด่าอิ','ด่ามา']
care = ['โอเอ๋น้าาาา','โอเอ๋นาจา','ไม่เอาไม่เสียใจ','โอ๋ๆๆๆ','ไม่อาวๆไม่ร้องๆ อึ้บ','ไม่เศร้านะค่ะ ^^','ไม่เศร้าน้าาาา','อุอิๆ อึ้บๆ ไม่เศร้าน้าา']
prefixinsult = ['ไอ้','อี','อิ','ไอ']
reinsult2 = ['ผี','ผี','ดอก','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','บลิซซาร์ดไม่คว่ำถ้วย','แหวกกอหญ้า','บ้าห้าร้อยจำพวก','ปลวกใต้หลังคา','หน้าปลาจวด',
'บ้องกัญชา','ปลาไม่กินเบ็ด','เห็ดสามสี','อิเห็ดต้มยำ','อิเห็ดต้มยำ',
'กะโหลกซออู้','กู่ไม่กลับ','ตับย่างเกลือ',
'เชื้ออหิวาต์','ม้าขี้ครอก','หอกขึ้นสนิม','ขิมสายขาด',
'ชาติสุนัข','ตะหวักตะบวย','กล้วยตากแห้ง','แกงฟักทอง',
'คลองเจ็ดคด','ชะมดเช็ด','เกล็ดเต็มตัว','มั่วไม่รู้จบ',
'ศพขึ้นอืด','หืดขึ้นคอ','ปลาหมอแถกเหงือก','เผือกรมควัน',
'มันสำปะหลัง','โกดังเก็บศพ','กบผัดเผ็ด','เป็ดทอดกระเทียม',
'ดีไม่ห่างเหิน','เดินไม่ดูทาง','ก้างติดคอ','หม้อก้นทะลุ',
'หัว***','กระจาดปลาแห้ง',
'ปลาทูแม่กลอง','สององคต','หดหัวในกระฎอง','สมองเท่าเมล็ดถั่ว',
'ตัวกินไก่','ใจปลาซิว','หิวตลอดศก','ซกมกเป็นนิจสิน',
'หินใต้บาดาล','เพลงผิดคีย์','สีทาบ้าน',
'จานเปื้อนคราบ','แมลงสาบทรงเครื่อง','เปลืองข้าวสุก','กระปุกตังไฉ่',
'มารสังคม','ผ้าห่มสีซีด','ศพไม่ฉีดฟอร์มาลิน','กระถินริมรั้ว',
'บัวเต่าถุย','กุ๊ยไร้สังกัด','ผัดผักไฟแดง','แพนงกระดูกหมู',
'สาคูน้ำกะทิ','กะปิค้างคืน','หื่นเป็น...','ขวานผ่าซาก',
'กากสิ่งปฏิกูล','พะยูนตากแดด','แรดสองนอ','จอหนังตะลุง',
'ถุงสองใบ','ไข่ลูกเดียว','เคียวห่วยๆ','ถ้วยสังขยาบูด',
'กระต่ายขูดมะพร้าว','ชาวสวนทุเรียน','ตะเพียนหางยาว','ว่าวหางขาด',
'ฉลาดแต่เรื่องโง่','โมฆบุรุษ','มนุษย์สามานย์','เชี่ยวชาญแต่เรื่องชั่ว',
'แกงคั่วหอยขม','นิยมแต่เรื่องผิด','จิตวิปลาส','ทาสเงินตรา',
'ชฎายอดหัก','ไม้หลักปักขี้เลน','จิ้งเหลนหางไหม้','ตะไคร่ในท่อน้ำ',
'ดำตับเป็ด','พูดเท็จหน้าด้านๆ','คอห่านส้วมซึม','อึมครึมตลอดชาติ',
'หาดจอมเทียน','เชี่ยนตะบันหมาก','ปากปลากะโห้','โถส้วมสาธารณะ',
'กระบะใส่ขี้แมว','เรือแจวยี่สิบฝีพาย','ควายเขาหัก','ปลักโคลนเลน',
'ตาเถรตกใต้ถุน','เนรคุณแผ่นดินเกิด','ระเบิดแสวงเครื่อง','ครกกระเดื่องตำข้าว',
'มะพร้าวห้าวยัดปาก','สากกระเบือยัดก้น','คนไททิ้งแผ่นดิน',
'ไพร่เพื่อทัก','บักหำน้อย','กบฏต่อราชบัลลังก์','ลานจอดนกเอี้ยง']
member = ['ม่าน','ฟ้า','กิฟ','กิ้ฟ','กิ๊ฟ','ฟัน','หลิว','ชุน','ชุณ','คิตตี้','เฟิน','เฟิร์น','กู้ด','ไอซ์','ใหม่','ปริม','ช้าง','ทัก','บิ๋ม','ปิ่น','มีน','นอต','น็อต','มิ้นท์','ฟร้อง','ฟร็อง','ฟร๊อง','เพชร','ปาล์ม','พลอย','อาม','อาร์ม','อาท','แม็ค','แม็ก','พี่ฟา','พี่น้ำ','พี่จูน','ออมสิน','แพรว','มิน','มิ้น','คิตตี้','มาย','ปืน','พี่','พี','กาย','ออม','ภูมิ','เบียร์','เบีย','แนน','แฟง','จูน','เอิท','ออมสิน','ปอน','แมค','แมก','เจส','มุก','น้ำ','บูม',
          'นั้ม','ทัยรัตน','ภาสวิชญ์','พีมลทิพย์','วรเดช','หลิน','กิ้ก','เก่ง','นิค','ฟาโล','กิ๊ก','นิก','ฟาโร']
member2 = ['กุลณัฐ','ศิริรัตน์','กัญญาภรณ์','ปิยภพ',
'ธีรเมธ','วิศววิท','รัฐภูมิ','สุพิชฌาย์','ธัชเดช','นิรุชา','กัญญารัตน์','ชณิตา','สิรวิชญ์','ธนภัทร','บุญณัฐ','พรหมสุรินท์','กิตติคุณ',
'ภูริณัฐ','วราภรณ์','สหฤทัย','ศราวุธ','โฆษิต','ศตวรรษ','ฤทัยรัตน์','ภาสวิชญ์','พิมลทิพย์','วรเดช','ศุุภสิริ','สุนทรา','ศุภกิจพล','ธนพล','อรรถพล'
,'อาท','แม็ค','แม็ก','พี่ฟา','พี่น้ำ','พี่จูน','ออมสิน','แพรว','มิน','มิ้น','คิตตี้','มาย','ปืน','พี่','พี','กาย','ออม','ภูมิ','เบียร์','เบีย','แนน','แฟง','จูน','เอิท','ออมสิน','ปอน','แมค','แมก','เจส','มุก','น้ำ','บูม',
'นั้ม','ทัยรัตน','ภาสวิชญ์','พีมลทิพย์','วรเดช','หลิน','กิ้ก','เก่ง','นิค','ฟาโล','กิ๊ก','นิก','ฟาโร','ท้อป','ทอป','ท่อป','ท๊อป','ท้อป','ปธ','ป.ธ','เมดี้','top','ม่าน','ฟ้า','กิฟ','กิ้ฟ','กิ๊ฟ','ฟัน','หลิว','ชุน','ชุณ','คิตตี้','เฟิน','เฟิร์น','กู้ด','ไอซ์','ใหม่','ปริม','ช้าง','ทัก','บิ๋ม','ปิ่น','มีน','นอต','น็อต','มิ้นท์','ฟร้อง','ฟร็อง','ฟร๊อง','เพชร','ปาล์ม','พลอย','อาม','อาร์ม']
good = ['เก่งจัง','น่ารักกกก','ดูดีมากเลย','ชอบๆ น่ารักมาก','สุดยอดเลย','ทำได้ดีมากเลย','น่ารักมากเลย','ดูดีมาก']
toldme = ['บอกว่ากุ' , 'บอกว่าเรา' , 'บอกว่ากุ' , 'บอกเราว่า' , 'บอกเค้าว่า' , 'บอกว่าเรา','บอกสิว่าเรา','บอกเราสิว่า','บอกเราทีว่า','บอกทีว่าเรา']


if status == 0:
    for tmp in toldme:
        if tmp in message:
            if isinsult == '0':
                randarray = ['ไม่น่าเชื่อถือพอค่ะ','ไม่น่ารักพอค่ะ','ไม่ดูดีพอค่ะ','ไม่ได้ผ่านเข้ารอบค่ะ']
                result = 'ขอโทษค่ะไม่สามารถทำกรณีดังกล่าวได้เพราะคุณ'+random.choice(randarray)
                status = 1
            else:
                select = randint (0,3)
                if select == 0:
                    result = message.replace(tmp,"")
                    result += 'ก็ได้ค่ะ'
                    status = 1
                elif select == 1:
                    result = 'ไม่ค่ะ'
                    result += random.choice(whynot)
                    status = 1
                elif select == 2:
                    result = message.replace(tmp,"")
                    result += 'ค่ะ'
                    status = 1
                else:
                    result = message.replace(tmp,"")
                    result += 'ก็ได้ค่ะ'
                    status = 1
if status == 0:
    for tmp in insult:
        if tmp in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                else:
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    current = random.choice(prefixinsult)
                    result = current + tmpo + final + 'ค่ะ'
                    status = 1
                    break
                if status == 0:
                    current = random.choice(prefixinsult)
                    result = current+final +'ค่ะ'
                    status = 1
            else:
                se = randint(0,2)
                if se == 0:
                    result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                if se == 1:
                    randarray = ['ไม่น่าเชื่อถือพอค่ะ','ไม่น่ารักพอค่ะ','ไม่ดูดีพอค่ะ','ไม่ได้ผ่านเข้ารอบค่ะ']
                    result = 'ขอโทษค่ะหนูไม่ด่าเพราะคุณ'+random.choice(randarray)
                status = 1
if status == 0:
    if 'ด่า' in message:
        if 'มัน' in message or 'สิ' in message or 'ซิ' in message or 'เดะ' in message or 'เซะ' in message or 'ดิ' in message or 'ที' in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                else:
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                    if (tmpo in message):
                        current = random.choice(prefixinsult)
                        if 'พี่' not  in message :
                            result = current + tmpo +current+ final + 'ค่ะ'
                            status = 1
                            break
                        else:
                            if select == 1 or select == 2:
                                result = current+tmpo+current+final+'ค่ะ'
                                status = 1
                                break 
                            else:
                                result =  current+tmpo+final+'ค่ะ'
                                status = 1
                                break
            else:
                se = randint(0,2)
                if se == 0:
                    result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                if se == 1:
                    randarray = ['ไม่น่าเชื่อถือพอค่ะ','ไม่น่ารักพอค่ะ','ไม่ดูดีพอค่ะ','ไม่ได้ผ่านเข้ารอบค่ะ']
                    result = 'ขอโทษค่ะหนูไม่ด่าเพราะคุณ'+random.choice(randarray)
                status = 1
if status == 0:
    if 'ชม' in message:
        if 'มัน' in message or 'สิ' in message or 'ซิ' in message or 'เดะ' in message or 'เซะ' in message or 'ดิ' in message or 'ที' in message or 'กุ' in message or 'กุ' in message or 'หน่อย':
            if 'ที่' not in message and '.' not in message:
                for tomp in chloeset:
                    if tomp in message:
                        final = ''
                        first = ''
                        second = ''
                        for tmpo in member2:
                            if (tmpo in message):
                                result = tmpo+random.choice(good)+'ค่ะ'
                                status = 1
                                break
                            #else:
                                #result = random.choice(good)+'ค่ะ'
                                #status = 1
                    #else:
                        #result = random.choice(good)+'ค่ะ'
                        #status = 1
if status == 0:
    if 'โอ๋' in message :
        if 'มัน' in message or 'สิ' in message or 'ซิ' in message or 'เดะ' in message or 'เซะ' in message or 'ดิ' in message or 'ที' in message or 'กุ' in message or 'กุ' in message or 'หน่อย':
            if True:
                final = ''
                first = ''
                second = ''
                for tmpo in member2:
                    if (tmpo in message):
                        result = tmpo+random.choice(care)
                        status = 1
                        break
                    #else:
                        #result = random.choice(good)+'ค่ะ'
                        #status = 1
            else:
                result = random.choice(good)+'ค่ะ'
                status = 1                
if status == 0:
    if 'ด่า' in message:
        if 'แหละ' in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    ran1 = ['ตึ่งตะลึงตึ่งโป๊ะ','ตะลึงตึงโป้ะ','ตะลึง ตะลึงตึงโป้ะ !','แฮร่']
                    result =  random.choice(ran1)
                    status = 1
                    break               
if status == 0:
    if 'แฮร' in message:
        result = random.choice(randomfive)
        status == 1
if status == 0:
	if '@tutor' in message:
		result = 'กดที่รูปของ Chloe Secretary\nเลือก "Chat" => แถบเมนูด้านล่างกดคำว่านัดเรียน\nคุณสามารถพูดคุยกับ Chloe ได้แต่อยู๋ในระหว่างพัฒนาต้องขออภัยในความไม่สมบูรณ์\n\n***ถ้าจองแล้วต้องการยกเลิกกรุณาติดต่อผู้สอน'
		status =1

'''if status == 0:
    if 'เพิ่มข้อความระบบ' in message:
        if isinsult == '1':
            stringout = message.replace('เพิ่มข้อความระบบ','')
            fo = open('question', 'r+')
            with open('question') as myFile:
                for num,line in enumerate(myFile,1):
                    if stringout in line:
                        f = open(gdate, 'r+')
                        d = f.readlines()
                        tmpstring = ''
                        for line in d:
                            if line != num
                                tmpstring += line
                        f.close()
                        os.remove('question')
                        fo2 = open('question', 'a')
                        fo2.write(tmpstring)
                        fo2.close()
            fo3 = open('question', 'a')
            fo3.write(stringout + '\n')
            fo3.close()
            result = 'เพิ่มข้อความระบบเรียบร้อยค่ะ'
'''
'''
if status == 0:
    if 'เพิ่มนัดเรียน:' in message:
        try:
            tmpgo = message
            message = message.replace('เพิ่มนัดเรียน:','')
            #print(message+'done')
            gdate = message[0:10]
            jobhour = message[11:13]
            jobmin = message[14:16]
            jobtime = message[17:18]
            name = message[19:]
            content = message[11:]
            print('เพิ่มนัดเรียน')
            print (content)
            fo = open(gdate, 'a')
            fo.write(content + '*\n')
            fo.close()
            fo = open('customerdate', 'a')
            fo.write(gdate + ',' + jobhour + ',' + jobmin + '\n')
            fo.close()
            result = 'เพิ่มนัดหมายการเรียนเรียบร้อยค่ะหากต้องการยกเลิกกรุณาติดต่อผู้สอน'
            line_bot_api.push_message(destination, TextSendMessage(tmpgo))
        except Exception as e:
            result = 'การนัดหมายล้มเหลวกรุณาติดต่อผู้สอน'
        bot_mode = 0
        bot_status = 0
        status = 1
if status == 0:
    if'เพิ่มตารางงาน:'in message:
        try:
            tmpgo = message
            message = message.replace('เพิ่มตารางงาน:','')
            #print(message+'done')
            gdate = message[0:10]
            jobhour = message[11:13]
            jobmin = message[14:16]
            jobtime = message[17:18]
            name = message[19:]
            content = message[11:]
            print('เพิ่มตารางงาน')
            print (content)
            fo = open(gdate, 'a')
            fo.write(content + '$\n')
            fo.close()
            fo = open('scheduledate', 'a')
            fo.write(gdate + ',' + jobhour + ',' + jobmin + '\n')
            fo.close()
            result = 'เพิ่มตารางงานเรียบร้อยค่ะ'
            line_bot_api.push_message(destination, TextSendMessage(tmpgo))
        except Exception as e:
            result = 'การเพิ่มตารางล้มเหลว'
        bot_mode = 0
        bot_status = 0
        status = 1        
if status == 0:
    if 'ตารางนัดหมายวันที่:' in message:
        try:
                atpos = message.find("ตารางนัดหมายวันที่:")
                message = message[atpos:]
                message = message.replace('ตารางนัดหมายวันที่:','')
                gdate = message[0:10]
                fo = open(gdate, 'r+')
                result = 'ตารางนัดหมายวันที่:\n'+gdate +'\n'
                for lines in fo:
                    if '*' in lines:
                        result += lines
                        fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
    bot_status = 0
    bot_mode = 0
    status = 1
if status == 0:
    if 'ตารางงานวันที่:' in message:
        try:
                atpos = message.find("ตารางงานวันที่:")
                message = message[atpos:]
                message = message.replace('ตารางงานวันที่:','')
                gdate = message[0:10]
                fo = open(gdate, 'r+')
                result = 'ตารางงานวันที่:\n'+gdate +'\n'
                for lines in fo:
                    if '$' in lines:
                        result += lines
                fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
            bot_status = 0
    bot_mode = 0
    status = 1
if status == 0:
    if 'ตารางวันที่:' in message:
        try:
                atpos = message.find("ตารางวันที่:")
                message = message[atpos:]
		message = message.replace('ตารางวันที่:','')
		gdate = message[0:10]
		fo = open(gdate, 'r+')
		result = 'รายการตารางวันที่\n'+gdate +'\n'
		for lines in fo:
                    if '*' not in lines and '$' not in lines:
                        result += lines
                fo.close()
	except Exception as e:
            print (e)
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
	bot_status = 0
	bot_mode = 0
	status = 1
if status == 0:
    if 'รายการนัดหมายวันนี้' in message:
	    try:
		index = 6
		gdate = ""
		f = open("customerdate", "r+")
		text = f.readlines()
		for line in text:
		    curday = int(line[0:2])
		    curmonth = int(line[3:5])
		    curyear =  int(line[6:10])
		    curhour = int(line[11:13])
		    curmin =  int(line[14:16])
		    if(curday == now.day and curmonth == now.month and curyear == now.year):
			try:
			    gdate = (now.strftime("%d-%m-%Y"))
			    result += "\nกำหนดการนัดหมาย \nวันนี้ : \n--------\n"
			    # Open a file
			    fo = open(gdate, "r+")
                            for lines in fo:
                                #print (lines)
                                if True:
                                    if '*' in lines:
                                    #if str(curmin) in lines:
                                        result += lines
                            # Close opend file
                            fo.close()
			    break
			except Exception as e:
			    print (e)
		    # Close opend file
		    f.close()
	    except:
                result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว' '''
'''
if status == 0:
    if 'รายการนัดหมายวันพรุ่งนี้' in message:
	    try:
		index = 6
		gdate = ""
		f = open("customerdate", "r+")
		text = f.readlines()
		for line in text:
		    curday = int(line[0:2])
		    curday= curday +1
		    curmonth = int(line[3:5])
		    curyear =  int(line[6:10])
		    curhour = int(line[11:13])
		    curmin =  int(line[14:16])
		    if(curday == now.day and curmonth == now.month and curyear == now.year):
			try:
			    gdate = (now.strftime("%d-%m-%Y"))
			    result += "\nกำหนดการนัดหมาย \nวันพรุ่งนี้ : \n--------\n"
			    # Open a file
			    fo = open(gdate, "r+")
                            for lines in fo:
                                #print (lines)
                                if True:
                                    if '*' in lines:
                                    #if str(curmin) in lines:
                                        result += lines
                            # Close opend file
                            fo.close()
			    break
			except Exception as e:
			    print (e)
		    # Close opend file
		    f.close()
	    except:
                result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
if status == 0:
    if 'รายการตารางงานวันนี้' in message:
	    try:
		index = 6
		gdate = ""
		f = open("scheduledate", "r+")
		text = f.readlines()
		for line in text:
		    curday = int(line[0:2])
		    curmonth = int(line[3:5])
		    curyear =  int(line[6:10])
		    curhour = int(line[11:13])
		    curmin =  int(line[14:16])
		    if(curday == now.day and curmonth == now.month and curyear == now.year):
			try:
			    gdate = (now.strftime("%d-%m-%Y"))
			    result += "\nกำหนดการตารางงาน \nวันนี้ : \n--------\n"
			    # Open a file
			    fo = open(gdate, "r+")
                            for lines in fo:
                                #print (lines)
                                if True:
                                    if '$' in lines:
                                    #if str(curmin) in lines:
                                        result += lines
                            # Close opend file
                            fo.close()
			    break
			except Exception as e:
			    print (e)
		    # Close opend file
		    f.close()
	    except Exception as e:
                result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
                print (e)
if status == 0:
    if 'รายการตารางงานวันพรุ่งนี้' in message:
	    try:
		index = 6
		gdate = ""
		f = open("scheduledate", "r+")
		text = f.readlines()
		for line in text:
		    curday = int(line[0:2])
		    curday= curday +1
		    curmonth = int(line[3:5])
		    curyear =  int(line[6:10])
		    curhour = int(line[11:13])
		    curmin =  int(line[14:16])
		    if(curday == now.day and curmonth == now.month and curyear == now.year):
			try:
			    gdate = (now.strftime("%d-%m-%Y"))
			    result += "\nกำหนดการตารางงาน \nวันพรุ่งนี้ : \n--------\n"
			    # Open a file
			    fo = open(gdate, "r+")
                            for lines in fo:
                                #print (lines)
                                if True:
                                    if '$' in lines:
                                    #if str(curmin) in lines:
                                        result += lines
                            # Close opend file
                            fo.close()
			    break
			except Exception as e:
			    print (e)
		    # Close opend file
		    f.close()
	    except:
                result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'		

'''
if status == 0:
    for tmp in simq_ask:
        if tmp in message:
            position = simq_ask.index(tmp)
            result = simq_ans[position]
            status = 1
'''            
if status == 0:
   if '!@ยอดค้างเข้าโคโลเนล' in message:
       group = 'C5c90aa2273d7093f30ca08a91066cd78'
       associateid = 'Cacab1833e4e7009f49c15779e645f66c'
       namepush = ''
       credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
       gc = gspread.authorize(credentials)
       sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
       worksheet = sh.worksheet("Account")
       for num in range(2, 31):
           tmp = (worksheet.cell(num, 22).value)
           if (tmp >= 1 ):
               name = worksheet.cell(num,7).value
               if num == 8:
                   continue
                name = name.encode("utf-8")
               namepush += name+' - '+tmp+' ครั้ง \n'
        result = 'รายงานจำนวนครั้งการค้างชำระถึงเดือนนี้\n'+namepush
       line_bot_api.push_message(destination, TextSendMessage(result))
       print("Push Report Stuck Assoc")
if status == 0:
   if '!@ยอดค้างภาคีลับ' in message:
       group = 'C5c90aa2273d7093f30ca08a91066cd78'
       associateid = 'Cacab1833e4e7009f49c15779e645f66c'
       namepush = ''
       credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
       gc = gspread.authorize(credentials)
       sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
       worksheet = sh.worksheet("Account")
       for num in range(2, 31):  # Must be 31 in col or last parameter
           tmp = (worksheet.cell(num, 22).value)
           if (tmp >= 1 ):
               name = worksheet.cell(num,7).value
               if num == 8:
                   continue
                name = name.encode("utf-8")
               namepush += name+' - '+tmp+' ครั้ง \n'
        result = 'รายงานจำนวนครั้งการค้างชำระถึงเดือนนี้\n'+namepush
        line_bot_api.push_message(associateid, TextSendMessage(result))
        print("Push Report Stuck Assoc")

if status == 0:
    if '!@ยอดค้างไลน์ภาค' in message:
	group = 'C5c90aa2273d7093f30ca08a91066cd78'
	associateid = 'Cacab1833e4e7009f49c15779e645f66c'
	namepush = ''
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
        worksheet = sh.worksheet("Account")
        for num in range(2, 31):  # Must be 31 in col or last parameter
            tmp = (worksheet.cell(num, 22).value)
            if (tmp >= 1 ):
                name = worksheet.cell(num,7).value
                if num == 8:
                    continue
                if num == 20:
                    continue
                name = name.encode("utf-8")
                namepush += name+' - '+tmp+' ครั้ง \n'
        result = 'รายงานจำนวนครั้งการค้างชำระถึงเดือนนี้\n'+namepush
        line_bot_api.push_message(group,TextSendMessage(result))
        print("Push Report Stuck Group")'''
if '!@' in message :
    os.remove('control')
    fo = open('control','a')
    if ('ภาคีลับ' in message):
        strws = '2'
    elif 'ไลน์ภาค' in message :
        strws = '1'
        fo.write(strws)
        fo.close()
        if (strws == '1'):
            destinations = 'C5c90aa2273d7093f30ca08a91066cd78'
            print ("Heads change to ไลน์ภาค")
        elif (strws == '2'):
            destinations = 'Cacab1833e4e7009f49c15779e645f66c'
            print ("Heads change to ภาคีลับ")
abort_after = 5
start = time.time()
def removeLine(filename, key):
    timeout_start = time.time()
    state = 0
    with open(filename, 'r+') as outputFile:
        with open(filename, 'r') as inputFile:
            seekPosition = 0 
            currentLine = inputFile.readline()
            while not currentLine.strip().startswith('%s' % key):
                delta = time.time() - start
                if delta >= abort_after:
                    state = 1
                    break
                seekPosition = inputFile.tell()
                currentLine = inputFile.readline()
            if state == 0:
                outputFile.seek(seekPosition, 0)
            
                currentLine = inputFile.readline()
                while currentLine:
                    outputFile.writelines(currentLine)
                    currentLine = inputFile.readline()
        if state == 0:
            outputFile.truncate()
        if state == 1:
            result = "[ERROR]: ไม่พบคคำถาม/ตอบดังกล่าว"
            status =  1
if status == 0:
    if "ลบถาม/" in message :
        try:
            atpos = message.find("ลบถาม/")
            message = message[atpos:]
            message = message.replace("ลบถาม/","")
            #message = message.replace("ตอบ/","")
            filename = 'qanda'
            removeLine(filename,message)
            if status == 0:
                result = "การลบคำถามเสร็จสมบูรณ์"
                status = 1     
        except Exception as e:
            print("Error Code: ")
            print (e)
            result = 'ไม่สามารถหาข้อมูลถามตอบดังกล่าวได้'
if status == 0:
    if "เพิ่มถาม/" in message:
        if isinsult == '1':
            try:
                atpos = message.find("เพิ่มถาม/")
                message = message[atpos:]
                message = message.replace("เพิ่มถาม/","")
                #message = message.replace("ตอบ/","")
                print (message)
                fo = open('qanda','a')
                fo.write(message+'\n')
                fo.close()
                result = "การเพิ่มคำถามเสร็จสมบูรณ์"
                status = 1
            except Exception as e:
                result = 'ไม่สามารถเพิ่มข้อมูลถามตอบดังกล่าวได้'
                print(e)
        else:
            randarray = ['ไม่น่าเชื่อถือพอค่ะ','ไม่น่ารักพอค่ะ','ไม่ดูดีพอค่ะ','ไม่ได้ผ่านเข้ารอบค่ะ','... ไม่สามารถสาธยายได้ค่ะ']
            result = 'ขอโทษค่ะไม่สามารถปฏิบัติกรณีดังกล่าวได้เพราะคุณ'+random.choice(randarray)
            status = 1

'''if status == 0:
    getresult = []
    tmp = []
    i = 0
    mode = '0'
    if isinsult == '1':
        i = 0
        fo = open('qanda','r+')
        for lines in fo:
            tmp = str(lines.split('/',1))
            if tmp[0] == message:
                getresult.append(tmp[1])
                i = i+1
        fo.close()
        try:
            if i == 1:
                result = getresult[0]
                status = 1
            elif i > 1:
                result = random.choice(getresult)
                status = 1
        except Exception as e:
            result = "ERROR"
            print (e)
'''

print ('%s' % result)
