import random
import time

GREEN = "\033[92m"
RESET = "\033[0m"

nazioni_capitali = {
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cape Verde": "Praia",
    "Cameroon": "Yaounde",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Congo, Democratic Republic of the": "Kinshasa",
    "Congo, Republic of the": "Brazzaville",
    "Djibouti": "Djibouti",
    "Egypt": "Cairo",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Eswatini (Swaziland)": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Ghana": "Accra",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Ivory Coast (Côte d'Ivoire)": "Yamoussoukro",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Rwanda": "Kigali",
    "São Tomé and Príncipe": "São Tomé",
    "Senegal": "Dakar",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria, Bloemfontein, Cape Town",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Tanzania": "Dodoma",
    "Togo": "Lome",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
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
