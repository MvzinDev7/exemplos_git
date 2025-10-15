# Criando uma tupla 
frutas = ("Banana", "Uva", "Morango", "Acerola")

# Print(type(frutas))

print(frutas)

print[2] = "Manga" #Teremos um erro (Tuplas são imutáveis e caso precise fazer manipulação dos dados é melhor usar fila)

print(frutas[2])


#Exibir todas as frutas

for item in frutas:
    print(item)
