import re
import os
address = "255.255.265.255"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

import logging


logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(message)s')

def valid_IPV_4(address: str, log_error: bool = True) -> bool:
    error_message = ""

    address = address.strip()
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    if not re.match(pattern, address):
        error_message = "Ошибка формата адреса"
    else:
        for octet in address.split('.'):
            if int(octet) > 255:
                error_message = "Неверный адрес"
                break

    # Запись ошибки в лог-файл только если log_error=True
    if error_message and log_error:
        logging.error(f"{address} - {error_message}")
        return False
    return not error_message


def valid_file(file_path: str) -> (list, int):
    """Проверяет IPv4 адреса из файла и возвращает список корректных адресов и количество некорректных."""
    valid_ips = []
    invalid_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if valid_IPV_4(line):
                valid_ips.append(line.strip())
            else:
                invalid_count += 1  # Увеличиваем счетчик некорректных адресов

    return valid_ips, invalid_count

def input_and_save_ip(file_path: str):
    """Запрашивает у пользователя IPv4 адрес, проверяет его и добавляет в файл, если он корректен."""
    while True:
        address = input("Введите IPv4 адрес")
        if valid_IPV_4(address):
            with open(file_path, 'a') as file:
                file.write(f"{address}\n")
            print(f"Адрес {address} сохранен в файл.")
            break
        else:
            print("Неверный адрес. Попробуйте снова.")


def display_menu():

    while True:
        print("\n--- Меню ---")
        print("1. Ввести и сохранить новый IPv4 адрес")
        print("2. Проверить IPv4 адреса из файла")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            file_path = input("Введите имя файла для сохранения адреса: ")
            input_and_save_ip(file_path)
        elif choice == '2':
            while True:
                file_path = input("Введите имя файла с IP-адресами для проверки: ")
                if not os.path.exists(file_path):
                    print(f"не найден файл {file_path}")
                else:
                    break
            valid_ips, invalid_count = valid_file(file_path)
            if valid_ips:
                print("Корректные IP-адреса:")
                for ip in valid_ips:
                    print(ip)
            else:
                print("Нет корректных IP-адресов в файле.")

            # Уведомление о некорректных IP-адресах
            if invalid_count > 0:
                print(f"Обнаружены некорректные IP-адреса. Проверьте лог файл 'errors.log'.")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
#clear_file(file_path)


display_menu()