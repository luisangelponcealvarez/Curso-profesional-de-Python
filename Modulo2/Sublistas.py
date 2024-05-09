lista_cursos = ["Python", "Java", "C#", "PHP"]
# [start:end]
# [start:] -> Obtenemos los ultimos elementos de la lista
# [:end] -> Obtenemos los primeros elementos de la lista
# [start:end:skip] -> Obtenemos los ultimos elementos de la lista
sub_lista = lista_cursos[0:3]
print(sub_lista)

sub_lista = lista_cursos[::-1]
print(sub_lista)
