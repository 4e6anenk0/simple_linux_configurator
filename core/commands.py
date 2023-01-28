from .base_cmd import BaseCmd
from core.system import BaseSystem, System
from core import log

logger = log.get_logger(__name__)


'''
Declarative commands for creating a configuration list. 
These commands store the specifics of the called system and 
forward the ready-made string commands to the implementation of the base command, 
where they are called by the system.

Frontend commands for declarative configuration.

Для создания класса команды, унаслежуйте базовую команду [BaseCmd] и смешайте класс с миксином TemplateMixin. Реализуйте метод 
[run_implementation()] в котором используйте методы базовой команды. Также реализуйте метод apply() в котором вызовете метод 
[template()]
'''

class TemplateMixin:

    def run_implementation(self):
        pass

    def template(self):
        logger.info(f'The [{self.cmd}] command is running...')
        try:
            self.run_implementation()
        except:
            logger.error('Command execution failed!')
            return
        logger.info('Success!')


class Run(BaseCmd, TemplateMixin):
    def __init__(self, cmd: str, silent: bool = False):
        self.cmd = cmd
        self.silent_install = silent

    def run_implementation(self):
        
        completed = self.run(self.cmd)

        if self.silent_install == False:
            output, _ = self.decode(completed)

            if output != None:
                logger.info(f'\n{output}')
    
    
    def apply(self):
        self.template()


class RootRun(BaseCmd, TemplateMixin):
    def __init__(self, cmd: str, system: BaseSystem, silent: bool = False):
        self.cmd = cmd
        self.system = system
        self.silent_install = silent

    def run_implementation(self):
        password = self.system.password
        completed = self.root_run(self.cmd, password)

        if self.silent_install == False:
            output, _ = self.decode(completed)

            if output:
                logger.info(f'\n{output}')
    
    def apply(self):
        self.template()


class Install(BaseCmd, TemplateMixin):
    def __init__(self, app_id: str, system: BaseSystem):
        self.system = system
        self.manager = system.manager
        self.cmd = self.manager.install(app_id)
        self.app_id = app_id
        
    def run_implementation(self):
        password = self.system.password
        # обоити запрос ввода "у"
        completed = self.root_run(f'{self.cmd}', password)

    def apply(self):
        self.template()
