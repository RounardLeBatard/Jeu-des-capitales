import random

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

def commands():
    print("""
+----------+-------------------------------------------+
|             Les commandes possibles sont :           |
+==========+===========================================+
| commands | obtenir la liste des commandes possibles  |
| rules    | obtenir la liste des règles               |
| play     | lancer la partie                          |
| stop     | arrêter la partie                         |
| score    | obtenir votre score pendant la partie     |
+----------+-------------------------------------------+
""")

def rules():
    print("""Règles du jeu :

    	Règles globales :
    		1. Vos réponses doivent toujours commencer par des majuscules. ("Dacca"/"Non")
    		2. Ne rajoutez pas d'espace à la fin de vos réponses. ("Bogota "Х, "Bogota"V)
    		3. Quand vous ne savez pas, répondez : "Je ne sais pas".

    	Les indices (1ère lettre de la capitale):
    		(Les indices fonctionnent comme un repêchage, 
    		si vous refusez l'indice, vous perdez 1pt, 
    		si vous acceptez l'indice 
    			et que vous trouvez, vous ne perdez que 0,5pt, 
    			si vous ne trouvez toujours pas, vous êtes vraiment mauvais. (-1,5pt))""")

def print_score():
    print("Votre score est de", points, "pt(s)")

def print_percentage():
    win_rate = win_count / turn_count
    win_rate *= 100
    win_rate = list(str(win_rate))

    if win_rate[3] == "0":
        print("Vous avez eu " + str(win_count) + " sur " + str(turn_count) +
            "(" + win_rate[0] + win_rate[1] + "%).")

    elif win_rate[0] + win_rate[1] + win_rate[2] == "100":
        print("Vous avez eu " + str(win_count) + " sur " + str(turn_count) +
            "(" + win_rate[0] + win_rate[1] + win_rate[2] + "%).")

    else:
        print("Vous avez eu " + str(win_count) + " sur " + str(turn_count) +
            "(" + win_rate[0] + win_rate[1] + win_rate[2] + win_rate[3] + "%).")

def first_letter():
    letters = list(capital)
    return letters[0]

Running = True
playing = "no"
points = 0
win_count = 0
turn_count = 0

while Running == True:
    while playing == "no":
        user_command = input("Ecrivez une commande (commands) : ")

        if user_command == "commands":
            commands()
        elif user_command == "rules":
            rules()
        elif user_command == "play":
            playing = "yes"

    while playing == "yes":
        random_num = random.randint(0, 197)
        country = countries[random_num]
        capital = capitals[random_num]

        print("Le pays dont vous devez trouver la capitale est", country)
        answer = input("Votre réponse est : ")

        if answer == capital:
            points += 1
            win_count += 1
            turn_count += 1
            print("Bravo ! C'est la bonne réponse (+1pt)")
        elif answer == "Je ne sais pas":
            points -= 1
            turn_count += 1
            clue = input("Dommage (-1pt) ! Voulez-vous un indice ? (Oui/Non) : ")
            if clue == "Oui":
                print("La première lettre est", first_letter())
                answer = input("Votre réponse est : ")
                if answer == capital:
                    points += 0.5
                    turn_count += 1
                    print("A moitié bravo. (+0,5pt)")
                else:
                    points -= 0.5
                    turn_count += 1
                    print("Mauvaise réponse (-0,5pt) ! Là, vous êtes vraiment mauvais, la réponse était", capital)
            else:
                continue
        elif answer == "stop":
            print_score()
            print_percentage()
            playing = "no"
        elif answer == "score":
            print_score()
        else:
            points -= 1
            turn_count += 1
            print("Mauvaise réponse ! La capitale de", country, "est", capital, "(-1pt)")