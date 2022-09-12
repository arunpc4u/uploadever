import time

import requests
import telebot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tg_tqdm import tg_tqdm
message_textpaus=''
message = ''
user_id =''
durl ='non'
token = '5221168866:AAGLvKleWYSR4nI33CgCUsk6dERud1AwUUg'
bot = telebot.TeleBot(token)
# You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start', 'login'])
def send_welcome(message):
#	User = input("Enter your User name: ")
	bot.reply_to(message, "Enter username passward Note You should take a space after user name ")
@bot.message_handler(func=lambda message: True,content_types=['photo','video','text','audio','document'])
def echo_message(message):
  print(message)
  try:
   file = message.video.file_id
  except:
    print("not video")
  try:
    print('audio')
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
#d file and auto mate
  try:
    print(file)
    Path = 'https://api.telegram.org/bot'+token+'/getFile?file_id='+file
    print(Path)
    callpath = requests.get(Path ,allow_redirects=True).text.split('"')  # message_textus.split(" ")
    print(callpath[17])
    pathfile = 'https://api.telegram.org/file/bot'+token+'/'+callpath[17]
    print(pathfile)
    useid = message.from_user.id
  #  print(useid.str)
    print(type(useid))
    form = open(str(useid) +".txt", "rt")
    print(form)
   #print(id , form)
    Lines = form.readlines()
    us = Lines[0]
    ps = Lines[1]
    url = 'https://uploadever.in/login.html'
    url2 = 'https://uploadever.in/?op=upload_form'
    s = Service('/var/www/html/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    driver.find_element_by_name("login").send_keys(us)
    driver.find_element_by_name("password").send_keys(ps)
    try:
      for post1 in driver.find_elements_by_xpath(
              '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[1]'):
        pot1 = post1.value_of_css_property('padding-left')
      for post2 in driver.find_elements_by_xpath(
              '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[2]'):
        pot2 = post2.value_of_css_property('padding-left')
      for post3 in driver.find_elements_by_xpath(
              '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[3]'):
        pot3 = post3.value_of_css_property('padding-left')
      for post4 in driver.find_elements_by_xpath(
              '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[4]'):
        pot4 = post4.value_of_css_property('padding-left')
      po = \
      driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div')[
        0].text
      pok = [int(pot1.strip('px')), int(pot2.strip('px')), int(pot3.strip('px')), int(pot4.strip('px'))]
      print(pok)
      po = [po[0], po[2], po[4], po[6]]

      print(po)
      res = {pok[i]: po[i] for i in range(len(pok))}
      print(res)
      # for key in sorted(res):
      #   print (key, res[key])
      sorted_list = sorted(res.keys())
      # sorted(res.items(), key=lambda x: x[1])
      print(type(sorted_list))
      print(type(res))
      cap = res[sorted_list[0]] + res[sorted_list[1]] + res[sorted_list[2]] + res[sorted_list[3]]
      print(cap)
      driver.find_element_by_css_selector("#container > div:nth-child(5) > div > div > div > form > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys(
        cap)
    except:
      print('no Cap')

    driver.find_element_by_css_selector('button.btn.btn-primary.btn-save.btn-block').click()
    driver.get(url2)
    try:
      for _ in tg_tqdm(range(100), token, useid):
        time.sleep(.050)
    except:
      print('kl')
    driver.find_element_by_css_selector("li#select_url").click()
    print('ts')
    print(pathfile)
    try:
     driver.find_element_by_css_selector("textarea.form-control").send_keys(pathfile)
     print('url')

     driver.find_element_by_css_selector('button.btn.btn-primary.btn-upload.uploadbtn').click()
     print('kkk')

     element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.ID, "s-links"))
     )
     print('do')

     print('ss')

     durl=driver.find_element_by_css_selector("textarea#s-links.form-control").get_attribute("value");
    except:
      durl = 'Incorrect password or username please try again Enter your username and passward by commond /login to'

    print("not ")
  except:
    print("not file")
   # print(file)
  cid = message.chat.id
  mid = message.message_id
  global message_textus
  message_textus= message.text

  user_id = message.from_user.id
  user_name = message.from_user.first_name
  try:
    message_textpaus = message.text.split(" ")#message_textus.split(" ")
    us= message_textpaus[0]
    ps=message_textpaus[1]
    #print(us,ps)
    print('go')
    fo = open(str(user_id)+'.txt', "w")
    print('ope')
    fo.write(message_textpaus[0]+'\n'+message_textpaus[1]);
   # Close opened file
    print('clo')
    fo.close()
    try:
      url = 'https://uploadever.in/login.html'
      url2 = 'https://uploadever.in/?op=upload_form'
      s = Service('/var/www/html/chromedriver.exe')
      driver = webdriver.Chrome(service=s)
      driver.get(url)
      driver.find_element_by_name("login").send_keys(us)
      driver.find_element_by_name("password").send_keys(ps)
      po = 'non'
      try:
        for post1 in driver.find_elements_by_xpath(
                '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[1]'):
          pot1 = post1.value_of_css_property('padding-left')
        for post2 in driver.find_elements_by_xpath(
                '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[2]'):
          pot2 = post2.value_of_css_property('padding-left')
        for post3 in driver.find_elements_by_xpath(
                '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[3]'):
          pot3 = post3.value_of_css_property('padding-left')
        for post4 in driver.find_elements_by_xpath(
                '//*[@id="container"]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div/span[4]'):
          pot4 = post4.value_of_css_property('padding-left')
        po = \
        driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div[3]/table/tbody/tr[2]/td[1]/div')[
          0].text
        pok = [int(pot1.strip('px')), int(pot2.strip('px')), int(pot3.strip('px')), int(pot4.strip('px'))]
        print(pok)
        po = [po[0], po[2], po[4], po[6]]

        print(po)
        res = {pok[i]: po[i] for i in range(len(pok))}
        print(res)
        # for key in sorted(res):
        #   print (key, res[key])
        sorted_list = sorted(res.keys())
        # sorted(res.items(), key=lambda x: x[1])
        print(type(sorted_list))
        print(type(res))
        cap = res[sorted_list[0]] + res[sorted_list[1]] + res[sorted_list[2]] + res[sorted_list[3]]
        print(cap)
        driver.find_element_by_css_selector(
          "#container > div:nth-child(5) > div > div > div > form > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys(
          cap)
      except:
        print('no Cap')
      driver.find_element_by_css_selector('button.btn.btn-primary.btn-save.btn-block').click()
      print('lokp')
      driver.find_element_by_name("key").send_keys('us')
      print('jiji')
    except:
      durl = 'Incorrect password or username please try again Enter your username and passward by commond /login to'
      print('lok')

  except:
    print("not text to split")
  try:
   print(message_textpaus[0],message_textpaus[1])

  except:
   print("not text")
  try:
   bot.reply_to(message, durl +'\n'+"send file")
  except:
   bot.reply_to(message, "send file" + '\n' )
bot.infinity_polling()
