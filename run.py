# (c) ArtGames101 2017
# Created by MrBackPack

import sys, os, random, time, subprocess
try:
    from data import cgun
except Exception as ImportError:
    gun = open("data/cgun.py", "w")
    gun.write("gun = 'Pistol'")

people = ["Player 2", "Player3", "Player4", "Player 5", "Player 6", "Player 7"]
guns = ["Pistol", "AK-47", "Knife", "MiniGun"]
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    print("============\n"
          "  Gun Rush  \n"
          "============\n")
    print("1. Play")
    print("\n"
          "2. Choose Weapon")
    print("\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        battle()
    if choice == "2":
        gunchoice()
    if choice == "0":
        clear_screen()
        print("Goodbye!")
        sys.exit(1)

def battle():
    clear_screen()
    print("========\n"
          " Battle \n"
          "========\n")
    print("Current Weapon : {}".format(cgun.gun))
    print("\n"
          "1. Continue  or  2. Switch Gun\n"
          "         0. Exit              \n")
    choice = user_choice()
    if choice == "1":
        choosebt()
    if choice == "2":
        gunchoice()
    if choice == "0":
        main()

def choosebt():
    clear_screen()
    print("========\n"
          " Choose \n"
          "  Type  \n"
          "========\n")
    print("\n"
          "1. FFA  |  0. Back")
    choice = user_choice()
    if choice == "1":
        ffa()
    if choice == "0":
        main()

def ffa():
    l = [ffa2(), ffa5(), ffa8(), ffa20]
    print(random.choice(l))

def ffa2():
    clear_screen()
    print("Connected!")
    time.sleep(3)
    clear_screen()
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You were killed by {}! >:(".format(random.choice(people)))
    time.sleep(3)
    main()

def ffa5():
    clear_screen()
    print("Connected!")
    time.sleep(3)
    clear_screen()
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You were killed by {}! >:(".format(random.choice(people)))
    time.sleep(3)
    main()

def ffa8():
    clear_screen()
    print("Connected!")
    time.sleep(3)
    clear_screen()
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), guns))
    time.sleep(3)
    print("You were killed by {}! >:(".format(random.choice(people)))
    time.sleep(3)
    main()

def ffa20():
    clear_screen()
    print("Connected!")
    time.sleep(3)
    clear_screen()
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("You killed {} with a {}".format(random.choice(people), cgun.gun))
    time.sleep(3)
    print("{} Killed {} with a {}".format(random.choice(people), random.choice(people), random.choice(guns)))
    time.sleep(3)
    print("You were killed by {}! >:(".format(random.choice(people)))
    time.sleep(3)
    main()

def gunchoice():
    clear_screen()
    print("=============\n"
          " Select Your \n"
          "    Weapon   \n"
          "=============\n")
    print("\n"
          "1. Pistol    2. AK-47\n"
          "3. Knife     4. Katana\n"
          "5. PlasmaGun 6. Sniper Rifle\n"
          "7. MiniGun   8. Rocket Launcher")
    print("\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Pistol'")
        input("Your Weapon is now a Pistol!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'AK-47'")
        input("Your Weapon is now an AK-47!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "3":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Knife'")
        input("Your Weapon is now a Knife!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "4":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Katana'")
        input("Your Weapon is now a Katana!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "5":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Plasma Gun'")
        input("Your Weapon is now a Plasma Gun!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "6":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Sniper Rifle'")
        input("Your Weapon is now a Sniper Rifle!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "7":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Mini Gun'")
        input("Your Weapon is now a Mini Gun!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "8":
        gun = open("data/cgun.py", "w")
        gun.write("gun = 'Rocket Launcher'")
        input("Your Weapon is now a Rocket Launcher!")
        gun.close()
        subprocess.call((sys.executable, "run.py"))
main()
