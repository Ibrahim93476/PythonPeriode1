# Oefening 1
# Print de volgende zin "Hello World"
print("Hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit
naam = "Ibrahim"
leeftijd = 18
woonstad = "Montfoort"

print(naam)
print(leeftijd)
print(woonstad)


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
print(f"Hallo mijn naam is {naam}, ik ben {leeftijd} jaar oud en ik woon in {woonstad}")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit
favouriteGame = "FIFA 24"
hoursPlayed = 200
rating = 9.0

print(f"Mijn favoriete game is {favouriteGame}")
print(f"Ik heb deze game {hoursPlayed} uur gespeeld")
print(f"Ik geef deze game een {rating}")


# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 10
number2 = 5

som = number1 + number2
verschil = number1 - number2
product = number1 * number2

print("Som:", som)
print("Verschil:", verschil)
print("Product:", product)


# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit
name = "Ibrahim"
health = 100
level = 10
damage = 25

print("Character:", name, "Health:", health, "Level:", level, "Damage:", damage)

health = health - 20
print("Nieuwe health na damage:", health)


# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit
weapon = "Gouden Zwaard"
damage = damage + 15
level = level + 1

print("Wapen:", weapon)
print("Nieuwe damage:", damage)
print("Nieuw level:", level)


# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe
name = "Ibrahim"
age = 18
favouriteGame = "FIFA 24"
hoursPlayed = 200
level = 11
score = 1500

# Bonus variabelen
rank = "Pro"
isOnline = True
platform = "PlayStation 5"

print(f"Gamer Profile: {name}, Leeftijd: {age}, Game: {favouriteGame}, Uren: {hoursPlayed}, Level: {level}, Score: {score}")
print(f"Bonus Info -> Rank: {rank}, Online: {isOnline}, Platform: {platform}")

score = score + 250
print("Nieuwe score:", score)