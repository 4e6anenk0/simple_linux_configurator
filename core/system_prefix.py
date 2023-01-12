'''
Системний префікс - це клас, який створюється автоматично під час ініціалізації виконання скрипту, та вказує
конфігуратору потрібні дані, такі як: тип системи, DE, змінні середовища, тощо.

Саме на цей префікс йде посилання, коли ми виконуємо: apply(config, System())

Перелік systems містить мітки, які використовуются для конкретизації власних скриптів відповідно 
цільової системи. Якщо мітка не вказана, то зазвичай виконується скрипт до усіх можливих середовищ.
'''

import platform
import os

class System:
    def __init__(self):
        self.__os_release = platform.freedesktop_os_release()
        self.__envs = os.environ
        self.name = self.__os_release.get('ID')
        self.pretty_name = self.__os_release.get('PRETTY_NAME')
        self.de = self.__envs['XDG_CURRENT_DESKTOP']

    def get_env(self, key: str):
        try: 
            return(self.__envs[key])
        except: 
            print('Variable is not find!')

    def set_env(self, key: str, value: str):
        pass

    def get_pkg_manager():
        pass



