from pathlib import Path
from core.utils.enums import PKGManagers as pkgm




class ManagerOperation:
    def __init__(self, base: str, operation: str, alias: str = None, default_options: str = None, ending: str = None) -> None:
        self.base = base
        self.operation = operation
        self.alias = alias
        self.default_options = default_options
        self.ending = ending
        self._builded_cmd: list[str] = []
        self._builded_cmd.append(base)
        self._builded_cmd.append(operation)
        self._builded_cmd.append(default_options)
    
    def get(self) -> str:
        cmd = " ".join(self._builded_cmd)
        return cmd

    def __str__(self) -> str:
        return self.base + self.operation
        

class UniversalManager:
    def __init__(self) -> None:
        self.name = ''

    def install(self, app_id: str) -> str:
        pass

    def remove(self, app_id: str) -> str:
        pass

    def update(self) -> str:
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


class Flatpak(UniversalManager):
    def __init__(self):
        self.base = pkgm.flatpak
        self.storage = 'flathub'
        self.assume = '-y --noninteractive'

    def install(self, app_id: str) -> str:
        cmd = f"{self.base} install {self.assume} {app_id}"
        return cmd

    def remove(self, app_id: str) -> str:
        cmd = f"{self.base} uninstall {self.assume} {app_id}"
        return cmd
    
    def update(self) -> str:
        cmd = f"{self.base} update"
        return cmd

    def add_repo():
        pass

    def delete_repo():
        pass

    def __str__(self) -> str:
        return self.__class__.__name__
