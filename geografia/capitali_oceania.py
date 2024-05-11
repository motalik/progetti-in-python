import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Australia": "Canberra",
    "Fiji": "Suva",
    "Kiribati": "Tarawa Atoll",
    "Marshall Islands": "Majuro",
    "Micronesia": "Palikir",
    "Nauru": "Yaren",
    "New Zealand": "Wellington",
    "Palau": "Melekeok",
    "Papua New Guinea": "Port Moresby",
    "Samoa": "Apia",
    "Solomon Islands": "Honiara",
    "Tonga": "Nuku'alofa",
    "Tuvalu": "Funafuti",
    "Vanuatu": "Port Vila"
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
