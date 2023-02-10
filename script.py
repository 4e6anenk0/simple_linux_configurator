#!/usr/bin/env python3

'''
from config import config

# init System
system = System()


system.apply(config)
'''

from pathlib import Path
from core.base_cmd import BaseCmd
from core.configurator import BaseConfigurator, Configurator
from core.pkg_managers.flatpak import Flatpak
from core.system import FakeSystem
from core.utils.enums import Systems, PKGManagers, DE
from core.settings import settingsObj, init_settings

#system = System()
""" settings.init() """
""" settingsObj.init() """
""" init_settings() """

#print(settings.localization['lang'])


""" cmd = BaseCmd() """
#cmd.run('ls -a /')
#cmd.root.run('cp -rf /usr/share/themes/. /home/$USER/test', password='7991')
#cmd.run('ls -l', password='7991', root=True)
#cmd.run('ls -l')
""" result = cmd.run('lb -a /')
output, error = cmd.decode(result)
print(f'Errors: {error}, Outputs: {output}') """
""" result = cmd.root_run('lb -a /', password='7991')
#print(result.stdout.decode('utf-8'))
output, error = cmd.decode(result)
print(f'Errors: {error}, Outputs: {output}') """

""" result = cmd.root_run('lb -a /', password='7991')
output, error = cmd.decode(result)
print(f'Errors: {error}, Outputs: {output}') 
 """

'''
Для того чтобы передать набор опций в конфигурацию, необходимо обратиться к пакетному менеджеру
и классу уоманды и выбрать опцию:
Manager.Operation.option(args)
'''



#fake_sys = FakeSystem(os_name=Systems.ubuntu, de=DE.gnome)
cnf = Configurator()
#print(cnf.system)
#cnf.run('ls -a /')
cnf.flatpak.install('org.gabmus.hydrapaper', [Flatpak.Install.subpath(Path('/usr/bin/')), Flatpak.Install.user()])
cnf.flatpak.remove('org.gabmus.hydrapaper', [Flatpak.Uninstall.user()])
cnf.flatpak.update()
cnf.flatpak.add_repo('flathub', 'https://flathub.org/repo/flathub.flatpakrepo')
cnf.flatpak.remove_repo('flathub')
cnf.flatpak.purge('org.gabmus.hydrapaper')
cnf.flatpak.add_cmd(Flatpak.Config(), [Flatpak.Config.user()])
""" cnf.flatpak.remove('org.gabmus.hydrapaper')
cnf.ubuntu.gnome.test('TEST!') """
cnf.flatpak.install('org.gabmus.hydrapaper')
""" cnf.flatpak.update() """
#cnf.run('ls -a /')
#cnf.sudo.run('ls -a /')


""" cnf.update_configuration()
print(cnf) """
configuration = cnf._extract_configs(os_name=Systems.manjaro, de=DE.gnome)

for el in configuration:
    print(el)

#print(cnf.system.de)


#cnf.manager

#cnf.apply() 

#cmd.a_run('ls -a /', password='7991')
#cmd.shellroot_run_cmd('ls -a /', password='7991')

""" 

cmd.chained_run('ls -a', 'grep venv')

cnf.run('ls -a').run('grep venv')
cnf.install('package', 'package1')
cnf.ubuntu.apt.install()
cnf.ubuntu.install()
cnf.ubuntu.snap.instal()
cnf.restart()
cnf.flatpak.install('package_id')
cnf.flatpak.chain('aaa').chain('aaa').cmd
cnf.flatpak(args).install(args, app)
cnf.snap.install('package')
cnf.add_extension('extension_url')
cnf.add_env(key = key, value = value)
cnf.apply()


cnf.flatpak.install('package_id')

cnf.ubuntu.snap.install(p)
cnf.fedora.flatpak.install(p)

sudo snap install p
sudo flatpak install p


"""

'''
conf = Configurator()
conf.install()
conf.delete()
conf.apply(system)
'''
