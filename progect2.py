from mysql.connector import connection

def database_exist(database):
    config={"user":"root","password":"belive_god1527","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute(f"drop database if EXISTS {database}")
    cur.execute(f"create database {database}")
    conn.commit()
    cur.close()
    conn.close()



def uus():
    config={"user":"root","password":"belive_god1527","host":"localhost","database":"pro"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute(""" create table sarina(
                    sarina_name varchar(50) not null,
                    saina_id    int  auto_increment primary key,
                    creadit     char(11) not null,
                    passord    nvarchar(11), 
                    note         text,
                    creat       datetime default current_timestamp
    )""")
    conn.commit()
    cur.close()
    conn.close()

def prodact():
    config={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""create table prodact (
                name varchar(50) not null,
                codeId bigint not null unique,
                id int not NULL primary key ,
                create_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id) references sarina(saina_id)
    )""")
    conn.commit()
    cur.close()
    conn.close()
 
def calcu():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"pro"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""create table calu(
                user_id int ,
                last_seen_cal datetime defaultt timestamp

    )""")

if __name__=="__main__":
    database="pro"
    database_exist(database)
    uus()
    prodact()
    calcu()
    