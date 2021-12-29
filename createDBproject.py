# Richard Deegan G00387896

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="25Szarfa"

)

cursor = db.cursor()

cursor.execute("create DATABASE dr_project")