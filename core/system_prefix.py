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

logger = log.get_logger(__name__)


class System:
    def __init__(self):
        self.__os_release = platform.freedesktop_os_release()
        self.__envs = os.environ
        self.__os_name = self.__os_release.get('ID')
        self.__os_pretty_name = self.__os_release.get('PRETTY_NAME')
        self.__de = self.__envs['XDG_CURRENT_DESKTOP']
        self.__password = None

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
            password = self.set_pass()
            return password
        else:
            return self.__password

    def set_pass(self):
        if self.__password == None:
            self.__password = getpass.getpass('Enter password: ')
            return self.__password
        else:
            return self.__password

    def get_env(self, key: str):
        try: 
            return(self.__envs[key])
        except: 
            print('Variable is not find!')

    def set_env(self, key: str, value: str):
        pass

    def get_pkg_manager():
        pass