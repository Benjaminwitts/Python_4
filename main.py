import random
import os
DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STOPPEN = 'q'
TOEVOEGEN = 't'
done = False
STANDAARD_FILE = "EN_NE.txt"
Lijst_txt_files = ["EN_NE.txt", "Jan.txt"]
NIEUWE_LIJST_Lijst = []
lijst = ["BONJOUR"]
z = 74-len(str(Lijst_txt_files))
niet_klaar = True


def lees_woordenlijst(STANDAARD_LIJST):
    a = {}
    if len(Lijst_txt_files) == 1:
        f = open("EN_NE.txt")

        for line in f:
            woord1, woord2 = line.strip('\n').split('=')
            a[woord1] = woord2
        f.close()
        return a

    elif len(Lijst_txt_files) > 1:
        f = open(STANDAARD_LIJST)
        for line in f:
            woord1, woord2 = line.strip('\n').split('=')
            a[woord1] = woord2
        f.close()
        return a


def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4) + "} |").format(regel))


def print_header():
    print("="*SCHERMBREEDTE)
    print("|"+" "*(SCHERMBREEDTE-2)+"|")


def print_footer():
    print("|"+" "*(SCHERMBREEDTE-2)+"|")
    print("="*SCHERMBREEDTE)


def main():
    while niet_klaar:
        print_header()
        print_regel("o - overhoren van de geselecteerde lijst")
        print_regel("t - voeg woorden toe aan de geselecteerde lijst")
        print_regel("k - selecteer een anderen lijst")
        print_regel("n - maak een nieuwe woordenlijst")
        print_regel("q - stoppen")
        print_footer()
        keuze_gebruiker = input("Uw keuze: ")
        if keuze_gebruiker == OVERHOREN:
            overhoren()

        elif keuze_gebruiker == TOEVOEGEN:
            voeg_woorden_toe()

        elif keuze_gebruiker == NIEUWE_LIJST:
            nieuwe_lijst_naam()

        elif keuze_gebruiker == KIES_LIJST:
            print_menu()

        elif keuze_gebruiker == STOPPEN:
            delete_everything()

        else:
            print_header()
            print_regel("Dat is ongeldig!")
            print_footer()


def overhoren():
    a = lees_woordenlijst(STANDAARD_FILE)
    random_woord = random.choice(list(a.keys()))
    print_header()
    print_regel("Vertaal "+random_woord+"!")
    print_footer()
    keuze_overhoren = input("Uw antwoord: ")

    if keuze_overhoren == a[random_woord]:
        print()
        print_header()
        print_regel("Dat klopt! " + random_woord + " betekend " + a[random_woord] + '!')
        print_regel("Type q als je wil stoppen!")
        print_footer()
        is_q = input()

        if is_q != "q":
            overhoren()
            print()
        else:
            for i in range(5):
                print()

    elif keuze_overhoren == STOPPEN:
        for i in range(5):
            print()

    elif keuze_overhoren != a[random_woord]:
        print()
        print_header()
        print_regel("Dat klopt niet! " + random_woord + " betekend " + a[random_woord] + "!")
        print_regel("Type q als je wil stoppen!")
        print_footer()
        is_q = input()

        if is_q != "q":
            overhoren()
            print()

        else:
            for i in range(5):
                print()


def voeg_woorden_toe():
    print_header()
    print_regel("Schrijf de woorden zo op: Eating=Eten !")
    print_footer()

    keuze_toevoegen = input()

    if keuze_toevoegen == STOPPEN:
        for i in range(5):
            print()
        main()

    elif SCHEIDER not in keuze_toevoegen:
        print_header()
        print_regel("JE BENT DE = VERGETEN!!!!!")
        print_footer()
        is_q = input()
        if is_q != "q":
            voeg_woorden_toe()
            print()
        else:
            for i in range(5):
                print()
        voeg_woorden_toe()
        print()

    else:
        f = open(STANDAARD_FILE, 'a')
        f.write("\n"+keuze_toevoegen)
        f.close()
        print_header()
        print_regel("Ik heb het gedaan!")
        print_footer()
        is_q = input()
        if is_q != "q":
            voeg_woorden_toe()
            print()

        else:
            for i in range(5):
                print()

        voeg_woorden_toe()
        print()


def print_menu():
    print()
    print_header()
    print_regel("Dit is de lijst van .txt files:")
    print("| ", Lijst_txt_files, " "*z+" |")
    print_regel("Om een .txt file te kiezen type de naam van de file in")
    print_footer()

    global STANDAARD_FILE
    STANDAARD_FILE = input()

    if STANDAARD_FILE in Lijst_txt_files:
        for thing in Lijst_txt_files:
            if thing == STANDAARD_FILE:
                lees_woordenlijst(STANDAARD_FILE)

                print_header()
                print_regel("Je file is geselecteerd")
                print_regel("Als je door wil gaan druk op enter")
                print_regel("Als je terug wil gaan naar het keuze menu druk op q")
                print_footer()

                is_q = input()
                if is_q != "q":
                    print_menu()
                    print()
                else:
                    for i in range(5):
                        print()
    else:
        print_header()
        print_regel("Deze file bestaat nog niet!")
        print_regel("Als je door wil gaan druk op enter")
        print_regel("Als je terug wil gaan naar het keuze menu druk op q")
        print_footer()
        is_q = input()
        if is_q != "q":
            print_menu()
            print()
        else:
            for i in range(5):
                print()


def nieuwe_lijst_naam():
    print_header()
    print_regel("Wat moet de naam van deze file zijn?")
    print_regel("VERGEET NIET ER .txt ACHTER TE ZETTEN!!!!")
    print_regel("klik de letter q om terug te gaan!")
    print_footer()
    nieuwe_naam = input()
    if nieuwe_naam == STOPPEN:
        main()
    elif ".txt" not in nieuwe_naam:
        print()
        print_header()
        print_regel("JE BENT .txt VERGETEN!!!!")
        print_footer()
        is_q = input()
        if is_q != "q":
            nieuwe_lijst_naam()
            print()
        else:
            for i in range(5):
                print()
    else:
        f = open(nieuwe_naam, 'a')
        Lijst_txt_files.append(nieuwe_naam)
        NIEUWE_LIJST_Lijst.append(nieuwe_naam)
        print_header()
        print_regel("De lijst is gemaakt!")
        print_regel("Voeg de eerste vetaling toe! anders werkt hij niet!")
        print_regel("Schrijf de woorden zo op: Eating=Eten !")
        print_footer()
        o = input()
        if SCHEIDER not in o:
            print_header()
            print_regel("JE BENT DE IS VERGETEN!!!!!")
            print_footer()

        else:
            f.write(o)
            f.close()
            print_header()
            print_regel("Gelukt, je lijst is gemaakt met een eerste woord!")
            print_regel("Druk op enter als je nog een list wil maken, druk anders op q")
            print_footer()
            is_q = input()
            if is_q != "q":
                nieuwe_lijst_naam()
                print()
            else:
                for i in range(5):
                    print()


def delete_everything():
    for thing in NIEUWE_LIJST_Lijst:
        os.remove(thing)
    print_header()
    print_regel("Goodbye!")
    print_footer()
    niet_klaar = False


main()
