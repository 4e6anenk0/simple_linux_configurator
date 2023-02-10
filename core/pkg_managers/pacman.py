
from core import log
from core.pkg_managers.managers import UniversalManager
from core.utils.cli_elements import Operation, Option
from core.utils.enums import PKGManagers as pkgm

logger = log.get_logger(__name__)


class _PacmanOptions:
    
    @classmethod
    def user(cls, parent_operation: str) -> Option:
        return Option('--user', parent_operation, alias='-u')

class Pacman(UniversalManager):
    class Database(Operation):
        operation = '--database'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--database'
            operation_alias = '-D'
            
            super().__init__(parent_label, operation, operation_alias)

        @classmethod
        def user(cls) -> Option:
            '''Install the application or runtime in a per-user installation'''
            return _PacmanOptions.user(cls.operation)
