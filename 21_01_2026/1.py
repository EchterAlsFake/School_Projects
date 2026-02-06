import logging

from base_api import setup_logger

logger = setup_logger("School Projects - []", level=logging.DEBUG)


jahr = int(input("Geben Sie ein Jahr ein"))
logger.debug(f"Jahr: {jahr}")
if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0):
    logger.debug("1. Bedingung erfüllt")
    if jahr % 4 == 0:
        logger.debug("2. Bedingung erfüllt")
        if jahr % 400 == 0:
            logger.debug("3. Bedingung erfüllt, es ist ein Schaltjahr!")
            ergebnis = True

        else:
            logger.warning("3. Bedingung nicht erfüllt, kein Schaltjahr")
            ergebnis = False

    # Korrektur
    else:
        logger.warning("2. Bedingung nicht erfüllt, kein Schaltjahr")
        ergebnis = False

# Korrektur
else:
    ergebnis = False


if (ergebnis):
    print(f"Nein, kein Schaltjahr")

else:
    print(f"Ja, es ist ein Schaltjahr")

