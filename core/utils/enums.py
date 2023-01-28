from enum import Enum


class DE(str, Enum):
    '''
    Enum describing supporting desktop environment for configuration
    '''
    generic = 'X-GENERIC'
    gnome = 'GNOME'
    gnome_classic = 'GNOME-CLASSIC'
    kde = 'KDE'
    lxde = 'LXDE'
    lxqt = 'LXQT'
    mate = 'MATE'
    xfce = 'XFCE'
    cinnamon = 'CINNAMON'
    deepin = 'DEEPIN'

class PKGManagers(str, Enum):
    '''
    Enum describing supporting package managers for configuration
    '''
    pacman = 'pacman'
    flatpak = 'flatpak'
    snap = 'snap'
    dnf = 'dnf'
    yuy = 'yuy'
    yum = 'yum'
    zypper = 'zypper'
    apt = 'apt'
    apt_get = 'apt-get'

class Systems(str, Enum):
    '''
    Enum describing supporting systems for configuration
    '''
    debian = 'debian'
    arch = 'arch'
    fedora = 'fedora'
    manjaro = 'manjaro'
    ubuntu = 'ubuntu'
    antegros = 'antegros'
