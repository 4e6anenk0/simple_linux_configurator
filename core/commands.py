from core.pkg_managers.managers import ManagerOperation
from core.pkg_managers.managers import UniversalManager
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

f'The [{self.cmd}] command is running...'

Command execution failed!
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


""" class TemplateForManagerInstallMixin:

    def run_implementation(self):
        pass

    def template(self):
        logger.info(f'Trying to install the program: {self.app_id}')
        try:
            self.run_implementation()
        except:
            logger.error(f'The {self.app_id} failed to install!')
            return
        logger.info('Success!') """


class Run(BaseCmd, TemplateMixin):
    def __init__(self, cmd: str, system: BaseSystem, silent: bool = False):
        self.silent_install = silent
        super().__init__(cmd)

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
        self.system = system
        self.silent_install = silent
        super().__init__(cmd)

    def run_implementation(self):
        password = self.system.password
        completed = self.root_run(self.cmd, password)

        if self.silent_install == False:
            output, _ = self.decode(completed)

            if output:
                logger.info(f'\n{output}')
    
    def apply(self):
        self.template()


""" class DefaultInstall(BaseCmd, TemplateForManagerInstallMixin):
    def __init__(self, app_id: str, system: BaseSystem):
        self.system = system
        self.manager = system.manager
        self.app_id = app_id
        super().__init__(self.manager.install(app_id))
        
    def run_implementation(self):
        password = self.system.password
        # обоити запрос ввода "у"
        completed = self.root_run(self.cmd, password)

    def apply(self):
        self.template() """


""" class ManagerInstall(BaseCmd, TemplateForManagerInstallMixin):
    def __init__(self, app_id: str, system: BaseSystem, manager: UniversalManager,  silent_install=False):
        self.manager = manager
        self.system = system
        self.app_id = app_id
        self.silent_install = silent_install
        super().__init__(self.manager.install(app_id=app_id))

    def run_implementation(self):
        if self.system.target == True:
            password = self.system.password
            completed = self.root_run(self.cmd, password)

            if self.silent_install == False:
                output, _ = self.decode(completed)

                if output:
                    logger.info(f'\n{output}')
    
    def apply(self):
        self.template() """


# реализовать фабрику, которая будет генерировать нужные классы

class TemplateForProviderMixin:

    def run_implementation(self):
        pass

    def template(self, pre: str, err: str):
        logger.info(pre)
        try:
            self.run_implementation()
        except:
            logger.error(err)
            return
        logger.info('Success!')

class ManagerCmd(BaseCmd, TemplateForProviderMixin):
    def __init__(self, cmd: str, system: BaseSystem, pre: str, err: str, silent: bool = False):
        self.pre = pre
        self.err = err
        self.silent = silent
        self.system = system
        super().__init__(cmd)
    
    def run_implementation(self):
        if self.system.target == True:
            password = self.system.password
            completed = self.root_run(self.cmd, password)

            if self.silent == False:
                output, _ = self.decode(completed)

                if output:
                    logger.info(f'\n{output}')
        else:
            logger.error('Unable to execute command on non-target system!')

    def apply(self):
        self.template(pre=self.pre, err=self.err)

class ManagerProvider:
    def __init__(self, system: BaseSystem, manager: UniversalManager = None, silent: bool = False) -> None:
        if not manager:
            self.__manager = system.manager
        else:
            self.__manager = manager
        self.system = system
        self.silent = silent
        
    def install(self, app_id: str) -> ManagerCmd:
        cmd = self.__manager.install(app_id)
        #cmd = self.__manager.install(app_id)
        pre_msg = f'Trying to install the program: {app_id}'
        err_msg = f'The {app_id} failed to install!'
        return ManagerCmd(cmd, self.system, pre_msg, err_msg, self.silent)

    def remove(self, app_id: str) -> ManagerCmd:
        #cmd = self.__manager.remove(app_id)
        cmd = self.__manager.remove(app_id)
        pre_msg = f'Trying to remove the program: {app_id}'
        err_msg = f'The {app_id} failed to remove!'
        return ManagerCmd(cmd, self.system, pre_msg, err_msg, self.silent)

    def update(self) -> ManagerCmd:
        #cmd = self.__manager.update()
        cmd = self.__manager.update()
        pre_msg = f'Trying to update apps...'
        err_msg = f'The failed to update!'
        return ManagerCmd(cmd, self.system, pre_msg, err_msg, self.silent)

    def cmd(self, cmd: str, pre_msg: str, err_msg: str) -> ManagerCmd:
        return ManagerCmd(cmd, self.system, pre_msg, err_msg, self.silent)

""" class ManagerInstall(BaseCmd, TemplateForPkgManagerMixin):
    def __init__(self, app_id: str, system: BaseSystem, manager: UniversalManager = None, silent: bool = False):
        if not manager:
            self.manager = system.manager
        else: 
            self.manager = manager
        self.system = system 
        self.app_id = app_id
        self.silent = silent
        super().__init__(self.manager.install(app_id))
    
    def apply(self):
        self.template(
            self.cmd, pre=f'Trying to install the program: {self.app_id}', err=f'The {self.app_id} failed to install!')


class ManagerRemove(BaseCmd, TemplateForPkgManagerMixin):
    def __init__(self, app_id: str, system: BaseSystem, manager: UniversalManager = None, silent: bool = False):
        self.manager = manager
        self.system = system
        self.app_id = app_id
        self.silent = silent
        super().__init__(self.manager.remove(app_id))

    def apply(self):
        self.template(
            self.cmd, pre=f'Trying to remove the program: {self.app_id}', err=f'The {self.app_id} failed to remove!')


class Remove(BaseCmd, TemplateForManagerInstallMixin):
    def __init__(self, app_id: str, manager: UniversalManager, system: BaseSystem, silent = False):
        self.manager = manager
        self.system = system
        self.app_id = app_id
        self.silent = silent
        super().__init__(self.manager.remove(app_id=app_id))

    def run_implementation(self):
        password = self.system
 """