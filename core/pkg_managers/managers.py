from core.pkg_managers.universal_manager import UniversalManager
from core.utils.enums import PKGManagers as pkgm

class Pacman(UniversalManager):
    def __init__(self):
        self.base = pkgm.pacman
        self.commands = {
            'pamac' : ['-b', '--dbpath']
        }

    def install(self, app_id: str) -> str:
        cmd = f'{self.base} -S {app_id}'
        return cmd
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Snap(UniversalManager):
    pass


class Flatpak(UniversalManager):
    pass