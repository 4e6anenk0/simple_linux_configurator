'''
Системний префікс - це клас, який створюється автоматично під час ініціалізації виконання скрипту, та вказує
конфігуратору потрібні дані, такі як: тип системи, DE, змінні середовища, тощо.

Саме на цей префікс йде посилання, коли ми виконуємо: apply(config, System())

Перелік systems містить мітки, які використовуются для конкретизації власних скриптів відповідно 
цільової системи. Якщо мітка не вказана, то зазвичай виконується скрипт до усіх можливих середовищ.
'''

import platform
import getpass
import os
from core import log
from core.pkg_managers.manager_provider import *
from core.pkg_managers.universal_manager import UniversalManager
from core.utils.enums import DE

logger = log.get_logger(__name__)


class BaseSystem:
    def __init__(self, os_name: str, os_pretty_name: str, de: str, manager: UniversalManager = None):
        self.__os_name = os_name
        self.__os_pretty_name = os_pretty_name
        self.__de = de
        self.__manager = manager

    @property
    def os_pretty_name(self):
        return self.__os_pretty_name

    @property
    def os_name(self):
        return self.__os_name

    @property
    def de(self):
        return self.__de

    def _try_get_pkg_manager(self):
        try:
            return get_pkg_manager(self.os_name)
        except:
            logger.warning(
                f'No pakage managers specified for host: {self.os_name}')
            raise Exception()

    @property
    def manager(self) -> UniversalManager:
        '''
        Property to get the manager value set in the system class. 
        If the manager has not been set, then the first time the property is accessed, 
        an attempt will be made to set the manager
        '''
        if self.__manager == None:
            logger.debug("Define the package manager...")
            try: 
                self.__manager = self._try_get_pkg_manager()
                return self.__manager
            except:
                logger.warning(
                    "The package manager wrapper may not yet be defined for your system")
        else:
            return self.__manager


class System(BaseSystem):
    def __init__(self):
        self.__password = None
        self.__os_release = platform.freedesktop_os_release()
        self.__envs = os.environ

        system_os_name = self.__os_release.get('ID')
        system_os_pretty_name = self.__os_release.get('PRETTY_NAME')
        system_de = self.__envs['XDG_CURRENT_DESKTOP']
        
        super().__init__(system_os_name, system_os_pretty_name, system_de)

    @property
    def password(self):
        '''
        Property to get the password value set in the system class. 
        If the password has not been set, then the first time the property is accessed, 
        an attempt will be made to set the password
        '''
        if self.__password == None:
            logger.warning(
                'You need to provide a password to execute privileged commands... ')
            try:
                password = self.get_pass()
            except:
                logger.error('Failed to get superuser password!')
                return
            
            self.__password = password
            return password
        else:
            return self.__password

    def get_pass(self):
        '''
        Get password from console input
        '''
        return getpass.getpass('Enter password: ')
        
    def set_pass(self):
        '''
        Set password. If it already exists then override with new value
        '''
        self.__password = getpass.getpass('Enter password: ')
           
    def get_env(self, key: str):
        try: 
            return(self.__envs[key])
        except: 
            print('Variable is not find!')

    def set_env(self, key: str, value: str):
        pass


class FakeSystem(BaseSystem):
    def __init__(self, os_name: str, de: str = DE.generic, envs: dict[str, str] = {}):
        self.__envs = envs
        
        super().__init__(os_name, 'FakeSystem', de)

    def get_env(self, key: str):
        try:
            return (self.__envs.get[key])
        except:
            print('Variable is not find!')

# logger.info("The system's package manager is defined as: ") 

'''
class System(DefaultSystem):
    def __init__(self):
        self.__os_release = platform.freedesktop_os_release()
        self.__envs = os.environ
        self.__os_name = self.__os_release.get('ID')
        self.__os_pretty_name = self.__os_release.get('PRETTY_NAME')
        self.__de = self.__envs['XDG_CURRENT_DESKTOP']
        self.__password = None
        self.__manager = None

    @property
    def os_pretty_name(self):
        return self.__os_pretty_name

    @property
    def os_name(self):
        return self.__os_name

    @property
    def de(self):
        return self.__de

    @property
    def password(self):
        
        if self.__password == None:
            logger.warning(
                'You need to provide a password to execute privileged commands... ')
            try:
                password = self.get_pass()
            except:
                logger.error('Failed to get superuser password!')
                return
            
            self.__password = password
            return password
        else:
            return self.__password

    def get_pass(self):
        
        return getpass.getpass('Enter password: ')
        

    def set_pass(self):
        
        self.__password = getpass.getpass('Enter password: ')
           
    def get_env(self, key: str):
        try: 
            return(self.__envs[key])
        except: 
            print('Variable is not find!')

    def set_env(self, key: str, value: str):
        pass

    def _get_os_pkg_manager(self):
        
        try:
            for manager in DefaultPkgManagers:
                if self.os_name in manager.value:
                    return get_manager(manager.name)
        except:
            logger.info('Error')

    def get_pkg_manager(self, os_name: str):
        
        try:
            for manager in DefaultPkgManagers:
                if os_name in manager.value:
                    return get_manager(manager.name)
        except:
            logger.info('Error')  

    @property
    def manager(self) -> UniversalManager:
        
        if self.__manager == None:
            logger.debug("Define the package manager...")

            try:
                manager = self._get_os_pkg_manager()
                if manager:
                    self.__manager = manager
                    return manager
                else:
                    logger.warning(
                        'Could not find a package manager for the target system')
                    
            except:
                logger.warning(
                    'The [manager] attribute is None!')

        else:
            return self.__manager
'''