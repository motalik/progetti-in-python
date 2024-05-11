import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Afghanistan": "Kabul",
    "Armenia": "Yerevan",
    "Azerbaijan": "Baku",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Bhutan": "Thimphu",
    "Brunei": "Bandar Seri Begawan",
    "Cambodia": "Phnom Penh",
    "China": "Beijing",
    "Cyprus": "Nicosia",
    "Georgia": "Tbilisi",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Israel": "Jerusalem",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Astana",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Lebanon": "Beirut",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Male",
    "Mongolia": "Ulaanbaatar",
    "Myanmar (Burma)": "Nay Pyi Taw",
    "Nepal": "Kathmandu",
    "North Korea": "Pyongyang",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palestine": "Jerusalem",
    "Philippines": "Manila",
    "Qatar": "Doha",
    "Russia": "Moscow",
    "Saudi Arabia": "Riyadh",
    "Singapore": "Singapore",
    "South Korea": "Seoul",
    "Sri Lanka": "Sri Jayawardenapura Kotte",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "United Arab Emirates": "Abu Dhabi",
    "Uzbekistan": "Tashkent",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a"
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
