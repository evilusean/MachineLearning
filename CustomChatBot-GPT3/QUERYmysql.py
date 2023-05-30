#pip install mysql.connector-python
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

mydb = mysql.connector.connect(
  host = "cloud.mindsdb.com",
  user = os.environ.get("USER"), #email used for mindsdb account
  password = os.environ.get("PASSWORD"), #password used for mindsdb
  port = "3306"
)

cursor = mydb.cursor()
#type question into 'text = '
cursor.execute('''SELECT response from mindsdb.snoopstein_model WHERE author_username = "mindsdb' AND text ="What is the QuestSean?"''')

#you need to iterate over each character as a response
for x in cursor:
  print(x)
