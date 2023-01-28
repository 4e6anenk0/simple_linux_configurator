'''
Конфігуратор - це клас, який зберігає набір конфігураційних команд, та виконує їх зі специфікою ОС.

Також, цей клас містить метод для створення цільного конфігураційного sh скрипту за потребою.

Цей клас виконує головний функіональний цикл з конфігурації системи, крок за кроком проводячи користувача
по візульному процессу до завершення. Також, цей клас зберігає інформацію о кількості виконаних команд,
та у разі повторного запуску виконує лише ті команди, які не були виконані.
'''

from core.system import BaseSystem, FakeSystem, System
from core.settings import settings
from core.commands import *
from core.utils.enums import DE, Systems as sys

class Configurator:
    def __init__(self, system: BaseSystem = None):
        self.settings = settings
        if system:
            self.system = system
        else:
            self.system = System()
        self.configuration = [BaseCmd]
        self.install_descriptor = 'default'
        self.sudo_descriptor = False

    def run(self, cmd: str):
        if self.sudo_descriptor == False:
            self.configuration.append(Run(cmd))
        else:
            self.configuration.append(RootRun(cmd, self.system))
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

    def ubuntu(self, de: str = DE.generic):
        os_name = sys.ubuntu
        if self.system.os_name == os_name:
            self.__setattr__(os_name, Configurator())
        else:
            fake_os = FakeSystem(os_name)
            self.__setattr__(os_name, Configurator())

    def print_pkg_manager(self):
        print(self.system.manager)

    def apply(self):
        for cmd in self.configuration:
            cmd.apply()
        logger.info('Configuration completed!!!')