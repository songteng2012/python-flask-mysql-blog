import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb.cursors



# 1.连接本地mysql数据库
conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'yaoll100.',database = 'mysql',charset = 'utf8',cursorclass = MySQLdb.cursors.DictCursor)

# 创建一个执行句柄，用来执行后面的语句
cur = conn.cursor()

#创建表

cur.execute("""CREATE TABLE if not exists posts (
         id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
         created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
         title VARCHAR(20) NOT NULL,
         content VARCHAR(60) NOT NULL)"""
)

# 已插入两条文章
# cur.execute("insert into posts (title,content) values('学习Flask1','跟麦叔学习Flask第一部分')")
# cur.execute("insert into posts (title,content) values('学习Flask2','跟麦叔学习Flask第二部分')")
cur.execute('select * from posts')
result = cur.fetchall()
print(result)

conn.commit()

# 关闭链接
conn.close()