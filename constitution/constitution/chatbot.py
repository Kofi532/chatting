# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import MySQLdb
#import pandas as pd
import tweepy
import time
from datetime import datetime, timezone
import re
import logging
import os
import time
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('your SSH hostname'),
    ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
    remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    db = MySQLdb.connect(
        user='kofi532',
        passwd='CONABLEboakye532-',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='kofi532$twitter',
    )
    # Do stuff



logger = logging.getLogger()

cursor = db.cursor()
cursor.execute("SELECT * FROM Persons")
table_rows = cursor.fetchall()
df = pd.DataFrame(table_rows)
li1 = list(df[2])
li2 = list(df[3])
lek = []
for a,b in zip(li1,li2):
    lek.append(a)
    lek.append(b)

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    lek
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}") 