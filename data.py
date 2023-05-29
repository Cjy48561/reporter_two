# 数据测试模块


import sqlite3
# 创建基于硬盘的数据库有则连接无则创建
# conn=sqlite3.connect('demo.db')

# 建表操作；根据提成图设置季节和7个提成档次
# import sqlite3
# conn=sqlite3.connect('demo.db')
# # 设置游标
# c=conn.cursor()
# # 建表sql语句
# sql='''
#     create table tc(
#         seasoin text primary key not null , --季节淡旺平
#         class_1 int not null ,  --档次1 特价房特殊价格
#         class_2 int not null,   --档次2 特价房和钟点房
#         class_3 int not null ,  --档次3 园景、湖景、豪华海景、普通海景
#         class_4 int not null ,  --档次4 行政海景、行政园景
#         class_5 int not null ,  --档次5 海景套房、园景套房
#         class_6 int not null,   --档次6 行政海景套房、行政园景套房
#         class_7 int not null    --档次7 总统套房
#     );
# '''
# # 执行sql语句
# c.execute(sql)
# # 提交数据
# conn.commit()
# # 关闭连接
# conn.close()

# 插入数据
# import sqlite3
#
# conn=sqlite3.connect('demo.db')
# c=conn.cursor()
# sql1='''
#     insert into tc
#     values ('淡季',5,6,25,28,30,30,100)
# '''
# sql2='''
#     insert into tc
#     values ('平季',5,6,25,28,30,30,100)
# '''
# sql3='''
#     insert into tc
#     values ('旺季',5,6,20,22,25,30,100)
# '''
#
# c.execute(sql1)
# c.execute(sql2)
# c.execute(sql3)
#
# conn.commit()
# conn.close()

# 查询数据
import sqlite3
conn=sqlite3.connect('demo.db')
c=conn.cursor()

sql='''
    select * from tc where seasoin='淡季';
'''
context=c.execute(sql)
for row in context:
    print('季节:',row[0])
    print('第一档:',row[1])
    print('第二档:',row[2])
    print('第三档:',row[3])
    print('第三档:',row[4])
    print('第三档:',row[5])
    print('第三档:',row[6])
    print('第三档:',row[7])
conn.close()