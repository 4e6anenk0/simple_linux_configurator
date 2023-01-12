'''
from config import config

# init System
system = System()


system.apply(config)
'''

from core.base_cmd import BaseCmd
from core.system_prefix import System

system = System()

cmd = BaseCmd()
#cmd.run('ls -a /')
#cmd.root.run('cp -rf /usr/share/themes/. /home/$USER/test', password='7991')
cmd.root_run('ls -l', password='7991')
cmd.run('ls -l')
'''
conf = Configurator()
conf.install()
conf.delete()
conf.apply(system)
'''
