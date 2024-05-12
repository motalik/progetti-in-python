import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Argentina": "Buenos Aires",
    "Bolivia": "La Paz e Sucre",
    "Brazil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Ecuador": "Quito",
    "Guyana": "Georgetown",
    "Paraguay": "Asuncion",
    "Peru": "Lima",
    "Suriname": "Paramaribo",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}
coppie_da_indovinare = list(nazioni_capitali.items())
random.shuffle(coppie_da_indovinare)

streak = 0
max_streak = 0
cont = 0
indovinato_al_primo_colpo = 0
sbagliato = 0
sbagliato_paesi = set()

start_time = time.time()

while coppie_da_indovinare:
    nazione, capitale = coppie_da_indovinare.pop()

    while True:
        risposta = input(f"{cont}. Qual è la capitale di {nazione}? ").strip()

        if risposta.lower() == capitale.lower():
            print("Esatto!")
            cont += 1
            streak += 1
            max_streak = max(max_streak, streak)
            if streak == 1:
                indovinato_al_primo_colpo += 1
            break
        else:
            if nazione not in sbagliato_paesi:
                sbagliato_paesi.add(nazione)
                print(GREEN + f"Sbagliato. La capitale corretta di {nazione} è {capitale}" + RESET)
                sbagliato += 1
            streak = 0
            cont += 1

end_time = time.time()
tempo_trascorso = end_time - start_time

print("Hai indovinato tutte le capitali! Il gioco è finito.")
print(f"Hai impiegato {tempo_trascorso:.2f} secondi.")
print(f"Streak maggiore: {max_streak}")
print(f"Hai sbagliato {sbagliato} volte.")

