from pathlib import Path
from core import log
from core.utils.cli_elements import Operation, Option
from core.utils.enums import PKGManagers as pkgm


class UniversalManager:

    @classmethod
    def install(cls, argument: str = None, options: list[Option] = None) -> str:
        pass

    @classmethod
    def remove(cls, argument: str = None, options: list[Option] = None) -> str:
        pass

    @classmethod
    def update(cls, argument: str = None, options: list[Option] = None) -> str:
        pass

class Pacman(UniversalManager):
    def __init__(self):
        self.base = pkgm.pacman
        self.commands = {
            'pamac' : ['-b', '--dbpath']
        }
        self.assume = '--noconfirm'

    def install(self, app_id: str) -> str:
        cmd = f'{self.base} {self.assume} -S {app_id}'
        return cmd

    def remove(self, app_id: str) -> str:
        cmd = f"{self.base} {self.assume} -R {app_id}"
        return cmd
    
    def update(self) -> str:
        cmd = f"{self.base} {self.assume} -Syyu"
        return cmd
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Snap(UniversalManager):
    pass



