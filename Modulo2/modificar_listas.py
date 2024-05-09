lista_curso = ["Python", "Java", "JavaScript", "PHP", "Ruby", "Go", "C#"]
lista_curso2 = ["C", "C++"]

lista_curso.append("Kotlin")  # En este añadimos un elemento al final de la lista
print(lista_curso)

lista_curso.insert(0, "C")  # En este añadimos en el indice 0 un elemento de la lista

lista_curso.extend(
    lista_curso2
)  # Añadimos todos los elementos de la lista2 a la lista1

print(lista_curso)
print(len(lista_curso))

lista_curso.remove("Kotlin")  # Eliminamos el elemento Kotlin de la lista
print(lista_curso)

del lista_curso[0]  # Eliminamos el elemento en el indice 0

lista_curso.clear()

print(len(lista_curso))
print(lista_curso)
