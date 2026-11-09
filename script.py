# Завдання 3

from pathlib import Path
import sys
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)


def visualize_directory(path_str, level=0):
    target_path = Path(path_str)

    # Перевірка наявності шляху та того, чи є він директорією
    if not target_path.exists():
        print(
            f"{Fore.RED}Помилка: Шлях '{path_str}' не існує."
        )
        return
    if not target_path.is_dir():
        print(
            f"{Fore.RED}Помилка: Шлях '{path_str}' не є директорією."
        )
        return

    indent = "  " * level
    if level == 0:
        print(f"{Style.BRIGHT}{Fore.CYAN}{target_path.name}/")
    else:
        print(f"{indent}{Style.BRIGHT}{Fore.CYAN}{target_path.name}/")

    # Обхід вмісту директорії
    try:
        entries = sorted(
            list(target_path.iterdir()), key=lambda x: (not x.is_dir(), x.name)
        )

        for entry in entries:
            entry_indent = "  " * (level + 1)
            if entry.is_dir():
                # Рекурсивний виклик для піддиректорій
                visualize_directory(entry, level + 1)
            else:
                print(
                    f"{entry_indent}{Fore.GREEN}{entry.name}"
                )

    except PermissionError:
        print(
            f"{'  ' * (level + 1)}{Fore.RED} Доступ до директорії обмежено."
        )

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python script.py <шлях_до_директорії>")
        return

    dir_path = sys.argv[1]
    visualize_directory(dir_path)

if __name__ == "__main__":
    main()