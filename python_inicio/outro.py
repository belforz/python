my_vetor = [1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6]
count_1 = my_vetor.count(1)
count_2 = my_vetor.count(2)
count_3 = my_vetor.count(3)
count_4 = my_vetor.count(4)
count_5 = my_vetor.count(5)
count_6 = my_vetor.count(6)
print("o tamnho desse vetor é de:", len(my_vetor))

list_1 = [1] * count_1
list_2 = [2] * count_2
list_3 = [3] * count_3
list_4 = [4] * count_4
list_5 = [5] * count_5
list_6 = [6] * count_5

new_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6
print(new_list)

vetor = [20, 50, 5, 92, 42, 52, 12, 120, 120, 120]

# fazendo a conta do tamnho do vetor
print("O tamanho do vetor é:", len(vetor))

#exibicao de dados
for i in range(len(vetor)):
    if i % 2 == 0:
        print(vetor[i])


# class Calc:
#     def retangulo(self):
#         try:
#             a_tri = float(str(input("Type o valor da area: ")))
#             b_tri = float(str(input("Type o valor da base: ")))
#             if a_tri < 0 :
#                 print("Tente um numero maior que 0")
#             else:
#                 a_res = (a_tri * b_tri) / 2
#                 formatted_result = "{:.2f}".format(a_res)
#                 print("A area do retangulo:", formatted_result)
#
#         except ValueError:
#             print("O valor é incorreto.")
#
#     def triangulo(self):
#         try:
#             a_tri1 = float(str(input("Type o valor da area")))
#             b_tri2 = float(str(input("Type o valor da base")))
#             if a_tri1 < 0:
#                 print("Tente um numero maior")
#                 return
#             else:
#                 a_res = (a_tri1 * b_tri2)
#                 formatted_result = "{:.2f". format(a_res)
#                 print("O resultado do triangulo é", formatted_result)
#         except ValueError:
#             print("O valor está incorreto")

# FAZENDO VETORES EM PYTHON



