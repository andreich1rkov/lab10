import random
import logging

logging.basicConfig(level=logging.INFO, filename="Ugadai_log.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")


while True:
    try:
        N = int(input("Введите границу для загаданного числа: "))
        if N < 2:
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Введите целое положительное число > 1")
        logging.error(" Error. Invalid 'N'", exc_info=True)
logging.info(f" Verhnyaya granica dlya zagadannogo cisla = {N}")

while True:
    try:
        k = int(input("Введите число попыток: "))
        if k < 1:
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Введите целое положительное число > 0")
        logging.error(" Error. Invalid 'k'", exc_info=True)
logging.info(f" Attepts given = {k}")


zagadal = random.randint(1, N)
logging.info(f" Zagadannoe number = {zagadal}")


number = 0
popitki = 0
while number != zagadal:
    print(f"Оставшиеся попытки: {k}")
    logging.info(f" Attempts left: {k}")
    
    if k == 0:
        print(f"Увы, попытки кончились. Я загадывал число {zagadal}")
        logging.info(" No more Attempts, sorry.")
        break
    
    while True:
        try:
            number = int(input("Число: "))
            logging.info(f" Vvedeno number: {number}")
            if number < 1:
                logging.error(" Error. Invalid 'number'", exc_info=True)
                raise ValueError
            break
        except ValueError:
            print("Ошибка. Введите целое число >1")
            logging.error(" Error. Invalid 'number'", exc_info=True)
    
    k -= 1
    popitki += 1
else:
    print(f"Правильно! Кол-во попыток составило: {popitki}. ")
    logging.info(f" Number guessed! Attempts: {popitki}")