hola = input("ingresa nombre")
edad = input("ingresa edad")
print(f"mi nombre es {hola} y tengo {edad} años")

data = ["hola", "como", "estas", "ñaño"]
with open(data, 'r', encoding='utf-8') as file:
    for datos in data:
        file.write(datos + '\n')