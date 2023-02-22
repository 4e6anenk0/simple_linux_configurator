from core.utils.cli_elements import Operation, Option
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


class ValidatedCmd:
    def __init__(self, cmd: str) -> None:
        self.__cmd = self.check_valid(cmd)
        self.black_list = ()

    @property
    def cmd(self):
        return self.__cmd

    @cmd.setter
    def cmd(self, cmd: str):
        try:
            self.__cmd = self.check_valid(cmd)
        except:
            logger.warning(
                f'Cannot set a value for a variable because the value did not pass validation!')

    def check_valid(self, cmd: str):
        pass

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

class ProvidedCmd(BaseCmd, TemplateForProviderMixin):
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


class BaseProvider:
    def __init__(self, system: BaseSystem, silent: bool = False) -> None:
        self._system = system
        self._silent = silent

    @classmethod
    def prepare(cls, *params: str) -> str:
        '''A method that allows concatenate arguments into a common string. 
        A single string argument must be passed to the final call to the wrapped package manager method.
        This method helps on the side of client functions that have expanded parameter declarations'''
        list_par = [arg for arg in params]
        str_par = " ".join(list_par)
        return str_par

    def new_cmd(self, cmd: str, pre_msg: str, err_msg: str) -> ProvidedCmd:
        return ProvidedCmd(cmd, self._system, pre_msg, err_msg, self._silent)
        

class ManagerProvider(BaseProvider):
    def __init__(self, system: BaseSystem, manager: UniversalManager = None, silent: bool = False) -> None:
        super().__init__(system, silent)
        if not manager:
            self.__manager = system.manager
        else:
            self.__manager = manager

    @property
    def manager(self):
        return self.__manager

    def get_cmd(self, method_name: str, pre_msg: str, err_msg: str, arg: str = None, options: list[Option] = None, head_options: list[Option] = None) -> ProvidedCmd:
        '''Allows get a command by named id from the required package manager'''
        try:
            method = getattr(self.__manager, method_name)
            if callable(method):
                cmd = method(arg, options, head_options)
                return ProvidedCmd(cmd, self._system, pre_msg, err_msg, self._silent)
        except:
            raise Exception('Failed to get command with manager method!')

    def install(self, arg: str, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to install the program: {arg}'
        err_msg = f'The {arg} failed to install!'
        return self.get_cmd('install', pre_msg, err_msg, arg, options, head_options)

    def remove(self, arg: str, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to remove the program: {arg}'
        err_msg = f'The {arg} failed to remove!'
        return self.get_cmd('remove', pre_msg, err_msg, arg, options, head_options)

    def update(self, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to update apps...'
        err_msg = f'The failed to update!'
        return self.get_cmd('update', pre_msg, err_msg, arg, options, head_options)

    def add_repo(self, arg: str, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to add a repository {arg}'
        err_msg = 'Failed to add repository'
        return self.get_cmd('add_repo', pre_msg, err_msg, arg, options, head_options)

    def remove_repo(self, arg: str, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to remove a repository {arg}'
        err_msg = 'Failed to remove repository'
        return self.get_cmd('remove_repo', pre_msg, err_msg, arg, options, head_options)

    def purge(self, arg: str, options: list[Option] = None, head_options: list[Option] = None):
        pre_msg = f'Trying to purge the program: {arg}'
        err_msg = f'The {arg} failed to purge!'
        return self.get_cmd('purge', pre_msg, err_msg, arg, options, head_options)

    
