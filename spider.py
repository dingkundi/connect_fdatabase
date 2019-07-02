import pymysql
from sshtunnel import SSHTunnelForwarder

ssh_host = "39.96.37.188"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = "root"  # 这是你在堡垒机上的用户名
ssh_password = "Kw7459170"  # 这是你在堡垒机上的用户密码
mysql_host = "127.0.0.1"  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = "root"  # 这是你mysql数据库上的用户名
mysql_password = "123"  # 这是你mysql数据库的密码
mysql_db = "contract"  # mysql服务器上的数据库名

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)) as server:
    conn = pymysql.connect(host=mysql_host,
                           port=server.local_bind_port,
                           user=mysql_user,
                           passwd=mysql_password,
                           db=mysql_db)

    cursor = conn.cursor()
    cursor.execute("show tables")
    row_1 = cursor.fetchall()
    print(row_1)
    # 获取前n行数据
    # row_2 = cursor.fetchmany(3)
    # 获取所有数据
    # row_3 = cursor.fetchall()
    # conn.commit()
    cursor.close()
    conn.close()




























