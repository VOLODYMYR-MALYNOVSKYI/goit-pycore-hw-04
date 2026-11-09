# Завдання 1

# Файл із даними про працівників та їх зарплатами (який вказано в мене, для перевірки роботи коду)

path = "/Users/koristuvac/Documents/GOIT/Python/Home_work/sellary_file.txt"

def total_salary(path):
    total_sum = 0
    count = 0

    try:

        # Обчислюємо суму зарплат та кількість працівників

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    total_sum += int(parts[1])
                    count += 1

        # Обчислюємо середню зарплату

        if count == 0:
            return 0, 0

        average_salary = total_sum / count
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return None, None
    except ValueError:
        print("Помилка: Файл містить пошкоджені дані або некоректний формат чисел.")
        return None, None

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Завдання 2

# Файл із даними про працівників та їх зарплатами (який вказано в мене, для перевірки роботи коду)

path = "/Users/koristuvac/Documents/GOIT/Python/Home_work/cats_document.txt"

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    
                    # Створюю словник із ключами id, name та age

                    cat_dict = {
                        "id": parts[0].strip(),
                        "name": parts[1].strip(),
                        "age": parts[2].strip(),
                    }
                    cats_info.append(cat_dict)
                else:
                    raise ValueError(f"Помилка: Файл містить пошкоджені дані або не повну інформацію: {line.strip()}")
        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return []

cats_info = get_cats_info(path)
print(cats_info)

# Завдання 3

# завдання 3 реалізовано у файлі script.py

# Завдання 4

# Допоміжні функції

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: enter name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: enter name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: enter contact name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: contact not found."


def show_all(contacts):
    if not contacts:
        return "Error: no contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

# Головна функція для взаємодії з користувачем

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()