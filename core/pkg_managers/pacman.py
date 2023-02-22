
from pathlib import Path
from core import log
from core.pkg_managers.managers import UniversalManager
from core.utils.cli_elements import Operation, Option
from core.utils.enums import PKGManagers as pkgm

logger = log.get_logger(__name__)


class _PacmanOptions:
    
    @classmethod
    def dbpath(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--dbpath', parent_operation, path, '-b')
        else:
            logger.error(
                f'A non-absolute path was specified for the [pacman --dbpath] class method')

    @classmethod
    def check(cls, parent_operation: str) -> Option:
        return Option('--check', parent_operation, alias='-k')
    
    @classmethod
    def quiet(cls, parent_operation: str) -> Option:
        return Option('--quiet', parent_operation, alias='-q')

    @classmethod
    def root(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--root', parent_operation, path, '-r')
        else:
            logger.error(
                f'A non-absolute path was specified for the [pacman --root] class method')
    
    @classmethod
    def verbose(cls, parent_operation: str) -> Option:
        return Option('--verbose', parent_operation, alias='-v')

    @classmethod
    def arch(cls, parent_operation: str, arch: str) -> Option:
        return Option('--arch', parent_operation, arch)

    @classmethod
    def asdeps(cls, parent_operation: str) -> Option:
        return Option('--asdeps', parent_operation)
    
    @classmethod
    def asexplicit(cls, parent_operation: str) -> Option:
        return Option('--asexplicit', parent_operation)
    
    @classmethod
    def cachedir(cls, parent_operation: str, dir_path: Path) -> Option:
        if Path.is_dir(dir_path):
            return Option('--cachedir', parent_operation, dir_path)
        else:
            logger.error(
                f'The specified path is not a directory for the [pacman --cachedir] class method')
    
    @classmethod
    def color(cls, parent_operation: str, when: str) -> Option:
        return Option('--color', parent_operation, when)

    @classmethod
    def config(cls, parent_operation: str, file_dir: str) -> Option:
        if Path.is_file(file_dir):
            return Option('--config', parent_operation, file_dir)
        else:
            logger.error(
                f'Path does not point to a file in [pacman --config] class method')

    @classmethod
    def confirm(cls, parent_operation: str) -> Option:
        return Option('--confirm', parent_operation)

    @classmethod
    def debug(cls, parent_operation: str) -> Option:
        return Option('--debug', parent_operation)
    
    @classmethod
    def disable_download_timeout(cls, parent_operation: str) -> Option:
        return Option('--disable-download-timeout', parent_operation)

    @classmethod
    def gpgdir(cls, parent_operation: str, dir_path: Path) -> Option:
        if Path.is_dir(dir_path):
            return Option('--gpgdir', parent_operation, dir_path)
        else:
            logger.error(
                f'The specified path is not a directory for the [pacman --gpgdir] class method')

    @classmethod
    def hookdir(cls, parent_operation: str, dir_path: Path) -> Option:
        if Path.is_dir(dir_path):
            return Option('--hookdir', parent_operation, dir_path)
        else:
            logger.error(
                f'The specified path is not a directory for the [pacman --hookdir] class method')
    
    @classmethod
    def logfile(cls, parent_operation: str, file_path: str) -> Option:
        if Path.is_file(file_path):
            return Option('--logfile', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [pacman --logfile] class method')
    
    @classmethod
    def sysroot(cls, parent_operation: str) -> Option:
        return Option('--sysroot', parent_operation)

    @classmethod
    def changelog(cls, parent_operation: str) -> Option:
        return Option('--changelog', parent_operation, alias='-c')

    @classmethod
    def deps(cls, parent_operation: str) -> Option:
        return Option('--deps', parent_operation, alias='-d')

    @classmethod
    def explicit(cls, parent_operation: str) -> Option:
        return Option('--explicit', parent_operation, alias='-e')

    @classmethod
    def groups(cls, parent_operation: str) -> Option:
        return Option('--groups', parent_operation, alias='-g')

    @classmethod
    def info(cls, parent_operation: str) -> Option:
        return Option('--info', parent_operation, alias='-i')

    @classmethod
    def list_(cls, parent_operation: str) -> Option:
        return Option('--list', parent_operation, alias='-l')

    @classmethod
    def foreign(cls, parent_operation: str) -> Option:
        return Option('--foreign', parent_operation, alias='-m')

    @classmethod
    def native(cls, parent_operation: str) -> Option:
        return Option('--native', parent_operation, alias='-n')

    @classmethod
    def owns(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--owns', parent_operation, file_path, alias='o')
        else:
            logger.error(
                f'Path does not point to a file in [pacman --owns] class method')

    @classmethod
    def file_(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--file', parent_operation, file_path, alias='p')
        else:
            logger.error(
                f'Path does not point to a file in [pacman --file] class method')

    @classmethod
    def search(cls, parent_operation: str, query: str) -> Option:
        return Option('--search', parent_operation, query, alias='-s')

    @classmethod
    def unrequired(cls, parent_operation: str) -> Option:
        return Option('--unrequired', parent_operation, alias='-t')

    @classmethod
    def upgrades(cls, parent_operation: str) -> Option:
        return Option('--upgrades', parent_operation, alias='-u')

    @classmethod
    def cascade(cls, parent_operation: str) -> Option:
        return Option('--cascade', parent_operation, alias='-c')

    @classmethod
    def nodeps(cls, parent_operation: str) -> Option:
        return Option('--nodeps', parent_operation, alias='-d')
    
    @classmethod
    def nosave(cls, parent_operation: str) -> Option:
        return Option('--nosave', parent_operation, alias='-n')

    @classmethod
    def print(cls, parent_operation: str) -> Option:
        return Option('--print', parent_operation, alias='-p')
    
    @classmethod
    def recursive(cls, parent_operation: str) -> Option:
        return Option('--recursive', parent_operation, alias='-s')

    @classmethod
    def unneeded(cls, parent_operation: str) -> Option:
        return Option('--unneeded', parent_operation, alias='-u')

    @classmethod
    def assume_installed(cls, parent_operation: str, package: str, version: str) -> Option:
        str_opt = f"{package}={version}"
        return Option('--assume-installed', parent_operation, str_opt)

    @classmethod
    def dbonly(cls, parent_operation: str) -> Option:
        return Option('--dbonly', parent_operation)

    @classmethod
    def print_format(cls, parent_operation: str, format_: str) -> Option:
        return Option('--print-format', parent_operation, format_)

    @classmethod
    def noprogressbar(cls, parent_operation: str) -> Option:
        return Option('--noprogressbar', parent_operation)

    @classmethod
    def noscriptlet(cls, parent_operation: str) -> Option:
        return Option('--noscriptlet', parent_operation)

    @classmethod
    def clean(cls, parent_operation: str) -> Option:
        return Option('--clean', parent_operation, alias='-c')

    @classmethod
    def sysupgrade(cls, parent_operation: str) -> Option:
        return Option('--sysupgrade', parent_operation, alias='-u')

    @classmethod
    def downloadonly(cls, parent_operation: str) -> Option:
        return Option('--downloadonly', parent_operation, alias='-w')
    
    @classmethod
    def refresh(cls, parent_operation: str) -> Option:
        return Option('--refresh', parent_operation, alias='-y')

    @classmethod
    def ignore(cls, parent_operation: str, package: str) -> Option:
        return Option('--ignore', parent_operation, package)

    @classmethod
    def ignoregroup(cls, parent_operation: str, group: str) -> Option:
        return Option('--ignoregroup', parent_operation, group)

    @classmethod
    def overwrite(cls, parent_operation: str, glob: str) -> Option:
        return Option('--overwrite', parent_operation, glob)

    @classmethod
    def list_storage(cls, parent_operation: str, storage: str) -> Option:
        return Option('--list', parent_operation, storage, alias='-l')

    @classmethod
    def needed(cls, parent_operation: str) -> Option:
        return Option('--needed', parent_operation)

    @classmethod
    def regex(cls, parent_operation: str) -> Option:
        return Option('--regex', parent_operation, alias='-x')

    @classmethod
    def machinereadable(cls, parent_operation: str) -> Option:
        return Option('--machinereadable', parent_operation)


class Pacman(UniversalManager):
    class Database(Operation):
        operation = '--database'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--database'
            operation_alias = '-D'
            default_head_options = '--noconfirm'
            
            super().__init__(parent_label, 
                            operation, 
                            operation_alias,
                            default_head_options=default_head_options)


        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def check(cls) -> Option:
            return _PacmanOptions.check(cls.operation)

        @classmethod
        def quiet(cls) -> Option:
            return _PacmanOptions.quiet(cls.operation)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def arch(cls) -> Option:
            return _PacmanOptions.arch(cls.operation)

        @classmethod
        def asdeps(cls) -> Option:
            return _PacmanOptions.asdeps(cls.operation)
            
        @classmethod
        def asexplicit(cls) -> Option:
            return _PacmanOptions.asexplicit(cls.operation)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def confirm(cls) -> Option:
            return _PacmanOptions.confirm(cls.operation)
        
        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def logfile(cls, file_dir: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_dir)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Query(Operation):
        operation = '--query'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--query'
            operation_alias = '-Q'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def changelog(cls) -> Option:
            return _PacmanOptions.changelog(cls.operation)

        @classmethod
        def deps(cls) -> Option:
            return _PacmanOptions.deps(cls.operation)

        @classmethod
        def explicit(cls) -> Option:
            return _PacmanOptions.explicit(cls.operation)

        @classmethod
        def groups(cls) -> Option:
            return _PacmanOptions.groups(cls.operation)

        @classmethod
        def info(cls) -> Option:
            return _PacmanOptions.info(cls.operation)

        @classmethod
        def check(cls) -> Option:
            return _PacmanOptions.check(cls.operation)

        @classmethod
        def list_(cls) -> Option:
            return _PacmanOptions.list_(cls.operation)

        @classmethod
        def foreign(cls) -> Option:
            return _PacmanOptions.foreign(cls.operation)

        @classmethod
        def native(cls) -> Option:
            return _PacmanOptions.native(cls.operation)

        @classmethod
        def owns(cls, file_path: Path) -> Option:
            return _PacmanOptions.owns(cls.operation, file_path)

        @classmethod
        def file_(cls, file_path: Path) -> Option:
            return _PacmanOptions.file_(cls.operation, file_path)

        @classmethod
        def quiet(cls) -> Option:
            return _PacmanOptions.quiet(cls.operation)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def search(cls, query: str) -> Option:
            return _PacmanOptions.search(cls.operation, query)

        @classmethod
        def unrequired(cls) -> Option:
            return _PacmanOptions.unrequired(cls.operation)

        @classmethod
        def upgrades(cls) -> Option:
            return _PacmanOptions.upgrades(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)
        
        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, when: str) -> Option:
            return _PacmanOptions.config(cls.operation, when)

        @classmethod
        def debug(cls, when: str) -> Option:
            return _PacmanOptions.debug(cls.operation, when)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)
        
        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def file_path(cls, file_path: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_path)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Remove(Operation):
        operation = '--remove'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--remove'
            operation_alias = '-R'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def cascade(cls) -> Option:
            return _PacmanOptions.cascade(cls.operation)

        @classmethod
        def nodeps(cls) -> Option:
            return _PacmanOptions.nodeps(cls.operation)

        @classmethod
        def nosave(cls) -> Option:
            return _PacmanOptions.nosave(cls.operation)

        @classmethod
        def print(cls) -> Option:
            return _PacmanOptions.print(cls.operation)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def recursive(cls) -> Option:
            return _PacmanOptions.recursive(cls.operation)

        @classmethod
        def unneeded(cls) -> Option:
            return _PacmanOptions.unneeded(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def assume_installed(cls, package: str, version: str) -> Option:
            return _PacmanOptions.assume_installed(cls.operation, package, version)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, file_dir: Path) -> Option:
            return _PacmanOptions.config(cls.operation, file_dir)

        @classmethod
        def dbonly(cls) -> Option:
            return _PacmanOptions.dbonly(cls.operation)

        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, file_path: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_path)

        @classmethod
        def noprogressbar(cls) -> Option:
            return _PacmanOptions.noprogressbar(cls.operation)
        
        @classmethod
        def noscriptlet(cls) -> Option:
            return _PacmanOptions.noscriptlet(cls.operation)

        @classmethod
        def print_format(cls, format_: str) -> Option:
            return _PacmanOptions.print_format(cls.operation, format_)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Sync(Operation):
        operation = '--sync'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--sync'
            operation_alias = '-S'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def clean(cls) -> Option:
            return _PacmanOptions.clean(cls.operation)

        @classmethod
        def nodeps(cls) -> Option:
            return _PacmanOptions.nodeps(cls.operation)
        
        @classmethod
        def groups(cls) -> Option:
            return _PacmanOptions.groups(cls.operation)

        @classmethod
        def info(cls) -> Option:
            return _PacmanOptions.info(cls.operation)
        
        @classmethod
        def list_(cls, storage: str) -> Option:
            return _PacmanOptions.list_storage(cls.operation, storage)

        @classmethod
        def print(cls) -> Option:
            return _PacmanOptions.print(cls.operation)
        
        @classmethod
        def quiet(cls) -> Option:
            return _PacmanOptions.quiet(cls.operation)
        
        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def search(cls, query: str) -> Option:
            return _PacmanOptions.search(cls.operation, query)
        
        @classmethod
        def sysupgrade(cls) -> Option:
            return _PacmanOptions.sysupgrade(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def downloadonly(cls) -> Option:
            return _PacmanOptions.downloadonly(cls.operation)

        @classmethod
        def refresh(cls) -> Option:
            return _PacmanOptions.refresh(cls.operation)

        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def asdeps(cls) -> Option:
            return _PacmanOptions.asdeps(cls.operation)

        @classmethod
        def asexplicit(cls) -> Option:
            return _PacmanOptions.asexplicit(cls.operation)

        @classmethod
        def assume_installed(cls, package: str, version: str) -> Option:
            return _PacmanOptions.assume_installed(cls.operation, package, version)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, file_dir: Path) -> Option:
            return _PacmanOptions.config(cls.operation, file_dir)

        @classmethod
        def confirm(cls) -> Option:
            return _PacmanOptions.confirm(cls.operation)

        @classmethod
        def dbonly(cls) -> Option:
            return _PacmanOptions.dbonly(cls.operation)

        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def ignore(cls, package: str) -> Option:
            return _PacmanOptions.ignore(cls.operation, package)

        @classmethod
        def ignoregroup(cls, group: str) -> Option:
            return _PacmanOptions.ignoregroup(cls.operation, group)

        @classmethod
        def logfile(cls, file_path: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_path)

        @classmethod
        def needed(cls) -> Option:
            return _PacmanOptions.needed(cls.operation)

        @classmethod
        def noprogressbar(cls) -> Option:
            return _PacmanOptions.noprogressbar(cls.operation)

        @classmethod
        def noscriptlet(cls) -> Option:
            return _PacmanOptions.noscriptlet(cls.operation)

        @classmethod
        def overwrite(cls, glob: str) -> Option:
            return _PacmanOptions.overwrite(cls.operation, glob)

        @classmethod
        def print_format(cls, format_: str) -> Option:
            return _PacmanOptions.print_format(cls.operation, format_)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Deptest(Operation):
        operation = '--deptest'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--deptest'
            operation_alias = '-T'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, file_dir: Path) -> Option:
            return _PacmanOptions.config(cls.operation, file_dir)

        @classmethod
        def confirm(cls) -> Option:
            return _PacmanOptions.confirm(cls.operation)

        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def logfile(cls, file_dir: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_dir)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Upgrade(Operation):
        operation = '--upgrade'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--upgrade'
            operation_alias = '-U'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)

        @classmethod
        def nodeps(cls) -> Option:
            return _PacmanOptions.nodeps(cls.operation)

        @classmethod
        def print(cls) -> Option:
            return _PacmanOptions.print(cls.operation)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def downloadonly(cls) -> Option:
            return _PacmanOptions.downloadonly(cls.operation)
        
        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def asdeps(cls) -> Option:
            return _PacmanOptions.asdeps(cls.operation)

        @classmethod
        def asexplicit(cls) -> Option:
            return _PacmanOptions.asexplicit(cls.operation)

        @classmethod
        def assume_installed(cls, package: str, version: str) -> Option:
            return _PacmanOptions.assume_installed(cls.operation, package, version)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, file_dir: Path) -> Option:
            return _PacmanOptions.config(cls.operation, file_dir)

        @classmethod
        def confirm(cls) -> Option:
            return _PacmanOptions.confirm(cls.operation)

        @classmethod
        def dbonly(cls) -> Option:
            return _PacmanOptions.dbonly(cls.operation)

        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def ignore(cls, package: str) -> Option:
            return _PacmanOptions.ignore(cls.operation, package)

        @classmethod
        def ignoregroup(cls, group: str) -> Option:
            return _PacmanOptions.ignoregroup(cls.operation, group)

        @classmethod
        def logfile(cls, file_path: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_path)

        @classmethod
        def needed(cls) -> Option:
            return _PacmanOptions.needed(cls.operation)

        @classmethod
        def noprogressbar(cls) -> Option:
            return _PacmanOptions.noprogressbar(cls.operation)

        @classmethod
        def noscriptlet(cls) -> Option:
            return _PacmanOptions.noscriptlet(cls.operation)

        @classmethod
        def overwrite(cls, glob: str) -> Option:
            return _PacmanOptions.overwrite(cls.operation, glob)

        @classmethod
        def print_format(cls, format_: str) -> Option:
            return _PacmanOptions.print_format(cls.operation, format_)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    class Files(Operation):
        operation = '--files'

        def __init__(self) -> None:
            parent_label = pkgm.pacman
            operation = '--files'
            operation_alias = '-F'
            default_head_options = '--noconfirm'

            super().__init__(parent_label,
                             operation,
                             operation_alias,
                             default_head_options=default_head_options)

        @classmethod
        def dbpath(cls, path: Path) -> Option:
            return _PacmanOptions.dbpath(cls.operation, path)
        
        @classmethod
        def list_(cls) -> Option:
            return _PacmanOptions.list_(cls.operation)

        @classmethod
        def quiet(cls) -> Option:
            return _PacmanOptions.quiet(cls.operation)

        @classmethod
        def root(cls, path: Path) -> Option:
            return _PacmanOptions.root(cls.operation, path)

        @classmethod
        def verbose(cls) -> Option:
            return _PacmanOptions.verbose(cls.operation)

        @classmethod
        def regex(cls) -> Option:
            return _PacmanOptions.regex(cls.operation)

        @classmethod
        def refresh(cls) -> Option:
            return _PacmanOptions.refresh(cls.operation)

        @classmethod
        def arch(cls, arch: str) -> Option:
            return _PacmanOptions.arch(cls.operation, arch)

        @classmethod
        def cachedir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.cachedir(cls.operation, dir_path)

        @classmethod
        def color(cls, when: str) -> Option:
            return _PacmanOptions.color(cls.operation, when)

        @classmethod
        def config(cls, file_dir: Path) -> Option:
            return _PacmanOptions.config(cls.operation, file_dir)

        @classmethod
        def confirm(cls) -> Option:
            return _PacmanOptions.confirm(cls.operation)

        @classmethod
        def debug(cls) -> Option:
            return _PacmanOptions.debug(cls.operation)

        @classmethod
        def disable_download_timeout(cls) -> Option:
            return _PacmanOptions.disable_download_timeout(cls.operation)

        @classmethod
        def gpgdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.gpgdir(cls.operation, dir_path)

        @classmethod
        def hookdir(cls, dir_path: Path) -> Option:
            return _PacmanOptions.hookdir(cls.operation, dir_path)

        @classmethod
        def logfile(cls, file_path: Path) -> Option:
            return _PacmanOptions.logfile(cls.operation, file_path)

        @classmethod
        def machinereadable(cls) -> Option:
            return _PacmanOptions.machinereadable(cls.operation)

        @classmethod
        def sysroot(cls) -> Option:
            return _PacmanOptions.sysroot(cls.operation)

    @classmethod
    def install(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.sync(arg, options, head_options)
        return cmd

    @classmethod
    def remove(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Remove().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def update(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        if options:
            all_opt = [Pacman.Sync.refresh(), Pacman.Sync.sysupgrade()].extend(options)
        else:
            all_opt = [Pacman.Sync.refresh(), Pacman.Sync.sysupgrade()]
        cmd = cls.Sync().get_cmd(arg, all_opt, head_options)
        return cmd

    @classmethod
    def database(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Database().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def query(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Query().get_cmd(arg, options, head_options)
        return cmd
    
    @classmethod
    def upgrade(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Upgrade().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def files(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Files().get_cmd(arg, options, head_options)
        return cmd
    
    @classmethod
    def sync(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Sync().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def deptest(cls, arg: str = None, options: list[Option] = None, head_options: list[Option] = None):
        cmd = cls.Deptest().get_cmd(arg, options, head_options)
        return cmd
