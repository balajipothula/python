import mysql.connector

try:

  db = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root", database="emp")

  cursor = db.cursor()
  
  cursor.execute("SELECT * FROM emp")
  emp = cursor.fetchall()
  for e in emp: print(e)

  cursor.execute("SELECT COUNT(*) FROM emp")
  count = cursor.fetchone()
  print(count)

except Exception as e:

  print("system message: " + str(e))
  print("user   message: exception")

finally:
  print("finally block executed")
