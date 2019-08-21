import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    use_unicode=True,
    charset="utf8"
)

# 通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()

# 创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作
# cur.execute(
#     "create table student(id int ,name varchar(20),class varchar(30),age varchar(10))"
# )

# 插入一条数据
cur.execute("insert into student values(2,'Tom','class 2','9')")

# # 修改查询条件的数据
# cur.execute("update student set class='class 1' where name = 'Tom'")
#
# # 删除查询条件的数据
# cur.execute("delete from student where age='9'")

# 关闭游标
cur.close()

# commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()

# 关闭数据库连接
conn.close()