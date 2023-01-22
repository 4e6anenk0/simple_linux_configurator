'''
Конфігуратор - це клас, який зберігає набір конфігураційних команд, та виконує їх зі специфікою ОС.

Також, цей клас містить метод для створення цільного конфігураційного sh скрипту за потребою.

Цей клас виконує головний функіональний цикл з конфігурації системи, крок за кроком проводячи користувача
по візульному процессу до завершення. Також, цей клас зберігає інформацію о кількості виконаних команд,
та у разі повторного запуску виконує лише ті команди, які не були виконані.
'''

from core.system_prefix import System
from core.settings import settings
from core.base_cmd import BaseCmd


class Configurator:
    def __init__(self) -> None:
        settings.init()
        self.system = System()
        self.commands = []
        
    def run(self):
        self.commands.append()

    def sudo(self):
        
        
        return self 

    def install():
        pass

    def main_loop(self):
        for cmd in self.commands:
            cmd()

