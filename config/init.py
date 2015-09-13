#!/home/isucon/local/python-3.3/bin/python

try:
  import MySQLdb
  from MySQLdb.cursors import DictCursor
except ImportError:
  import pymysql as MySQLdb
  from pymysql.cursors import DictCursor

def connect_db():
  host = 'localhost'
  port = 3306
  username = 'isucon'
  password = ''
  dbname   = 'isucon'
  db = MySQLdb.connect(host=host,  port=port,  db=dbname,  user=username,  passwd=password,  cursorclass=DictCursor,  charset="utf8")
  return db

def main():
  db = connect_db()
  cur = db.cursor()
  cur.execute("SELECT * FROM memos WHERE is_private=0 ORDER BY created_at DESC,  id DESC LIMIT 100")
  cur.execute('select * from memos')
  memos = cur.fetchall()
  for memo in memos:
    cur.execute('select username from users where id=%s', memo['user'])
    username = cur.fetchone()['username']
    cur.execute("update memos set username=%s where user=%s", (username, memo['user']))

  cur.close()
  db.commit()

main()
