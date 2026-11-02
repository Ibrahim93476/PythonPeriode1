# Opdracht 2: Simpele Rekenmachine

getal1 = input("Voer het eerste getal in: ")
getal2 = input("Voer het tweede getal in: ")

bewerking = input("Kies de berekening (+, -, *, /): ")

# omzetten naar getal
g1 = int(getal1)
g2 = int(getal2)

match bewerking:
    case "+":
        antwoord = g1 + g2
        print("Het antwoord is:", antwoord)
    case "-":
        antwoord = g1 - g2
        print("Het antwoord is:", antwoord)
    case "*":
        antwoord = g1 * g2
        print("Het antwoord is:", antwoord)
    case "/":
        antwoord = g1 / g2
        print("Het antwoord is:", antwoord)
    case _:
        print("Foutmelding")