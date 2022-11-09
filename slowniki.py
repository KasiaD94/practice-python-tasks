kontakty = {
    "Bartek" : 938477566,
    "Monika" : 938377264,
    "Kamila" : 947662781
}

# miejsce na twoj kod
kontakty["Jakub"] = 938273443
del kontakty["Kamila"]

# sprawdzenie poprawnosci koadu
if "Jakub" in kontakty and kontakty["Jakub" ] == 938273443:
    print ("Jakub jest w kontaktach.")
    print ("Jego numer to ", kontakty["Jakub"], ".")
if "Kamila" not in kontakty:
    print ("Kamili nie ma w kontaktach.")
