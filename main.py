import imaplib
import email
import time
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re


user_login = 'akhmetgaraevrr@yandex.ru'
user_password = 'esvwkqqilexzbfan'
imap_server = 'imap.yandex.ru'
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(user_login, user_password)
imap.select('INBOX')
while True:
    if len(imap.search(None, 'UNSEEN')[-1][-1]) > 3:
        print('new letter')
    time.sleep(1)