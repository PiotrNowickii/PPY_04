import random

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
updatedList = random.sample(moja_lista, 10)
k = 0
for i in updatedList:
    k+=1
    print(str(k) + ". " + i)