from core.pkg_managers.universal_manager import UniversalManager
from core.utils.enums import PKGManagers as pkgm

class Pacman(UniversalManager):
    def __init__(self):
        self.base = pkgm.pacman
        self.support_atrs = (

        )
    
    def __str__(self) -> str:
        return self.__class__.__name__