from enum import Enum
from core.pkg_managers.managers import Pacman
from core.utils.enums import PKGManagers as pkgm
from core.utils.enums import Systems as sys

class DefaultPkgManagers(Enum):
    apt = (sys.ubuntu, sys.debian)
    pacman = (sys.manjaro, sys.arch, sys.antegros)
    dnf = (sys.fedora)


def get_manager(name: str):
    '''
    Method for providing a package manager class via a string argument id
    '''
    if name == pkgm.pacman:
        return Pacman()
    elif name == pkgm.apt:
        return 'Not implement'
    else:
        return None


def get_pkg_manager(os_name: str):
    '''
    Helper method for getting the package manager class by parsing the os name
    '''
    for manager in DefaultPkgManagers:
        if os_name in manager.value:
            return get_manager(manager.name)
   
    raise Exception('No manager specified for this os name!')

