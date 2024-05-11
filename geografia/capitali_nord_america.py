import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Canada": "Ottawa",
    "United States": "Washington D.C.",
    "Mexico": "Mexico City",
    "Bahamas": "Nassau",
    "Cuba": "Havana",
    "Haiti": "Port au Prince",
    "Dominican Republic": "Santo Domingo",
    "Jamaica": "Kingston",
    "Trinidad and Tobago": "Port of Spain",
    "Barbados": "Bridgetown",
    "Saint Kitts and Nevis": "Basseterre",
    "Antigua and Barbuda": "Saint John's",
    "Dominica": "Roseau",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Grenada": "Saint George's",
    "Belize": "Belmopan",
    "Costa Rica": "San Jose",
    "El Salvador": "San Salvador",
    "Guatemala": "Guatemala City",
    "Honduras": "Tegucigalpa",
    "Nicaragua": "Managua",
    "Panama": "Panama City"
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
