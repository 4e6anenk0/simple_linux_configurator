#!/usr/bin/env python3

'''
from config import config

# init System
system = System()


system.apply(config)
'''

from core.configurator import Configurator

#system = System()
""" settings.init() """
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

""" result = cmd.root_run('lb -a /', password='7991', shell=True)
output, error = cmd.decode(result)
print(f'Errors: {error}, Outputs: {output}') """

cnf = Configurator()
#cnf.run('ls -a /')
#cnf.run('ls -a /')
cnf.sudo.run('ls -a /')

cnf.apply()




#cmd.a_run('ls -a /', password='7991')

#cmd.shellroot_run_cmd('ls -a /', password='7991')



""" 

cmd.chained_run('ls -a', 'grep venv')

cnf.run('ls -a').run('grep venv')
cnf.install('package')
cnf.flatpak.install('package_id')
cnf.snap.install('package')
cnf.add_extension('extension_url')
cnf.add_env(key = key, value = value)
cnf.apply()

"""

'''
conf = Configurator()
conf.install()
conf.delete()
conf.apply(system)
'''
