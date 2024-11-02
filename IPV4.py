import re
import os

import logging


logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(message)s')

class IPValidator:
    def __init__(self):
        pass

    @staticmethod
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

        if error_message and log_error:
            logging.error(f"{address} - {error_message}")
            return False
        return not error_message

    @staticmethod
    def valid_file(file_path: str) -> (list, int):
        valid_ips = []
        invalid_count = 0

        with open(file_path, 'r') as file:
            for line in file:
                if IPValidator.valid_IPV_4(line):
                    valid_ips.append(line.strip())
                else:
                    invalid_count += 1

        return valid_ips, invalid_count

    @staticmethod
    def input_and_save_ip(file_path: str):
        while True:
            address = input("Введите IPv4 адрес: ")
            if IPValidator.valid_IPV_4(address):
                with open(file_path, 'a') as file:
                    file.write(f"{address}\n")
                print(f"Адрес {address} сохранен в файл.")
                break
            else:
                print("Неверный адрес. Попробуйте снова.")

    def display_menu(self):
        while True:
            print("\n--- Меню ---")
            print("1. Ввести и сохранить новый IPv4 адрес")
            print("2. Проверить IPv4 адреса из файла")
            print("3. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                file_path = input("Введите имя файла для сохранения адреса: ")
                self.input_and_save_ip(file_path)
            elif choice == '2':
                while True:
                    file_path = input("Введите имя файла с IP-адресами для проверки: ")
                    if not os.path.exists(file_path):
                        print(f"Не найден файл {file_path}")
                    else:
                        break
                valid_ips, invalid_count = self.valid_file(file_path)
                if valid_ips:
                    print("Корректные IP-адреса:")
                    for ip in valid_ips:
                        print(ip)
                else:
                    print("Нет корректных IP-адресов в файле.")

                if invalid_count > 0:
                    print(f"Обнаружены некорректные IP-адреса. Проверьте лог файл 'errors.log'.")
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    validator = IPValidator()
    validator.display_menu()