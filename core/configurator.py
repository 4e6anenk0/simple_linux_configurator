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

class BaseConfigurator:
    def __init__(self, system: BaseSystem = None):
        if system:
            self.__system = system
        else:
            self.__system = System()
        self.__configuration: list[BaseCmd] = []
        self.__sudo_descriptor = False

    def __str__(self) -> str:
        if self.configuration:
            return '\n'.join(str(cmd) for cmd in self.configuration)
        else:
            return "Empty configuration list!"
        
    @property
    def system(self):
        return self.__system

    @property
    def configuration(self):
        return self.__configuration

    @property
    def sudo_descriptor(self):
        return self.__sudo_descriptor

    @property
    def sudo(self):
        self.sudo_descriptor = True

        return self

    @sudo_descriptor.setter
    def sudo_descriptor(self, value):
        self.__sudo_descriptor = value

    def apply(self):
        for cmd in self.configuration:
            cmd.apply()
        
class SnapConfigurator(BaseConfigurator):
    pass

class FlatpakConfigurator(BaseConfigurator):
    pass

class Configurator(BaseConfigurator):
    def __init__(self, system: BaseSystem = None):
        self.settings = settings
        
        """ if system:
            self.system = system
        else:
            self.system = System()
        self.configuration = [BaseCmd]
        self.sudo_descriptor = False """
        self.flatpak = FlatpakConfigurator()
        self.snap = SnapConfigurator()
        self.configurators: list[BaseConfigurator] = []
        self.configurators.append(self.snap)
        self.configurators.append(self.flatpak)

        super().__init__(system)

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

    """ @property
    def sudo(self):
        self.sudo_descriptor = True

        return self """

    def install():
        pass

    def ubuntu(self, de: str = DE.generic):
        os_name = sys.ubuntu
        if self.system.os_name == os_name:
            self.__setattr__(os_name, Configurator())
        else:
            fake_os = FakeSystem(os_name, de)
            self.__setattr__(os_name, Configurator(fake_os))

    def print_pkg_manager(self):
        print(self.system.manager)

    """ def apply(self):
        for manager in self.configurators:
            self.configuration.append(manager)
        for cmd in self.configuration:
            cmd.apply()
        logger.info('Configuration completed!!!') """