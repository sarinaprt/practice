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
    return ca



if __name__=="__main__":
    insret_sina("sarineb","01234967891","s195","hdhhshdaafhhfhaehfhfah")
    selecT_id()
    pro_duct("msin",125698123,2)

