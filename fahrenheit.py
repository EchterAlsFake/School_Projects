"""
Dieses Programm rechnet die Celsius Temperatur zu Fahrenheit um.
"""

from colorama import Fore, init
init(autoreset=True)

celsius = input(f"{Fore.LIGHTCYAN_EX}Enter the temperature in celsius -->:{Fore.LIGHTWHITE_EX}")
celsius = int(celsius)

fahrenheit = celsius * 9 / 5 + 32
print(f"{Fore.LIGHTMAGENTA_EX}The temperature in Fahrenheit is -->:{Fore.LIGHTWHITE_EX} {fahrenheit}")

