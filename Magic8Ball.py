import random

question = input('Dime tu pregunta:')

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Si - posta que si!'
elif random_number == 2:
  answer = 'y, la verdad es que vos ya sabes la respuesta'
elif random_number == 3:
  answer = 'Preguntale a los astros o a las cartas'
elif random_number == 4:
  answer = 'Tu energia esta muy pesada, rompiste la matrix! necesitamos que vuelvas a preguntar'
elif random_number == 5:
  answer = 'Tenes que aprender a descansar para saber la respuesta'
elif random_number == 6:
  answer = 'La historia siempre se repite sino estudiamos para cambiarla'
elif random_number == 7:
  answer = 'Mis fuentes alienigenas dicen que mejor por ahora, no'
elif random_number == 8:
  answer = 'Se manija, dale para adelante!'
elif random_number == 9:
  answer = 'La energia esta en duda, deberias confiar mas en vos primero'
else:
  answer = 'Hay magia dentro tuyo, cuando la liberes y disfrutes, sabras la respuesta'
  
print('Pregunta:      ' + question) 
print('Respuesta de la Magic 8 Ball:  ' + answer)