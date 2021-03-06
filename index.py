import os
from arboretum import Arboretum
from actions import annex_habitat
from actions import release_animal
from actions import build_facility_report
from actions import add_plant
from actions import feed_animal

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

colors = {
    "Black": "\u001b[30m",
    "Red": "\u001b[31m",
    "Green": "\u001b[32m",
    "Yellow": "\u001b[33m",
    "Blue": "\u001b[34m",
    "Magenta": "\u001b[35m",
    "Cyan": "\u001b[36m",
    "White": "\u001b[37m",
    "Reset": "\u001b[0m",
}


def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++")
    print("+ K  e  a  h  u  a    A  r  b  o  r  e  t  u  m +")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++\u001b[0m\n")
    print("\u001b[32m1. Annex Habitat 🏞")
    print("2. Release Animal 🐬 into Habitat")
    print("3. Feed Animal 🐠")
    print("4. Add Plant 🌺 to Habitat")
    print("5. Display Facility Report 📈")
    print("6. Exit 🚪\u001b[0m")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        add_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()


main_menu()
