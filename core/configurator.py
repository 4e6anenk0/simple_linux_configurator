'''
Конфігуратор - це клас, який зберігає набір конфігураційних команд, та виконує їх зі специфікою ОС.

Також, цей клас містить метод для створення цільного конфігураційного sh скрипту за потребою.

Цей клас виконує головний функіональний цикл з конфігурації системи, крок за кроком проводячи користувача
по візульному процессу до завершення. Також, цей клас зберігає інформацію о кількості виконаних команд,
та у разі повторного запуску виконує лише ті команди, які не були виконані.
'''

from core.system import BaseSystem, FakeSystem, systemObj
from core.settings import settingsObj
from core.commands import *
from core.utils.enums import DE, Systems as sys
from core.pkg_managers.flatpak import Flatpak
from core.utils.cli_elements import Option

class BaseConfigurator:
    def __init__(self, system: BaseSystem = None, name: str = "base_configurator"):
        if system:
            self.__system = system
        else:
            # если нет системы переданой в этот класс, то установим обьект системы нашего хоста
            self.__system = systemObj
        self.__configuration: list[BaseCmd] = []
        self.__configurators: list[BaseConfigurator] = []
        self.__sudo_descriptor = False
        self.__name = name

    def __str__(self) -> str:
        if self.configuration:
            return '\n'.join(str(cmd.cmd) for cmd in self.configuration)
        else:
            return "Empty configuration list!"

    def add_configurator(self, configurator):
        self.__configurators.append(configurator)

    def register_configurator(self, configurator):
        if configurator in self.configurators:
            return configurator
        else:
            self.add_configurator(configurator)
            return configurator

    @property
    def name(self):
        return self.__name
        
    @property
    def system(self):
        return self.__system

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, configuration: list[BaseCmd]):
        self.__configuration = configuration

    @property
    def configurators(self):
        return self.__configurators

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
        ##  реализовать проверку через system.target
        if self.system.__class__.__name__ == FakeSystem.__name__:
            logger.warning(
                'Cannot execute apply method on non-target machine. Use code generation instead')
            return
        self.update_configuration()
        for cmd in self.configuration:
            cmd.apply()

    def update_configuration(self):
        '''
        Метод для обновления верхнеуровневого конфигуратора коммандами, хранимыми во вложенных конфигураторах
        '''
        try: 
            configuration = self.extract_target_configs()
            self.configuration = configuration
        except:
            logger.error('Failed to update configuration')

        
    def extract_all_configs(self) -> list[BaseCmd]:
        '''
        Метод для рекурсивного обхода всех вложенных конфигураторов и извлечения всех хранимых внутри них комманд
        '''
        configuration = []
        if self.configuration:
            configuration.extend(self.configuration)
        if self.__configurators:
            for cnf in self.__configurators:
                configuration.extend(cnf.extract_all_configs())
            return configuration
        else:
            return configuration

    def extract_target_configs(self) -> list[BaseCmd]:
        '''
        Метод для рекурсивного обхода всех вложенных конфигураторов и извлечения целевых (предназначеных для рабочей ОС) хранимых внутри них комманд
        '''
        configuration = []
        if self.system.target == True:
            if self.configuration:
                configuration.extend(self.configuration)
        if self.__configurators:
            for cnf in self.__configurators:
                if cnf.system.target == True:
                    configuration.extend(cnf.extract_all_configs())
            return configuration
        else:
            return configuration

    def extract_specific_configs(self, os_name: str) -> list[BaseCmd]:
        '''
        Метод для рекурсивного обхода всех вложенных конфигураторов и извлечения хранимых внутри них комманд предназначенных для конкретной ОС
        '''
        configuration = []
        if self.system.os_name == os_name:
            if self.configuration:
                configuration.extend(self.configuration)
        if self.__configurators:
            for cnf in self.__configurators:
                if cnf.system.os_name == os_name:
                    configuration.extend(cnf.extract_all_configs())
            return configuration
        else:
            return configuration

    def _check(self, os_name: str = None, de: str = None, target: bool = None) -> bool:
        check = True
        if os_name:
            if self.system.os_name == os_name:
                check = True
            else:
                return False
        if de:
            if self.system.de == de:
                check = True
            else:
                return False
        if target: 
            if self.system.target == target:
                check = True
            else:
                return False
        return check

    def extract_configs(self, os_name: str = None, de: str = None, target: bool = None):
        configuration = []
        if self._check(os_name, de, target) == True:
            if self.configuration:
                configuration.extend(self.configuration)
        
        if self.configurators:
            for cnf in self.__configurators:
                if cnf._check(os_name, de, target) == True:
                    configuration.extend(
                        cnf.extract_configs(os_name, de, target))
            return configuration
        else:
            return configuration
        
class SnapConfigurator(BaseConfigurator):

    pass

class FlatpakConfigurator(BaseConfigurator):
    def __init__(self, system: BaseSystem = None):
        super().__init__(system, 'flatpak_configurator')
        self.__manager = Flatpak
        self.__provider = ManagerProvider(system, self.__manager) # провайдер, который по запросу позволяет собирать команды с нужным пакетным менеджером

    def install(self, app_id: str, options: list[Option] = None):
        self.configuration.append(self.__provider.install(app_id, options))
    
    def remove(self, app_id: str, options: list[Option] = None):
        self.configuration.append(self.__provider.remove(app_id, options))

    def update(self, options: list[Option] = None):
        self.configuration.append(self.__provider.update(options=options))

    def add_repo(self, name: str, location: str, options: list[Option] = None):
        cmd = self.__manager.remote_add(name=name, location=location, options=options)
        pre_msg = f'Trying to add a repository {name}'
        err_msg = 'Failed to add repository'
        self.configuration.append(self.__provider.cmd(cmd, pre_msg, err_msg))


class UbuntuConfigurator(BaseConfigurator):
    def __init__(self, system: BaseSystem = None):
        super().__init__(system, 'ubuntu_configurator')

    @property
    def gnome(self):
        self.system.de = DE.gnome
        return self

    @property
    def kde(self):
        self.system.de = DE.kde

    def test(self, test_str: str):
        self.configuration.append(Run(test_str, self.system))

class Configurator(BaseConfigurator):
    def __init__(self, system: BaseSystem = None):
        super().__init__(system, 'main_configurator')
        self.settings = settingsObj
        self.__provider = ManagerProvider(self.system)
        self.flatpak_configurator: FlatpakConfigurator = None
        self.snap_configurator: SnapConfigurator = None
        self.ubuntu_configurator: UbuntuConfigurator = None

    @property
    def flatpak(self):
        if self.flatpak_configurator:
            configurator = self.register_configurator(self.flatpak_configurator)
            return configurator
        else:
            self.flatpak_configurator = FlatpakConfigurator(self.system)
            return self.flatpak

    def run(self, cmd: str):
        if self.sudo_descriptor == False:
            self.configuration.append(Run(cmd, self.system))
        else:
            self.configuration.append(RootRun(cmd, self.system))
        self.sudo_descriptor = True

    def install(self, app_id: str):
        self.configuration.append(self.__provider.install(app_id))

    def remove(self, app_id: str):
        self.configuration.append(self.__provider.remove(app_id))

    def update(self):
        self.configuration.append(self.__provider.update())

    @property
    def ubuntu(self):
        os_name = sys.ubuntu
        if self.system.os_name == os_name:
            
            if self.ubuntu_configurator:
                configurator = self.register_configurator(self.ubuntu_configurator)
                return configurator
            else:
                self.ubuntu_configurator = UbuntuConfigurator(self.system)
                return self.ubuntu
        else:
            if self.ubuntu_configurator:
                configurator = self.register_configurator(self.ubuntu_configurator)
                return configurator
            else:
                self.ubuntu_configurator = UbuntuConfigurator(FakeSystem(os_name))
                return self.ubuntu

    def print_pkg_manager(self):
        print(self.system.manager)
