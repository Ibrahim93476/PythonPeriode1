# Opdracht 1: Leeftijd check
age = 21
if age >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent nog geen 18.")

# Opdracht 2: Cijfer check
grade = 7.5
if grade >= 5.5:
    print("Je hebt een voldoende!")
else:
    print("Je hebt een onvoldoende.")

# Opdracht 3: Cijfer beoordeling (Elif)
grade = 9
if grade >= 8:
    print("Goed gedaan!")
elif grade >= 5.5:
    print("Voldoende!")
else:
    print("Onvoldoende.")

# Opdracht 4: Game Character
health = 80
has_shield = True

if health >= 50:
    print("Je hebt genoeg health.")
else:
    print("Je hebt weinig health!")

if has_shield:
    print("Je hebt een schild!")

# Opdracht 5: Toegang check
age = 19
has_ticket = True

if age >= 18 and has_ticket:
    print("Je mag naar binnen!")
else:
    print("Je mag niet naar binnen.")

# Opdracht 6: Tellen 1 t/m 10
for i in range(1, 11):
    print(i)

# Opdracht 7: Tafel van 5
for i in range(1, 11):
    print(f"{i} x 5 = {i * 5}")

# Opdracht 8: Countdown
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("GO!")

# Opdracht 9: Health verliezen
health = 100
for i in range(10):
    health -= 10
    print(f"Health: {health}")

# Opdracht 10: Even of oneven
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is oneven")