import mysql.connector
try:
    con = mysql.connector.connect(user='root', password='', host='localhost', database='naruto_the_anime')
    cursor = con.cursor()
    descricao_sql = 20
    descricao_sql1 = 14
    cursor.execute("UPDATE personagens SET descricao = %s WHERE id >= %s", (descricao_sql, descricao_sql1))
    con.commit()

    if cursor.rowcount >= 1:
        print("It was sucessfully done")
    else:
        print("It was a failure")
except ValueError:
    print("Erro")