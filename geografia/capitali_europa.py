import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Austria": "Vienna",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Czech Republic (Czechia)": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia (Macedonia)": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Ukraine": "Kiev",
    "United Kingdom": "London",
    "Vatican City": "Vatican City",
    "Wales": "Cardiff"
}

coppie_da_indovinare = list(nazioni_capitali.items())
random.shuffle(coppie_da_indovinare)
cont=0

start_time = time.time()

while coppie_da_indovinare:
    nazione, capitale = coppie_da_indovinare.pop()

    while True:
        risposta = input(f"{cont}.Qual è la capitale di {nazione}? ").strip()

        if risposta.lower() == capitale.lower():
            print("Esatto!")
            cont+=1
            
            break
        else:
            print(GREEN + f"Sbagliato. La capitale corretta di {nazione} è {capitale}" + RESET)
end_time = time.time()
tempo_trascorso = end_time - start_time

print("Hai indovinato tutte le capitali! Il gioco è finito.")
print(f"Hai impiegato {tempo_trascorso:.2f} secondi.")
