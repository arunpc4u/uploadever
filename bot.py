import os
from os.path import exists as file_exists
import telebot
import re
import requests
import json
token = 'pasteyourbottokenkeyhere!'
bot = telebot.TeleBot(token)
message_textpaus=''
message = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello Dear Sir, If you have UploadEver.in Account than Please => /clickhere")

@bot.message_handler(commands=['clickhere'])
def click(message):
    bot.reply_to(message, "Okay, Please Send API Key!")

@bot.message_handler(commands=['register'])
def echoc_message(message):
    userid = message.from_user.id
    print(userid)
    try:
        api = message.text
        print(api)
        if len(api) == 17:
            if apicheck(api) == str(200):
                register(api, userid)
                bot.reply_to(message, "DONE" )
            else: bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )
        else:
           bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )
    except:
        bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )

@bot.message_handler(commands=['login'])
def echoa_message(message):
    bot.reply_to(message, "login")

@bot.message_handler(commands=['delete'])
def echob_message(message):
    user_id = message.from_user.id
    bot.reply_to(message, "Deleted") + deactivate(user_id)

def apicheck(api):
    URL = 'https://uploadever.in/api/account/info?key='
    allinone = URL + api
    data = json.loads(requests.get(allinone).text)
    return str(data['status'])

def uploadeverclone(fileid):
    fileid = str(fileid)
    onlyidd = fileid.replace('https://uploadever.in','')
    onlyid = onlyidd.replace('/','')
    return onlyid

def register(api, userid):
    useridf = str(userid) + '.txt'
    file = open(useridf,"a")
    file.write(api)
    file.close()
    print('saved')

def deactivate(sss):
    useridf = str(sss) + '.txt'
    os.remove(useridf)
@bot.message_handler(content_types=['text'])
def echo_message(message):
    user_message = message.text
    user_id = message.from_user.id
    if file_exists(str(user_id) + '.txt') == False:
        userid = message.from_user.id
        print(user_id)
        try:
            api = message.text
            print(api)
            if len(api) == 17:
                if apicheck(api) == str(200):
                    register(api, userid)
                    bot.reply_to(message, "DONE" )
                else: bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )
            else:
               bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )
        except:
            bot.reply_to(message, "PLEASE PROVIDE CORRECT API KEY!" )
    else:
         thisisis = 'https://uploadever.in/'
         if thisisis in user_message:
            URL = 'https://uploadever.in/api/file/clone?file_code={0}&key='
            dlurl = URL.format(uploadeverclone(user_message))
            form = open(str(user_id) +".txt", "rt")
            Lines = form.readlines()
            allinone = dlurl + str(Lines)[2:-2]
            print(allinone)
            data = json.loads(requests.get(allinone).text)
            #str(data['result']['url'])
            bot.reply_to(message, str(data['result']['url']) )
         else:
            bot.reply_to(message, 'Send File or UploadEver Link' )

@bot.message_handler(func=lambda message: True,content_types=['photo','video','text','audio','document'])
def echox_message(message):
    user_id = message.from_user.id
    print(message)
    try:
        file = message.video.file_id
    except:
        print("not video")
    try:
        file = message.audio.file_id
    except:
        print("Not audio")
    try:
        file = message.document.file_id
    except:
        print("not doc")
    try:
        file = message.photo[0].file_id
    except:
        print("not photo")
    try:
        print(file)
        Path = 'https://api.telegram.org/bot'+token+'/getFile?file_id='+file
        print(Path)
        callpath = requests.get(Path ,allow_redirects=True).text.split('"')  # message_textus.split(" ")
        print(callpath[17])
        pathfile = 'https://api.telegram.org/file/bot'+token+'/'+callpath[17]
        print(pathfile)
        useid = message.from_user.id
        print(str(useid))
        URL = 'https://uploadever.in/api/upload/url?key={1}&url={0}&fld_id=0'
        form = open(str(user_id) +".txt", "rt")
        Lines = form.readlines()
        apik = str(Lines)[2:-2]
        print(apik)
        dlurl = URL.format(pathfile,apik)
        print(dlurl)
        data = json.loads(requests.get(dlurl).text)
        #str(data['result']['url'])
        bot.reply_to(message, str(data['result']['file_code']) )
    except:
        bot.reply_to(message, 'mtlb')
bot.infinity_polling()
