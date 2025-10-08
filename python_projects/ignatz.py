"""
Johannes Habel Copyright (C) 2025 <EchterAlsFake@proton.me
Licensed under GPLv3

Name: Bauer Ignatz Problem
Version: 1.0
"""
import httpx
import re
from bs4 import BeautifulSoup
from colorama import Fore, init
init(autoreset=True)


# Einlesen der Daten
a = int(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX}Gib die Breite ein -->:"))
b = int(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX}Gib die Länge ein -->:"))
#preis = int(input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX}Gib den Preis des Materials pro Meter ein (in Euro)-->:"))

print("Aktuelle Preise werden heruntergeladen...")
content = httpx.get("https://www.zaun-idee.de/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36" }).content.decode("utf-8")
soup = BeautifulSoup(content, "html.parser")
preis = soup.find("div", class_="hasDiscount").find("span", class_="amount-pre-discount text-12-11").text.replace(",", ".").strip().replace("€", "")
preis = float(preis)

Fläche = a*b
Umfang = 2 * (a+b)
Preis = Umfang * preis

print(f"""
Die Fläche beträgt: {Fläche}
Der Umfang beträgt: {Umfang}

Der Endpreis liegt bei: {Fore.LIGHTMAGENTA_EX}{Preis} €
""")





