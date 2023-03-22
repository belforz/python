




#conexao com sql com inputs
# import mysql.connector
# try:
#     con = mysql.connector.connect(user='root', password='',host='localhost', database='naruto_the_anime')
#     cursor = con.cursor()
#
#     insert_nome = str(input("Type a name: "))
#     insert_idade = int(input("Type an age: "))
#     insert_aldeia = str(input("Type a village: "))
#     insert_status = str(input("Type a status: "))
#
#     insert_dados = "INSERT INTO personagens(nome, idade, aldeia, status) VALUES(%s, %s, %s, %s)"
#     values_dados = (insert_nome, insert_idade, insert_aldeia, insert_status)
#     cursor.execute(insert_dados, values_dados)
#     con.commit()
#
#     if cursor.rowcount == 1:
#         print("It was sucessfully done")
#     else:
#         print("It was a failure")
#
#     cursor.close()
#     con.close()
# except ValueError:
#     print("Invalid input")
#
#
#













#conexao com o sql simples
# cnx = mysql.connector.connect(user='root', password='', host='localhost', database= 'naruto_the_anime')
#
# cursor = cnx.cursor()
#
# insert_dados = "INSERT INTO personagens(nome, idade, aldeia, status) VALUES (%s,%s,%s,%s)"
# values_dados =('Minato Uzumaki', 30,'Vila da Folho','Morto')
# cursor.execute(insert_dados, values_dados)
# cnx.commit()
# if cursor.rowcount == 1:
#     print("It was sucessfully done!")
# else:
#     print("Error")
# cursor.close()
# cnx.close()
