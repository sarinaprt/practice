from mysql.connector import connection


def insret_sina(sarina_name,creadit,passord,note):
    config={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("insert into sarina(sarina_name,creadit,passord,note)values(%s,%s,%s,%s)",(sarina_name,creadit,passord,note))
    conn.commit()
    cur.close()
    conn.close()

def pro_duct(name,codeId,id):
    config={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("insert into prodact(name,codeId,id)values(%s,%s,%s)",(name,codeId,id))
    conn.commit()
    cur.close()
    conn.close()

def selecT_id():
    config={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("select * from sarina ")
    ca=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return ca
def calu(user_id):
    config={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("insert into calu(user_id,)values(%s)",(user_id))
    conn.commit()
    cur.close()
    conn.close()

def upd():
    confg={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**confg)
    cur=conn.cursor()
    cur.execute("update sarina set passord='sarinaa' where id=1")
    conn.commit()
    cur.close()
    conn.close()

def joi():
    confg={"user":"root","password":"belive_god1527","database":"pro","host":"localhost"}
    conn=connection.MySQLConnection(**confg)
    cur=conn.cursor()
    cur.execute("""select calu.user_id ,calu.last_seen_cal ,sarina.sarina_name,
                sarina.saina_id,sarina.email,sarina.passord,sarina.creadit 
                from sarina 
                left join calu on calu.user_id=sarina.saina_id""")
    conn.commit()
    cur.close()
    conn.close()

if __name__=="__main__":
    insret_sina()
    pro_duct()
    calu()
