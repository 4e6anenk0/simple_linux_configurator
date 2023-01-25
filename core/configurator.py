'''
Конфігуратор - це клас, який зберігає набір конфігураційних команд, та виконує їх зі специфікою ОС.

Також, цей клас містить метод для створення цільного конфігураційного sh скрипту за потребою.

Цей клас виконує головний функіональний цикл з конфігурації системи, крок за кроком проводячи користувача
по візульному процессу до завершення. Також, цей клас зберігає інформацію о кількості виконаних команд,
та у разі повторного запуску виконує лише ті команди, які не були виконані.
'''

from core.system_prefix import System
from core.settings import settings
from core.commands import *


class Configurator:
    def __init__(self):
        settings.init()
        self.settings = settings
        self.system = System()
        self.commands = [BaseCmd]
        self.install_descriptor = 'default'
        self.sudo_descriptor = False

    def run(self, cmd: str):
        if self.sudo_descriptor == False:
            self.commands.append(Run(cmd))
        else:
            self.commands.append(RootRun(cmd, self.system))
        self.sudo_descriptor = True

    """ def install(self, app_id):
        if self.install_descriptor == 'default':
            self.commands.append(InstallCmd(app_id))
        elif self.install_descriptor == 'flatpak':
            self.commands.append(InstallCmd(app_id, self.install_descriptor)) """

    @property
    def sudo(self):
        self.sudo_descriptor = True

        return self

    def install():
        pass

    def apply(self):
        for cmd in self.commands:
            cmd.apply()
        logger.info('Configuration completed!!!')

