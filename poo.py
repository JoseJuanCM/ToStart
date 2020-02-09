#P.O.


class Persona:

	especie = 'Humano'

	def __init__(self, nombre, edad, genero):
		self.nombre = nombre
		self.edad = edad
		self. genero = genero


p1 = Persona("Juan","30","Hombre,Macho,Mexicano")
p2 = Persona("Jose","30","Hombre,Macho,Mexicano")
p1.especie='Alien'
print(type(p1))
print(type(p2))

print(p1.nombre.upper()+'-'+p1.edad+'-'+p1.genero+'-'+p1.especie)
print(p2.nombre.lower()+'-'+p2.edad+'-'+p2.genero+'-'+p2.especie)
