import time
from random import randint
"""Program simulates a Climate System with some user name interaction."""


# Welcome message
def climate_buddy():
    msg1 = "ClimateBuddy te da la bienvenida!"
    print(msg1)
    time.sleep(1)
    user = input("Cómo te llamas?: ")
    welcome_msg = f"Bienvenido {user.title()}!"
    print(welcome_msg)

    # Starting app message
    time.sleep(1)
    print("ClimateBuddy está iniciando...")
    starting_counter = 0
    while starting_counter < 3:
        print("Escaneando la Temperatura...")
        starting_counter += 1
        time.sleep(2)
    # temperaturas frías: calentar
    temp_below_0_msg = "Wow, está congelante hoy!"
    temp_1_to_10_msg = "Que frío está haciendo!"
    temp_11_15_msg = "Está templado hoy, quiere un poco más de calor?"
    current_temp_msg = "Temperatura actual: "
    heating_msg = "Calentando..."
    temp_20_msg = f"La Temperatura ahora es: 20°"

    # temperaturas excesos
    temp_input_limit_msg = "El valor excede los límites "

    current_temp = randint(-10, 15)
    if current_temp <= 0:
        print(f"{temp_below_0_msg} {current_temp_msg} {current_temp}°")
        while current_temp < 20:
            print(f"{heating_msg} {current_temp_msg} {current_temp}°")
            current_temp += 1
            time.sleep(3)

            if current_temp == 20:
                print(temp_20_msg)


    elif (current_temp >= 1) and (current_temp < 11):
        print(f"{temp_1_to_10_msg} {current_temp_msg} {current_temp}°")
        while current_temp < 20:
            print(f"{heating_msg} {current_temp_msg} {current_temp}°")
            current_temp += 1
            time.sleep(3)

            if current_temp == 20:
                print(temp_20_msg)

    elif (current_temp > 10) and (current_temp < 16):
        print(f"{temp_11_15_msg} {current_temp_msg} {current_temp}°")
        while current_temp < 20:
            print(f"{heating_msg} {current_temp_msg} {current_temp}°")
            current_temp += 1
            time.sleep(3)

            if current_temp == 20:
                print(temp_20_msg)

    print("Entrando en Modo Ahorrador.")
    sleep_counter = 0
    while sleep_counter <2:
        print(".")
        sleep_counter += 1
        time.sleep(2)

    print("Status: Mode Ahorrador")




climate_buddy()


