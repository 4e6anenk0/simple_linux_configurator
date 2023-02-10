from core.settings import settingsObj
from core import log

logger = log.get_logger(__name__)

class Option:
    def __init__(self, key: str, parent_operation: str, value: object = None, alias: str = None) -> None:
        self.key = key
        self.value = value
        self.alias = alias
        self.parent_operation = parent_operation
        self.equal = ' '
        self.compact = False
        self.__set_equal_from_settings()
        self.__set_compact_from_settings()

    def __set_equal_from_settings(self):
        settings_par = settingsObj.project.get('equal')
        if settings_par == 'True':
            self.equal = '='
        elif settings_par == 'False':
            
            self.equal = ' '
        else:
            logger.error(
                'An invalid value for the argument was specified in the settings: project -> equal')

    def __set_compact_from_settings(self):
        if settingsObj.project.get('use_compact_commands') == 'True':
            self.compact = True
        elif settingsObj.project.get('use_compact_commands') == 'False':
            self.compact = False
        else:
            logger.error(
                'An invalid value for the argument was specified in the settings: project -> use_compact_commands')

    def value_to_str(self) -> str:
        return str(self.value)

    def get(self):
        if self.compact == True and self.alias != None:
            if self.value:
                return f'{self.alias}{self.equal}{self.value_to_str()}'
            else:
                return f'{self.alias}'
        else:
            if self.value:
                return f'{self.key}{self.equal}{self.value_to_str()}'
            else:
                return f'{self.key}'
        

    def __str__(self) -> str:
        if self.value:
            return f'{self.key} {self.value_to_str()}'
        else:
            return f'{self.key}'


class Operation:
    def __init__(self,
                 parent_label: str,
                 operation: str,
                 operation_alias: str = None,
                 default_options: str = '') -> None:
        self.parent_label = parent_label
        self.operation = operation
        self.alias = operation_alias
        self.default_options = default_options

    def _represent_options(self, options: list[Option]) -> str:
        if options:
            represent_opt = []
            for opt in options:
                represent_opt.append(opt.get())
        else:
            return []
        return represent_opt

    def _is_target_option(self, option: Option):
        if option.parent_operation == self.operation:
            return True
        else:
            return False

    def _validate_options(self, options: list[Option]):
        if options:
            for option in options:
                if self._is_target_option(option) == False:
                    logger.error(
                        f"Probably the wrong options were passed. Invalid option: [{option.get()}], target operation: [{self.operation}]. For non-target options, it is impossible to get the correct command")
                    raise Exception(
                        "There is a non-valid item in the options list!")
        else:
            return

    def get_cmd(self, argument: str = None, options: list[Option] = None, head_options: list[Option] = None) -> str:
        
        self._validate_options(options)
    
        represent_options = self._represent_options(options)
        represent_head_options = self._represent_options(head_options)
        
        build_cmd = [self.parent_label]
        build_cmd.extend(represent_head_options)
        build_cmd.append(self.operation)
        build_cmd.append(self.default_options)
        build_cmd.extend(represent_options)
        
        if argument:
            build_cmd.append(str(argument))

        cmd = " ".join(build_cmd)
            
        return cmd
