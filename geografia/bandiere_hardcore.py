from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import time

start_time = None

def update_flag_counter():
    counter_a_schermo.config(text=f"{bandiere_totali - len(ordine_immagini)}/{bandiere_totali}")

def show_next_flag(event=None):
    global index, start_time
    if start_time is None:
        start_time = time.time()
    if entry.get().strip().lower() == lista_immagini[ordine_immagini[index]]:
        immagine_corrente_a_schermo.destroy()
        del ordine_immagini[index]
        update_flag_counter()
        if ordine_immagini:
            index = random.randint(0, len(ordine_immagini) - 1)
            show_flag()
            entry.delete(0, tk.END)
        else:
            end_game()

def end_game():
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    feedback.config(text=f"Gioco finito, tempo impiegato: {minutes} minuti {seconds} secondi")
    root.after(2000, root.quit)

def update_timer():
    if start_time:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        timer_a_schermo.config(text=f"Tempo: {minutes:02d}:{seconds:02d}")
    root.after(1000, update_timer)

def close_app():
    root.quit()

root = tk.Tk()
root.title("Indovina la bandiera")
root.attributes('-fullscreen', False)
root.attributes('-fullscreen', True)
root.configure(bg="white")
bottone_chiusura = tk.Button(root, text="Chiudi", command=close_app)
bottone_chiusura.pack(side="top", anchor="ne")
counter_a_schermo = tk.Label(root, text="", bg="white")
counter_a_schermo.pack(side="top", anchor="ne")
timer_a_schermo = tk.Label(root, text="Tempo: 00:00", bg="white")
timer_a_schermo.pack(side="top", anchor="nw")
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<KeyRelease>", show_next_flag)  # Controlla automaticamente la risposta ad ogni lettera inserita
feedback = tk.Label(root, text="", bg="white")
feedback.pack(pady=5)
frame_immagine = tk.Frame(root, bg="white")
frame_immagine.pack(pady=10)


lista_immagini = {
    "bandiere/afghanistan.gif": "afghanistan",
    "bandiere/albania.gif": "albania",
    "bandiere/algeria.gif": "algeria",
    "bandiere/andorra.gif": "andorra",
    "bandiere/angola.gif": "angola",
    "bandiere/antigua-and-barbuda.gif": "antigua and barbuda",
    "bandiere/argentina.gif": "argentina",
    "bandiere/armenia.gif": "armenia",
    "bandiere/australia.gif": "australia",
    "bandiere/austria.gif": "austria",
    "bandiere/azerbaijan.gif": "azerbaijan",
    "bandiere/bahamas.gif": "bahamas",
    "bandiere/bahrain.gif": "bahrain",
    "bandiere/bangladesh.gif": "bangladesh",
    "bandiere/barbados.gif": "barbados",
    "bandiere/belarus.gif": "belarus",
    "bandiere/belgium.gif": "belgium",
    "bandiere/belize.gif": "belize",
    "bandiere/benin.gif": "benin",
    "bandiere/bhutan.gif": "bhutan",
    "bandiere/bolivia.gif": "bolivia",
    "bandiere/bosnia.gif": "bosnia and herzegovina",
    "bandiere/botswana.gif": "botswana",
    "bandiere/brazil.gif": "brazil",
    "bandiere/brunei.gif": "brunei",
    "bandiere/bulgaria.gif": "bulgaria",
    "bandiere/burkina-faso.gif": "burkina faso",
    "bandiere/burundi.gif": "burundi",
    "bandiere/ivory-coast.gif": "ivory coast",
    "bandiere/cape-verde.gif": "cape verde",
    "bandiere/cambodia.gif": "cambodia",
    "bandiere/cameroon.gif": "cameroon",
    "bandiere/canada.gif": "canada",
    "bandiere/central-african-republic.gif": "central african republic",
    "bandiere/chad.gif": "chad",
    "bandiere/chile.gif": "chile",
    "bandiere/china.gif": "china",
    "bandiere/colombia.gif": "colombia",
    "bandiere/comoros.gif": "comoros",
    "bandiere/congo.gif": "congo",
    "bandiere/costa-rica.gif": "costa rica",
    "bandiere/croatia.gif": "croatia",
    "bandiere/cuba.gif": "cuba",
    "bandiere/cyprus.gif": "cyprus",
    "bandiere/czechia.gif": "czechia",
    "bandiere/denmark.gif": "denmark",
    "bandiere/djibouti.gif": "djibouti",
    "bandiere/dominica.gif": "dominica",
    "bandiere/dominican-republic.gif": "dominican republic",
    "bandiere/north-korea.gif": "north korea",
    "bandiere/ecuador.gif": "ecuador",
    "bandiere/egypt.gif": "egypt",
    "bandiere/el-salvador.gif": "el salvador",
    "bandiere/equatorial-guinea.gif": "equatorial guinea",
    "bandiere/eritrea.gif": "eritrea",
    "bandiere/estonia.gif": "estonia",
    "bandiere/eswatini.gif": "eswatini",
    "bandiere/ethiopia.gif": "ethiopia",
    "bandiere/fiji.gif": "fiji",
    "bandiere/finland.gif": "finland",
    "bandiere/france.gif": "france",
    "bandiere/gabon.gif": "gabon",
    "bandiere/gambia.gif": "gambia",
    "bandiere/georgia.gif": "georgia",
    "bandiere/germany.gif": "germany",
    "bandiere/ghana.gif": "ghana",
    "bandiere/greece.gif": "greece",
    "bandiere/grenada.gif": "grenada",
    "bandiere/guatemala.gif": "guatemala",
    "bandiere/guinea.gif": "guinea",
    "bandiere/guinea-bissau.gif": "guinea bissau",
    "bandiere/guyana.gif": "guyana",
    "bandiere/haiti.gif": "haiti",
    "bandiere/vatican-city.gif": "vatican city",
    "bandiere/honduras.gif": "honduras",
    "bandiere/hungary.gif": "hungary",
    "bandiere/iceland.gif": "iceland",
    "bandiere/india.gif": "india",
    "bandiere/indonesia.gif": "indonesia",
    "bandiere/iran.gif": "iran",
    "bandiere/iraq.gif": "iraq",
    "bandiere/ireland.gif": "ireland",
    "bandiere/israel.gif": "israel",
    "bandiere/italy.gif": "italy",
    "bandiere/jamaica.gif": "jamaica",
    "bandiere/japan.gif": "japan",
    "bandiere/jordan.gif": "jordan",
    "bandiere/kazakhstan.gif": "kazakhstan",
    "bandiere/kenya.gif": "kenya",
    "bandiere/kiribati.gif": "kiribati",
    "bandiere/kuwait.gif": "kuwait",
    "bandiere/kyrgyzstan.gif": "kyrgyzstan",
    "bandiere/laos.gif": "laos",
    "bandiere/latvia.gif": "latvia",
    "bandiere/lebanon.gif": "lebanon",
    "bandiere/lesotho.gif": "lesotho",
    "bandiere/liberia.gif": "liberia",
    "bandiere/libya.gif": "libya",
    "bandiere/liechtenstein.gif": "liechtenstein",
    "bandiere/lithuania.gif": "lithuania",
    "bandiere/luxembourg.gif": "luxembourg",
    "bandiere/madagascar.gif": "madagascar",
    "bandiere/malawi.gif": "malawi",
    "bandiere/malaysia.gif": "malaysia",
    "bandiere/maldives.gif": "maldives",
    "bandiere/mali.gif": "mali",
    "bandiere/malta.gif": "malta",
    "bandiere/marshall-islands.gif": "marshall islands",
    "bandiere/mauritania.gif": "mauritania",
    "bandiere/mauritius.gif": "mauritius",
    "bandiere/mexico.gif": "mexico",
    "bandiere/micronesia.gif": "micronesia",
    "bandiere/moldova.gif": "moldova",
    "bandiere/monaco.gif": "monaco",
    "bandiere/mongolia.gif": "mongolia",
    "bandiere/montenegro.gif": "montenegro",
    "bandiere/morocco.gif": "morocco",
    "bandiere/mozambique.gif": "mozambique",
    "bandiere/myanmar.gif": "myanmar",
    "bandiere/namibia.gif": "namibia",
    "bandiere/nauru.gif": "nauru",
    "bandiere/nepal.gif": "nepal",
    "bandiere/netherlands.gif": "netherlands",
    "bandiere/new-zealand.gif": "new zealand",
    "bandiere/nicaragua.gif": "nicaragua",
    "bandiere/niger.gif": "niger",
    "bandiere/nigeria.gif": "nigeria",
    "bandiere/macedonia.gif": "macedonia",
    "bandiere/norway.gif": "norway",
    "bandiere/oman.gif": "oman",
    "bandiere/pakistan.gif": "pakistan",
    "bandiere/palau.gif": "palau",
    "bandiere/panama.gif": "panama",
    "bandiere/papua-new-guinea.gif": "papua new guinea",
    "bandiere/paraguay.gif": "paraguay",
    "bandiere/peru.gif": "peru",
    "bandiere/philippines.gif": "philippines",
    "bandiere/poland.gif": "poland",
    "bandiere/portugal.gif": "portugal",
    "bandiere/qatar.gif": "qatar",
    "bandiere/romania.gif": "romania",
    "bandiere/russia.gif": "russia",
    "bandiere/rwanda.gif": "rwanda",
    "bandiere/st-kitts-and-nevis.gif": "st kitts and nevis",
    "bandiere/st-lucia.gif": "st lucia",
    "bandiere/samoa.gif": "samoa",
    "bandiere/san-marino.gif": "san marino",
    "bandiere/sao-tome.gif": "sao tome and principe",
    "bandiere/saudi-arabia.gif": "saudi arabia",
    "bandiere/senegal.gif": "senegal",
    "bandiere/serbia.gif": "serbia",
    "bandiere/seychelles.gif": "seychelles",
    "bandiere/sierra-leone.gif": "sierra leone",
    "bandiere/singapore.gif": "singapore",
    "bandiere/slovakia.gif": "slovakia",
    "bandiere/slovenia.gif": "slovenia",
    "bandiere/solomon-islands.gif": "solomon islands",
    "bandiere/somalia.gif": "somalia",
    "bandiere/south-africa.gif": "south africa",
    "bandiere/south-korea.gif": "south korea",
    "bandiere/south-sudan.gif": "south sudan",
    "bandiere/spain.gif": "spain",
    "bandiere/sri-lanka.gif": "sri lanka",
    "bandiere/st-vincent.gif": "st vincent",
    "bandiere/palestine.gif": "palestine",
    "bandiere/sudan.gif": "sudan",
    "bandiere/suriname.gif": "suriname",
    "bandiere/sweden.gif": "sweden",
    "bandiere/switzerland.gif": "switzerland",
    "bandiere/syria.gif": "syria",
    "bandiere/tajikistan.gif": "tajikistan",
    "bandiere/tanzania.gif": "tanzania",
    "bandiere/thailand.gif": "thailand",
    "bandiere/east-timor.gif": "east timor",
    "bandiere/togo.gif": "togo",
    "bandiere/tonga.gif": "tonga",
    "bandiere/trinidad-and-tobago.gif": "trinidad and tobago",
    "bandiere/tunisia.gif": "tunisia",
    "bandiere/turkey.gif": "turkey",
    "bandiere/turkmenistan.gif": "turkmenistan",
    "bandiere/tuvalu.gif": "tuvalu",
    "bandiere/uae.gif": "uae",
    "bandiere/uk.gif": "uk",
    "bandiere/usa.gif": "usa",
    "bandiere/taiwan.png": "taiwan",
    "bandiere/uganda.gif": "uganda",
    "bandiere/ukraine.gif": "ukraine",
    "bandiere/uruguay.gif": "uruguay",
    "bandiere/uzbekistan.gif": "uzbekistan",
    "bandiere/vanuatu.gif": "vanuatu",
    "bandiere/venezuela.gif": "venezuela",
    "bandiere/vietnam.gif": "vietnam",
    "bandiere/yemen.gif": "yemen",
    "bandiere/zambia.gif": "zambia",
    "bandiere/zimbabwe.gif": "zimbabwe",
}


ordine_immagini = list(lista_immagini.keys())
random.shuffle(ordine_immagini)
bandiere_totali = len(ordine_immagini)

index = random.randint(0, len(ordine_immagini) - 1)

first_flag_shown = False

def show_flag():
    global immagine_corrente_a_schermo, first_flag_shown
    if hasattr(show_flag, "immagine_corrente_a_schermo") and immagine_corrente_a_schermo is not None:
        immagine_corrente_a_schermo.destroy()
    
    percorso_immagine = ordine_immagini[index]
    image = Image.open(percorso_immagine)
    image = ImageTk.PhotoImage(image)
    immagine_corrente_a_schermo = tk.Label(frame_immagine, image=image, bg="white")
    immagine_corrente_a_schermo.image = image
    immagine_corrente_a_schermo.pack(pady=5, anchor="w")
    
    if not first_flag_shown:
        first_flag_shown = True
        root.after(1000, lambda: immagine_corrente_a_schermo.pack_forget())
    else:
        root.after(50, lambda: [immagine_corrente_a_schermo.pack_forget(), entry.focus_set()])

show_flag()
update_flag_counter()
update_timer()
root.mainloop()
