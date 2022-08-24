import random
from tkinter import *

window = Tk()

window.title("Jeu des capitales (par Rounard)")
window.geometry("1000x600+250+100")
window.minsize(720, 480)
window.iconbitmap("logo\logo.ico")
window.config(background="#2b2b2b")
window.resizable(width=False, height=False)

countries = [
    "Afghanistan",
    "Afrique du Sud",
    "Albanie",
    "Algérie",
    "Allemagne",
    "Andorre",
    "Angola",
    "Antigua-et-Barbuda",
    "Arabie saoudite",
    "Argentine",
    "Arménie",
    "Australie",
    "Autriche",
    "Azerbaïdjan",
    "Bahamas",
    "Bahreïn",
    "Bangladesh",
    "Barbade",
    "Belgique",
    "Belize",
    "Bénin",
    "Bhoutan",
    "Biélorussie",
    "Birmanie (Myanmar)",
    "Bolivie",
    "Bosnie-Herzégovine",
    "Botswana",
    "Brésil",
    "Brunei",
    "Bulgarie",
    "Burkina Faso",
    "Burundi",
    "Cambodge",
    "Cameroun",
    "Canada",
    "Cap-Vert",
    "République centrafricaine",
    "Chili",
    "Chine",
    "Chypre",
    "Colombie",
    "Comores",
    "République du Congo",
    "République démocratique du Congo",
    "Îles Cook",
    "Corée du Nord",
    "Corée du Sud",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatie",
    "Cuba",
    "Danemark",
    "Djibouti",
    "République dominicaine",
    "Dominique",
    "Égypte",
    "Émirats arabes unis",
    "Équateur",
    "Érythrée",
    "Espagne",
    "Estonie",
    "Eswatini (Swaziland)",
    "États-Unis",
    "Éthiopie",
    "Fidji",
    "Finlande",
    "France",
    "Gabon",
    "Gambie",
    "Géorgie",
    "Ghana",
    "Grèce",
    "Grenade",
    "Guatemala",
    "Guinée",
    "Guinée-Bissau",
    "Guinée équatoriale",
    "Guyana",
    "Haïti",
    "Honduras",
    "Hongrie",
    "Inde",
    "Indonésie",
    "Irak",
    "Iran",
    "Irlande",
    "Islande",
    "Israël",
    "Italie",
    "Jamaïque",
    "Japon",
    "Jordanie",
    "Kazakhstan",
    "Kenya",
    "Kirghizistan",
    "Kiribati",
    "Koweït",
    "Laos",
    "Lesotho",
    "Lettonie",
    "Liban",
    "Liberia",
    "Libye",
    "Liechtenstein",
    "Lituanie",
    "Luxembourg",
    "Macédoine du Nord",
    "Madagascar",
    "Malaisie",
    "Malaisie",
    "Malawi",
    "Maldives",
    "Mali",
    "Malte",
    "Maroc",
    "Îles Marshall",
    "Maurice",
    "Mauritanie",
    "Mexique",
    "États fédérés de Micronésie",
    "Moldavie",
    "Monaco",
    "Mongolie",
    "Monténégro",
    "Mozambique",
    "Namibie",
    "Nauru",
    "Népal",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norvège",
    "Nouvelle-Zélande",
    "Oman",
    "Ouganda",
    "Ouzbékistan",
    "Pakistan",
    "Palaos",
    "Palestine",
    "Panama",
    "Papouasie-Nouvelle-Guinée",
    "Paraguay",
    "Pays-Bas",
    "Pérou",
    "Philippines",
    "Pologne",
    "Portugal",
    "Qatar",
    "Roumanie",
    "Royaume-Uni",
    "Russie",
    "Rwanda",
    "Saint-Christophe-et-Niévès",
    "Saint-Marin",
    "Saint-Vincent-et-les-Grenadines",
    "Sainte-Lucie",
    "Îles Salomon",
    "Salvador",
    "Samoa",
    "Sao Tomé-et-Principe",
    "Sénégal",
    "Serbie",
    "Seychelles",
    "Sierra Leone",
    "Singapour",
    "Slovaquie",
    "Slovénie",
    "Somalie",
    "Soudan",
    "Soudan du Sud",
    "Sri Lanka",
    "Suède",
    "Suisse",
    "Suriname",
    "Syrie",
    "Tadjikistan",
    "Tanzanie",
    "Tchad",
    "République tchèque",
    "Thaïlande",
    "Timor oriental",
    "Togo",
    "Tonga",
    "Trinité-et-Tobago",
    "Tunisie",
    "Turkménistan",
    "Turquie",
    "Tuvalu",
    "Ukraine",
    "Uruguay",
    "Vanuatu",
    "Vatican",
    "Venezuela",
    "Viêt Nam",
    "Yémen",
    "Zambie",
    "Zimbabwe"
]
countries_done = []
capitals = [
    "Kaboul",
    "Pretoria",
    "Tirana",
    "Alger",
    "Berlin",
    "Andorre-la-Vieille",
    "Luanda",
    "Saint John's",
    "Riyad",
    "Buenos Aires",
    "Erevan",
    "Canberra",
    "Vienne",
    "Bakou",
    "Nassau",
    "Manama",
    "Dacca",
    "Bridgetown",
    "Bruxelles",
    "Belmopan",
    "Porto-Novo",
    "Thimphou",
    "Minsk",
    "Naypyidaw",
    "La Paz",
    "Sarajevo",
    "Gaborone",
    "Brasilia",
    "Bandar Seri Begawan",
    "Sofia",
    "Ouagadougou",
    "Gitega",
    "Phnom Penh",
    "Yaoundé",
    "Ottawa",
    "Praia",
    "Bangui",
    "Santiago",
    "Pékin",
    "Nicosie",
    "Bogota",
    "Moroni",
    "Brazzaville",
    "Kinshasa",
    "Avarua",
    "Pyongyang",
    "Séoul",
    "San José",
    "Yamoussoukro",
    "Zagreb",
    "La Havane",
    "Copenhague",
    "Djibouti",
    "Saint-Domingue",
    "Roseau",
    "Le Caire",
    "Abou Dabi",
    "Quito",
    "Asmara",
    "Madrid",
    "Tallinn",
    "Mbabane",
    "Washington D.C.",
    "Addis-Abeba",
    "Suva",
    "Helsinki",
    "Paris",
    "Libreville",
    "Banjul",
    "Tbilissi",
    "Accra",
    "Athènes",
    "Saint-Georges",
    "Guatemala",
    "Conakry",
    "Bissau",
    "Malabo",
    "Georgetown",
    "Port-au-Prince",
    "Tegucigalpa",
    "Budapest",
    "New Delhi",
    "Jakarta",
    "Bagdad",
    "Téhéran",
    "Dublin",
    "Reykjavik",
    "Tel Aviv",
    "Rome",
    "Kingston",
    "Tokyo",
    "Amman",
    "Nour-Soultan",
    "Nairobi",
    "Bichkek",
    "Tarawa-Sud",
    "Koweït",
    "Vientiane",
    "Maseru",
    "Riga",
    "Beyrouth",
    "Monrovia",
    "Tripoli",
    "Vaduz",
    "Vilnius",
    "Luxembourg",
    "Skopje",
    "Antananarivo",
    "Kuala Lumpur",
    "Putrajaya",
    "Lilongwe",
    "Malé",
    "Bamako",
    "La Valette",
    "Rabat",
    "Delap-Uliga-Darrit",
    "Port-Louis",
    "Nouakchott",
    "Mexico",
    "Palikir",
    "Chisinau",
    "Monaco",
    "Oulan-Bator",
    "Podgorica",
    "Maputo",
    "Windhoek",
    "Yaren",
    "Katmandou",
    "Managua",
    "Niamey",
    "Abuja",
    "Alofi",
    "Oslo",
    "Wellington",
    "Mascate",
    "Kampala",
    "Tachkent",
    "Islamabad",
    "Melekeok",
    "Ramallah",
    "Panama",
    "Port Moresby",
    "Asuncion",
    "Amsterdam",
    "Lima",
    "Manille",
    "Varsovie",
    "Lisbonne",
    "Doha",
    "Bucarest",
    "Londres",
    "Moscou",
    "Kigali",
    "Basseterre",
    "Saint-Marin",
    "Kingstown",
    "Castries",
    "Honiara",
    "San Salvador",
    "Apia",
    "São Tomé",
    "Dakar",
    "Belgrade",
    "Victoria",
    "Freetown",
    "Singapour",
    "Bratislava",
    "Ljubljana",
    "Mogadiscio",
    "Khartoum",
    "Djoubanote",
    "Sri Jayawardenapura Kotte",
    "Stockholm",
    "Berne",
    "Paramaribo",
    "Damas",
    "Douchanbé",
    "Dodoma",
    "N'Djaména",
    "Prague",
    "Bangkok",
    "Dili",
    "Lomé",
    "Nuku'alofa",
    "Port-d'Espagne",
    "Tunis",
    "Achgabat",
    "Ankara",
    "Funafuti",
    "Kiev",
    "Montevideo",
    "Port-Vila",
    "Cité du Vatican",
    "Caracas",
    "Hanoï",
    "Sanaa",
    "Lusaka",
    "Harare"
]

country = "None"
capital = "None"
answer = "None"
clue = "None"
question_template = "Le pays dont vous devez trouver la capitale est : "
running = True
score = 0
win_count = 0
turn_count = 0

def generate():
    global country
    global capital
    global article

    random_num = random.randint(0, 197)

    if random_num in countries_done:
        generate()
    else:
        countries_done.append(random_num)

        country = countries[random_num]

        capital = capitals[random_num]

        vowels = ["A", "E", "I", "O", "U", "Y"]

        country = countries[random_num]
        capital = capitals[random_num]

        if list(country)[0] in vowels:
            article = "l'"
        else:
            article = ""
        label_question["text"] = question_template
        label_question_country["text"] = article + country

def increase_score(n):
    global score
    score += n
    label_score["text"] = score

def decrease_score(n):
    global score
    score -= n
    label_score["text"] = score

def start_game():
    generate()
    game_ui()

def game_ui():
    forget_menu()
    label_question.pack(expand=YES)
    label_question_country.pack()
    question_frame.pack()
    label_info.pack(pady=5)
    answer_entry.pack(expand=YES, padx=10, pady=7)
    answer_entry_frame.pack(pady=6)
    question_and_answer.pack(expand=YES)

    label_score.pack(pady=5, padx=5, anchor="e")

def forget_menu():
    label_title.pack_forget()
    title.pack_forget()
    icon_canvas.pack_forget()
    play_button.pack_forget()
    play_button_border.pack_forget()

def check_answer(event):
    global win_count
    global turn_count

    if answer_entry.get() == capital:
        increase_score(1)
        win_count += 1
        turn_count += 1
        label_info["fg"] = "#62FF49"
        label_info["text"] = "[+1] Bravo ! C'est la bonne réponse !"
    elif answer_entry.get() == "Je ne sais pas":
        decrease_score(1)
        turn_count += 1
        clue()
#        label_info["fg"] = "#FF634C"
#        label_info["text"] = "[-1] Dommage ! La réponse était : " + capital
    else:
        decrease_score(1)
        turn_count += 1
        label_info["fg"] = "#FF634C"
        label_info["text"] = "[-1] Dommage ! La réponse était : " + capital

    generate()
    answer_entry.delete(0, END)

def first_letter():
    letters = list(capital)
    return letters[0]

def clue():
    label_ask_clue_1.pack()
    label_ask_clue_2.pack()
    frame_clue.pack(anchor="n")

window.bind("<Return>", check_answer)

question_and_answer = Frame(window, bg="#2b2b2b")

question_frame = Frame(question_and_answer, bg="#2b2b2b")
label_question = Label(question_frame, text="Le pays dont vous devez trouver la capitale est :",
                       font=("Consolas", 17), bg="#2b2b2b", fg="white")
label_question_country = Label(question_frame, text="Country", font=("Consolas bold", 19), bg="#2b2b2b", fg="white")

label_info = Label(question_and_answer, text="", font=("Calibri italic", 15), bg="#2b2b2b", fg="#FF634C")

answer_entry_frame = Frame(question_and_answer, bg="#2b2b2b")

answer_entry = Entry(answer_entry_frame, textvariable=answer, bd=3, font=("Consolas", 20), width=30, relief="flat")

title = Frame(window, background="#2b2b2b")
title.pack(anchor="n", pady=50)

width = 150
height = 150
icon = PhotoImage(file="logo\map.png").zoom(8).subsample(32)
icon_canvas = Canvas(title, width=width, height=height, bg="#2b2b2b", bd=0, highlightthickness=0)
icon_canvas.create_image(width/2, height/2, image=icon)
icon_canvas.pack()

label_title = Label(title, text="Jeu des capitales", font=("Consolas", 30), bg="#2b2b2b", fg="white")
label_title.pack(pady=10)

play_button_border = Frame(window, highlightthickness=0, highlightbackground="white", bd=3)
play_button = Button(play_button_border, text="Jouer", font=("Consolas", 30), bg="#2b2b2b", fg="white", bd=0,
                     command=start_game)
play_button.pack()
play_button_border.pack()

frame_clue = Frame(window)
label_ask_clue_1 = Label(frame_clue, text="Voulez vous un indice")
label_ask_clue_2 = Label(frame_clue, text="(1ère lettre de la capitale) ?")

label_score = Label(window, text=0, font=("Consolas", 35), background="#2b2b2b", fg="white")

window.mainloop()



