from pathlib import Path
from core.pkg_managers.managers import UniversalManager
from core.utils.cli_elements import *
from core import log
from core.utils.enums import PKGManagers as pkgm

logger = log.get_logger(__name__)

class _FlatpakOptions:

    @classmethod
    def user(cls, parent_operation: str) -> Option:
        return Option('--user', parent_operation, alias='-u')

    @classmethod
    def system(cls, parent_operation: str) -> Option:
        return Option('--system', parent_operation)

    @classmethod
    def installation(cls, parent_operation: str, name: str) -> Option:
        return Option('--installation', parent_operation, name)

    @classmethod
    def arch(cls, parent_operation: str, apx: str) -> Option:
        return Option('--arch', parent_operation, apx)

    @classmethod
    def no_pull(cls, parent_operation: str) -> Option:
        return Option('--no-pull', parent_operation)

    @classmethod
    def no_deploy(cls, parent_operation: str) -> Option:
        return Option('--no-deploy', parent_operation)

    @classmethod
    def no_related(cls, parent_operation: str) -> Option:
        return Option('--no-related', parent_operation)

    @classmethod
    def no_deps(cls, parent_operation: str) -> Option:
        return Option('--no-deps', parent_operation)

    @classmethod
    def no_auto_pin(cls, parent_operation: str) -> Option:
        return Option('--no-auto-pin', parent_operation)

    @classmethod
    def no_static_deltas(cls, parent_operation: str) -> Option:
        return Option('--no-static-deltas', parent_operation)

    @classmethod
    def runtime(cls, parent_operation: str) -> Option:
        return Option('--runtime', parent_operation)

    @classmethod
    def app(cls, parent_operation: str) -> Option:
        return Option('--app', parent_operation)

    @classmethod
    def include_sdk(cls, parent_operation: str) -> Option:
        return Option('--include-sdk', parent_operation)

    @classmethod
    def include_debug(cls, parent_operation: str) -> Option:
        return Option('--include-debug', parent_operation)

    @classmethod
    def bundle(cls, parent_operation: str) -> Option:
        return Option('--bundle', parent_operation)

    @classmethod
    def from_(cls, parent_operation: str) -> Option:
        return Option('--from', parent_operation)

    @classmethod
    def gpg_file(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--gpg-file', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [flatpak --gpg-file] class method')

    @classmethod
    def subpath(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--subpath', parent_operation, path)
        else:
            logger.error(
                f'A non-absolute path was specified for the [flatpak --subpath] class method')

    @classmethod
    def reinstall(cls, parent_operation: str) -> Option:
        return Option('--reinstall', parent_operation)

    @classmethod
    def or_update(cls, parent_operation: str) -> Option:
        return Option('--or-update', parent_operation)

    @classmethod
    def sideload_repo(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--sideload-repo', parent_operation, path)
        else:
            logger.error(
                f'A non-absolute path was specified for the [flatpak --sideload-repo] class method')

    @classmethod
    def verbose(cls, parent_operation: str) -> Option:
        return Option('--verbose', parent_operation, alias='-v')

    @classmethod
    def ostree_verbose(cls, parent_operation: str) -> Option:
        return Option('--ostree-verbose', parent_operation)

    @classmethod
    def keep_ref(cls, parent_operation: str) -> Option:
        return Option('--keep-ref', parent_operation)

    @classmethod
    def force_remove(cls, parent_operation: str) -> Option:
        return Option('--force-remove', parent_operation)

    @classmethod
    def unused(cls, parent_operation: str) -> Option:
        return Option('--unused', parent_operation)

    @classmethod
    def delete_data(cls, parent_operation: str) -> Option:
        return Option('--delete-data', parent_operation)
    
    @classmethod
    def commit(cls, parent_operation: str, commit: str) -> Option:
        return Option('--commit', parent_operation, commit)

    @classmethod
    def appstream(cls, parent_operation: str) -> Option:
        return Option('--appstream', parent_operation)

    @classmethod
    def remove(cls, parent_operation: str) -> Option:
        return Option('--remove', parent_operation)
    
    @classmethod
    def show_details(cls, parent_operation: str) -> Option:
        return Option('--show-details', parent_operation, alias='-d')
    
    @classmethod
    def all(cls, parent_operation: str) -> Option:
        return Option('--all', parent_operation, alias='-a')

    @classmethod
    def app_runtime(cls, parent_operation: str, runtime: str) -> Option:
        return Option('--app-runtime', parent_operation, runtime)
    
    @classmethod
    def columns(cls, parent_operation: str, fields: list[str]) -> Option:
        fields_string = ','.join(fields)
        return Option('--columns', parent_operation, fields_string)
    
    @classmethod
    def show_ref(cls, parent_operation: str) -> Option:
        return Option('--show-ref', parent_operation, alias='-r')
    
    @classmethod
    def show_commit(cls, parent_operation: str) -> Option:
        return Option('--show-commit', parent_operation, alias='-c')
    
    @classmethod
    def show_origin(cls, parent_operation: str) -> Option:
        return Option('--show-origin', parent_operation, alias='-o')
    
    @classmethod
    def show_size(cls, parent_operation: str) -> Option:
        return Option('--show-size', parent_operation, alias='-s')
    
    @classmethod
    def show_parent(cls, parent_operation: str) -> Option:
        return Option('--show-parent', parent_operation, alias='-p')
    
    @classmethod
    def show_metadata(cls, parent_operation: str) -> Option:
        return Option('--show-metadata', parent_operation, alias='-m')
    
    @classmethod
    def show_runtime(cls, parent_operation: str) -> Option:
        return Option('--show-runtime', parent_operation)
    
    @classmethod
    def show_sdk(cls, parent_operation: str) -> Option:
        return Option('--show-sdk', parent_operation)

    @classmethod
    def show_permissions(cls, parent_operation: str) -> Option:
        return Option('--show-permissions', parent_operation, alias='-M')
    
    @classmethod
    def file_access(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--file-access', parent_operation, path)
        else:
            logger.error(
                f'A non-absolute path was specified for the [flatpak --file-access] class method')
    
    @classmethod
    def show_extensions(cls, parent_operation: str) -> Option:
        return Option('--show-extensions', parent_operation, alias='-e')

    @classmethod
    def show_location(cls, parent_operation: str) -> Option:
        return Option('--show-location', parent_operation, alias='-l')
    
    @classmethod
    def since(cls, parent_operation: str, time: str) -> Option:
        return Option('--since', parent_operation, time)
    
    @classmethod
    def until(cls, parent_operation: str, time: str) -> Option:
        return Option('--until', parent_operation, time)

    @classmethod
    def reverse(cls, parent_operation: str) -> Option:
        return Option('--reverse', parent_operation)

    @classmethod
    def list_(cls, parent_operation: str) -> Option:
        return Option('--list', parent_operation)

    @classmethod
    def get(cls, parent_operation: str) -> Option:
        return Option('--get', parent_operation)

    @classmethod
    def set_(cls, parent_operation: str) -> Option:
        return Option('--set', parent_operation)
    
    @classmethod
    def unset(cls, parent_operation: str) -> Option:
        return Option('--unset', parent_operation)

    @classmethod
    def dry_run(cls, parent_operation: str) -> Option:
        return Option('--dry-run', parent_operation)
    
    @classmethod
    def reinstall_all(cls, parent_operation: str) -> Option:
        return Option('--reinstall-all', parent_operation)

    @classmethod
    def destination_repo(cls, parent_operation: str, recognition: str) -> Option:
        return Option('--destination-repo', parent_operation, recognition)
    
    @classmethod
    def allow_partial(cls, parent_operation: str) -> Option:
        return Option('--allow-partial', parent_operation)
    
    @classmethod
    def command(cls, parent_operation: str, command: str) -> Option:
        return Option('--command', parent_operation, command)

    @classmethod
    def cwd(cls, parent_operation: str, dir: Path) -> Option:
        if Path.is_dir(dir):
            return Option('--cwd', parent_operation, dir)
        else:
            logger.error(
                f'The specified path is not a directory for the [flatpak --cwd] class method')
    
    @classmethod
    def branch(cls, parent_operation: str, branch: str) -> Option:
        return Option('--branch', parent_operation, branch)

    @classmethod
    def devel(cls, parent_operation: str) -> Option:
        return Option('--devel', parent_operation, alias='-d')

    @classmethod
    def runtime_version(cls, parent_operation: str, version: str) -> Option:
        return Option('--runtime-version', parent_operation, version)
    
    @classmethod
    def log_session_bus(cls, parent_operation: str) -> Option:
        return Option('--log-session-bus', parent_operation)

    @classmethod
    def log_system_bus(cls, parent_operation: str) -> Option:
        return Option('--log-system-bus', parent_operation)

    @classmethod
    def log_a11y_bus(cls, parent_operation: str) -> Option:
        return Option('--log-a11y-bus', parent_operation)
    
    @classmethod
    def no_a11y_bus(cls, parent_operation: str) -> Option:
        return Option('--no-a11y-bus', parent_operation)

    @classmethod
    def a11y_bus(cls, parent_operation: str) -> Option:
        return Option('--a11y-bus', parent_operation)
    
    @classmethod
    def no_session_bus(cls, parent_operation: str) -> Option:
        return Option('--no-session-bus', parent_operation)

    @classmethod
    def session_bus(cls, parent_operation: str) -> Option:
        return Option('--session-bus', parent_operation)
    
    @classmethod
    def no_documents_portal(cls, parent_operation: str) -> Option:
        return Option('--no-documents-portal', parent_operation)
    
    @classmethod
    def file_forwarding(cls, parent_operation: str) -> Option:
        return Option('--file-forwarding', parent_operation)
    
    @classmethod
    def runtime_commit(cls, parent_operation: str) -> Option:
        return Option('--runtime-commit', parent_operation)
    
    @classmethod
    def sandbox(cls, parent_operation: str) -> Option:
        return Option('--sandbox', parent_operation)

    @classmethod
    def die_with_parent(cls, parent_operation: str) -> Option:
        return Option('--die-with-parent', parent_operation, alias='-p')

    @classmethod
    def parent_pid(cls, parent_operation: str, pid: str) -> Option:
        return Option('--parent-pid', parent_operation, pid)

    @classmethod
    def parent_expose_pids(cls, parent_operation: str) -> Option:
        return Option('--parent-expose-pids', parent_operation)

    @classmethod
    def parent_share_pids(cls, parent_operation: str) -> Option:
        return Option('--parent-share-pids', parent_operation)

    @classmethod
    def instance_id_fd(cls, parent_operation: str) -> Option:
        return Option('--instance-id-fd', parent_operation)

    @classmethod
    def app_path(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--app-path', parent_operation, path)
        else:
            logger.error(
                f'A non-absolute path was specified for the [flatpak --app-path] class method')
            
    @classmethod
    def usr_path(cls, parent_operation: str, path: Path) -> Option:
        if Path.is_absolute(path):
            return Option('--usr-path', parent_operation, path)
        else:
            logger.error(
                f'A non-absolute path was specified for the [flatpak --usr-path] class method')

    @classmethod
    def share(cls, parent_operation: str, shared_resource: str) -> Option:
        return Option('--share', parent_operation, shared_resource)

    @classmethod
    def unshare(cls, parent_operation: str, shared_resource: str) -> Option:
        return Option('--unshare', parent_operation, shared_resource)

    @classmethod
    def socket(cls, parent_operation: str, socket: str) -> Option:
        return Option('--socket', parent_operation, socket)
    
    @classmethod
    def nosocket(cls, parent_operation: str, socket: str) -> Option:
        return Option('--nosocket', parent_operation, socket)

    @classmethod
    def device(cls, parent_operation: str, device: str) -> Option:
        return Option('--device', parent_operation, device)

    @classmethod
    def nodevice(cls, parent_operation: str, device: str) -> Option:
        return Option('--nodevice', parent_operation, device)
    
    @classmethod
    def allow(cls, parent_operation: str, possibility: str) -> Option:
        return Option('--allow', parent_operation, possibility)

    @classmethod
    def disallow(cls, parent_operation: str, possibility: str) -> Option:
        return Option('--disallow', parent_operation, possibility)

    @classmethod
    def filesystem(cls, parent_operation: str, file_system: str) -> Option:
        return Option('--filesystem', parent_operation, file_system)

    @classmethod
    def nofilesystem(cls, parent_operation: str, file_system: str) -> Option:
        return Option('--nofilesystem', parent_operation, file_system)
    
    @classmethod
    def env(cls, parent_operation: str, variable: str, value: str) -> Option:
        env_str = f"{variable}={value}"
        return Option('--env', parent_operation, env_str)

    @classmethod
    def env_fd(cls, parent_operation: str, file_descriptor: str) -> Option:
        return Option('--env-fd', parent_operation, file_descriptor)

    @classmethod
    def unset_env(cls, parent_operation: str, variable: str) -> Option:
        return Option('--unset-env', parent_operation, variable)

    @classmethod
    def own_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--own-name', parent_operation, dbas_name)
    
    @classmethod
    def talk_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--talk-name', parent_operation, dbas_name)
    
    @classmethod
    def no_talk_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--no-talk-name', parent_operation, dbas_name)

    @classmethod
    def system_own_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--system-own-name', parent_operation, dbas_name)

    @classmethod
    def system_talk_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--system-talk-name', parent_operation, dbas_name)

    @classmethod
    def system_no_talk_name(cls, parent_operation: str, dbas_name: str) -> Option:
        return Option('--system-no-talk-name', parent_operation, dbas_name)

    @classmethod
    def add_policy(cls, parent_operation: str, subsystem: str, key: str, value: str) -> Option:
        str_par = f"{subsystem}.{key}={value}"
        return Option('--add-policy', parent_operation, str_par)

    @classmethod
    def remove_policy(cls, parent_operation: str, subsystem: str, key: str, value: str) -> Option:
        str_par = f"{subsystem}.{key}={value}"
        return Option('--remove-policy', parent_operation, str_par)

    @classmethod
    def persist(cls, parent_operation: str, file_name: str) -> Option:
        return Option('--persist', parent_operation, file_name)

    @classmethod
    def runtime_env(cls, parent_operation: str, env: str) -> Option:
        return Option('--runtime', parent_operation, env)

    @classmethod
    def reset(cls, parent_operation: str) -> Option:
        return Option('--reset', parent_operation)

    @classmethod
    def show(cls, parent_operation: str) -> Option:
        return Option('--show', parent_operation)

    @classmethod
    def unique(cls, parent_operation: str) -> Option:
        return Option('--unique', parent_operation, alias='-u')

    @classmethod
    def transient(cls, parent_operation: str) -> Option:
        return Option('--transient', parent_operation, alias='-t')
    
    @classmethod
    def noexist(cls, parent_operation: str) -> Option:
        return Option('--noexist', parent_operation, alias='-n')
    
    @classmethod
    def allow_read(cls, parent_operation: str) -> Option:
        return Option('--allow-read', parent_operation, alias='-r')

    @classmethod
    def allow_write(cls, parent_operation: str) -> Option:
        return Option('--allow-write', parent_operation, alias='-w')

    @classmethod
    def allow_delete(cls, parent_operation: str) -> Option:
        return Option('--allow-delete', parent_operation, alias='-d')

    @classmethod
    def allow_grant_permission(cls, parent_operation: str) -> Option:
        return Option('--allow-grant-permission', parent_operation, alias='-g')
    
    @classmethod
    def forbid_read(cls, parent_operation: str) -> Option:
        return Option('--forbid-read', parent_operation)
    
    @classmethod
    def forbid_write(cls, parent_operation: str) -> Option:
        return Option('--forbid-write', parent_operation)
    
    @classmethod
    def forbid_delete(cls, parent_operation: str) -> Option:
        return Option('--forbid-delete', parent_operation)
    
    @classmethod
    def forbid_grant_permission(cls, parent_operation: str) -> Option:
        return Option('--forbid-grant-permission', parent_operation)
    
    @classmethod
    def appid(cls, parent_operation: str, app_id: str) -> Option:
        return Option('--app', parent_operation, app_id, alias='-a')

    @classmethod
    def doc_id(cls, parent_operation: str) -> Option:
        return Option('--doc-id', parent_operation)

    @classmethod
    def data(cls, parent_operation: str, data: str) -> Option:
        return Option('--data', parent_operation, data)
    
    @classmethod
    def all(cls, parent_operation: str) -> Option:
        return Option('--all', parent_operation)
    
    @classmethod
    def show_disabled(cls, parent_operation: str) -> Option:
        return Option('--show-disabled', parent_operation)

    @classmethod
    def no_gpg_verify(cls, parent_operation: str) -> Option:
        return Option('--no-gpg-verify', parent_operation)

    @classmethod
    def no_enumerate(cls, parent_operation: str) -> Option:
        return Option('--no-enumerate', parent_operation)

    @classmethod
    def no_use_for_deps(cls, parent_operation: str) -> Option:
        return Option('--no-use-for-deps', parent_operation)

    @classmethod
    def prio(cls, parent_operation: str, prio: str) -> Option:
        return Option('--prio', parent_operation, prio)

    @classmethod
    def subset(cls, parent_operation: str, subset: str) -> Option:
        return Option('--subset', parent_operation, subset)

    @classmethod
    def title(cls, parent_operation: str, title: str) -> Option:
        return Option('--title', parent_operation, title)
    
    @classmethod
    def comment(cls, parent_operation: str, comment: str) -> Option:
        return Option('--comment', parent_operation, comment)
    
    @classmethod
    def description(cls, parent_operation: str, description: str) -> Option:
        return Option('--description', parent_operation, description)

    @classmethod
    def homepage(cls, parent_operation: str, address: str) -> Option:
        return Option('--homepage', parent_operation, address)
    
    @classmethod
    def icon(cls, parent_operation: str, address: str) -> Option:
        return Option('--icon', parent_operation, address)

    @classmethod
    def default_branch(cls, parent_operation: str, branch: str) -> Option:
        return Option('--default-branch', parent_operation, branch)
    
    @classmethod
    def collection_id(cls, parent_operation: str, build_id: str) -> Option:
        return Option('--collection-id', parent_operation, build_id)

    @classmethod
    def gpg_import(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--gpg-import', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [flatpak --gpg-import] class method')

    @classmethod
    def filter(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--filter', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [flatpak --filter] class method')

    @classmethod
    def cached(cls, parent_operation: str) -> Option:
        return Option('--cached', parent_operation)

    @classmethod
    def sideloaded(cls, parent_operation: str) -> Option:
        return Option('--sideloaded', parent_operation)
    
    @classmethod
    def disable(cls, parent_operation: str) -> Option:
        return Option('--disable', parent_operation)
    
    @classmethod
    def authenticator_name(cls, parent_operation: str, name: str) -> Option:
        return Option('--authenticator-name', parent_operation, name)

    @classmethod
    def authenticator_option(cls, parent_operation: str, key: str, value: str) -> Option:
        str_par = f"{key}={value}"
        return Option('--authenticator-option', parent_operation, str_par)

    @classmethod
    def authenticator_install(cls, parent_operation: str) -> Option:
        return Option('--authenticator-install', parent_operation)

    @classmethod
    def no_authenticator_install(cls, parent_operation: str) -> Option:
        return Option('--no-authenticator-install', parent_operation)

    @classmethod
    def no_follow_redirect(cls, parent_operation: str) -> Option:
        return Option('--no-follow_redirect', parent_operation)

    @classmethod
    def if_not_exists(cls, parent_operation: str) -> Option:
        return Option('--if-not-exists', parent_operation)

    @classmethod
    def follow_redirect(cls, parent_operation: str) -> Option:
        return Option('--follow-redirect', parent_operation)

    @classmethod
    def gpg_verify(cls, parent_operation: str) -> Option:
        return Option('--gpg-verify', parent_operation)

    @classmethod
    def enumerate(cls, parent_operation: str) -> Option:
        return Option('--enumerate', parent_operation)

    @classmethod
    def use_for_deps(cls, parent_operation: str) -> Option:
        return Option('--use-for-deps', parent_operation)

    @classmethod
    def url(cls, parent_operation: str, address: str) -> Option:
        return Option('--url', parent_operation, address)

    @classmethod
    def enable(cls, parent_operation: str) -> Option:
        return Option('--enable', parent_operation)

    @classmethod
    def update_metadata(cls, parent_operation: str) -> Option:
        return Option('--update-metadata', parent_operation)

    @classmethod
    def force(cls, parent_operation: str) -> Option:
        return Option('--force', parent_operation)

    @classmethod
    def updates(cls, parent_operation: str) -> Option:
        return Option('--updates', parent_operation)

    @classmethod
    def log(cls, parent_operation: str) -> Option:
        return Option('--log', parent_operation)

    @classmethod
    def var(cls, parent_operation: str, runtime_env: str) -> Option:
        return Option('--var', parent_operation, runtime_env, alias='-v')

    @classmethod
    def base(cls, parent_operation: str, app: str) -> Option:
        return Option('--base', parent_operation, app)

    @classmethod
    def base_version(cls, parent_operation: str, version: str) -> Option:
        return Option('--base-version', parent_operation, version)

    @classmethod
    def base_extension(cls, parent_operation: str, extension: str) -> Option:
        return Option('--base-extension', parent_operation, extension)

    @classmethod
    def extension_tag(cls, parent_operation: str, extension_tag: str) -> Option:
        return Option('--extension-tag', parent_operation, extension_tag)
    
    @classmethod
    def writable_sdk(cls, parent_operation: str) -> Option:
        return Option('--writable-sdk', parent_operation, alias='-w')

    @classmethod
    def type_(cls, parent_operation: str, type_: str) -> Option:
        return Option('--type', parent_operation, type_)

    @classmethod
    def tag(cls, parent_operation: str, tag: str) -> Option:
        return Option('--tag', parent_operation, tag)

    @classmethod
    def sdk_extension(cls, parent_operation: str, extension: str) -> Option:
        return Option('--sdk-extension', parent_operation, extension)

    @classmethod
    def extension(cls, parent_operation: str, name: str, variable: str, value: str = None) -> Option:
        if value:
            str_par = f"{name}={variable}={value}"
        else:
            str_par = f"{name}={variable}"
        return Option('--extension', parent_operation, str_par)
    
    @classmethod
    def sdk_dir(cls, parent_operation: str, dir_path: Path) -> Option:
        if Path.is_dir(dir_path):
            return Option('--sdk-dir', parent_operation, dir_path)
        else:
            logger.error(
                f'The specified path does not point to a directory in [flatpak --sdk-dir] class method')

    @classmethod
    def update(cls, parent_operation: str) -> Option:
        return Option('--update', parent_operation)

    @classmethod
    def readonly(cls, parent_operation: str) -> Option:
        return Option('--readonly', parent_operation)

    @classmethod
    def bind_mount(cls, parent_operation: str, appointment: str, source: str) -> Option:
        str_par = f"{appointment}={source}"
        return Option('--bind-mount', parent_operation, str_par)

    @classmethod
    def build_dir(cls, parent_operation: str, dir_path: Path) -> Option:
        if Path.is_dir(dir_path):
            return Option('--build-dir', parent_operation, dir_path)
        else:
            logger.error(
                f'The specified path does not point to a directory in [flatpak --build-dir] class method')

    @classmethod
    def metadata(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--metadata', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [flatpak --metadata] class method')

    @classmethod
    def with_appdir(cls, parent_operation: str) -> Option:  
        return Option('--with-appdir', parent_operation)

    @classmethod
    def require_version(cls, parent_operation: str, major: str, minor: str, micro: str) -> Option:
        str_par = f"{major}.{minor}.{micro}"
        return Option('--require-version', parent_operation, str_par)

    @classmethod
    def no_exports(cls, parent_operation: str) -> Option:
        return Option('--no-exports', parent_operation)

    @classmethod
    def extra_data(cls, parent_operation: str) -> Option:
        return Option('--extra-data', parent_operation)

    @classmethod
    def remove_extension(cls, parent_operation: str, name: str) -> Option:
        return Option('--remove-extension', parent_operation, name)
    
    @classmethod
    def extension_priority(cls, parent_operation: str, value: str) -> Option:
        return Option('--extension-priority', parent_operation, value)

    @classmethod
    def sdk(cls, parent_operation: str, sdk: str) -> Option:
        return Option('--sdk', parent_operation, sdk)

    @classmethod
    def no_inherit_permissions(cls, parent_operation: str) -> Option:
        return Option('--no-inherit-permissions', parent_operation)

    @classmethod
    def metadata_group(cls, parent_operation: str, group: str, key: str, value: str = None) -> Option:
        if value:
            str_par = f"{group}={key}={value}"
        else:
            str_par = f"{group}={key}"
        return Option('--metadata', parent_operation, str_par)

    @classmethod
    def subject(cls, parent_operation: str, subject: str) -> Option:
        return Option('--subject', parent_operation, subject, alias='-s')

    @classmethod
    def body(cls, parent_operation: str, body: str) -> Option:
        return Option('--body', parent_operation, body, alias='-b')

    @classmethod
    def update_appstream(cls, parent_operation: str) -> Option:
        return Option('--update-appstream', parent_operation)

    @classmethod
    def no_update_summary(cls, parent_operation: str) -> Option:
        return Option('--no-update-summary', parent_operation)

    @classmethod
    def files(cls, parent_operation: str, sub_dir: Path) -> Option:
        if Path.is_dir(sub_dir):
            return Option('--files', parent_operation, sub_dir)
        else:
            logger.error(
                f'The specified path does not point to a directory in [flatpak --files] class method')

    @classmethod
    def gpg_sign(cls, parent_operation: str, key_id: str) -> Option:
        return Option('--gpg-sign', parent_operation, key_id)
    
    @classmethod
    def exclude(cls, parent_operation: str, example: str) -> Option:
        return Option('--exclude', parent_operation, example)

    @classmethod
    def include(cls, parent_operation: str, example: str) -> Option:
        return Option('--include', parent_operation, example)

    @classmethod
    def gpg_homedir(cls, parent_operation: str, home_dir: Path) -> Option:
        if Path.is_dir(home_dir):
            return Option('--gpg-homedir', parent_operation, home_dir)
        else:
            logger.error(
                f'The specified path does not point to a directory in [flatpak --gpg-homedir] class method')

    @classmethod
    def end_of_life(cls, parent_operation: str, reason: str) -> Option:
        return Option('--end-of-life', parent_operation, reason)

    @classmethod
    def end_of_life_rebase(cls, parent_operation: str, id: str) -> Option:
        return Option('--end-of-life-rebase', parent_operation, id)

    @classmethod
    def end_of_life_rebase_2(cls, parent_operation: str, old_id: str, new_id: str) -> Option:
        str_par = f"{old_id}={new_id}"
        return Option('--end-of-life-rebase', parent_operation, str_par)

    @classmethod
    def token_type(cls, parent_operation: str, value: str) -> Option:
        return Option('--token-type', parent_operation, value)

    @classmethod
    def timestamp(cls, parent_operation: str, time_stamp: str) -> Option:
        return Option('--timestamp', parent_operation, time_stamp)

    @classmethod
    def disable_fsync(cls, parent_operation: str) -> Option:
        return Option('--disable-fsync', parent_operation)

    @classmethod
    def disable_sandbox(cls, parent_operation: str) -> Option:
        return Option('--disable-sandbox', parent_operation)

    @classmethod
    def no_summary_index(cls, parent_operation: str) -> Option:
        return Option('--no-summary-index', parent_operation)

    @classmethod
    def repo_url(cls, parent_operation: str, address: str) -> Option:
        return Option('--repo-url', parent_operation, address)

    @classmethod
    def runtime_repo(cls, parent_operation: str, address: str) -> Option:
        return Option('--runtime-repo', parent_operation, address)

    @classmethod
    def gpg_keys(cls, parent_operation: str, file_path: Path) -> Option:
        if Path.is_file(file_path):
            return Option('--gpg-keys', parent_operation, file_path)
        else:
            logger.error(
                f'Path does not point to a file in [flatpak --gpg-keys] class method')

    @classmethod
    def from_commit(cls, parent_operation: str, commit: str) -> Option:
        return Option('--from-commit', parent_operation, commit)

    @classmethod
    def oci(cls, parent_operation: str) -> Option:
        return Option('--oci', parent_operation)

    @classmethod
    def ref(cls, parent_operation: str, ref: str) -> Option:
        return Option('--ref', parent_operation, ref)

    @classmethod
    def redirect_url(cls, parent_operation: str, address: str) -> Option:
        return Option('--redirect-url', parent_operation, address)

    @classmethod
    def deploy_sideload_collection_id(cls, parent_operation: str) -> Option:
        return Option('--deploy-sideload-collection-id', parent_operation)

    @classmethod
    def deploy_collection_id(cls, parent_operation: str) -> Option:
        return Option('--deploy-collection-id', parent_operation)

    @classmethod
    def generate_static_deltas(cls, parent_operation: str) -> Option:
        return Option('--generate-static-deltas', parent_operation)

    @classmethod
    def static_delta_jobs(cls, parent_operation: str, num_tasks: int) -> Option:
        str_par = str(num_tasks)
        return Option('--static-delta-jobs', parent_operation, str_par)

    @classmethod
    def static_delta_ignore_ref(cls, parent_operation: str, sample: str) -> Option:
        return Option('--static-delta-ignore-ref', parent_operation, sample)
    
    @classmethod
    def prune(cls, parent_operation: str) -> Option:
        return Option('--prune', parent_operation)

    @classmethod
    def prune_dry_run(cls, parent_operation: str) -> Option:
        return Option('--prune-dry-run', parent_operation)

    @classmethod
    def prune_depth(cls, parent_operation: str, depth: int) -> Option:
        str_par = str(depth)
        return Option('--prune-depth', parent_operation, str_par)

    @classmethod
    def no_update_appstream(cls, parent_operation: str) -> Option:
        return Option('--no-update-appstream', parent_operation)

    @classmethod
    def src_repo(cls, parent_operation: str, source_repo: str) -> Option:
        return Option('--src-repo', parent_operation, source_repo)

    @classmethod
    def src_ref(cls, parent_operation: str, source_ref: str) -> Option:
        return Option('--src-ref', parent_operation, source_ref)

    @classmethod
    def untrusted(cls, parent_operation: str) -> Option:
        return Option('--untrusted', parent_operation)

    @classmethod
    def extra_collection_id(cls, parent_operation: str, build_id: str) -> Option:
        return Option('--extra-collection-id', parent_operation, build_id)

    @classmethod
    def info(cls, parent_operation: str) -> Option:
        return Option('--info', parent_operation)

    @classmethod
    def branches(cls, parent_operation: str) -> Option:
        return Option('--branches', parent_operation)

    @classmethod
    def metadata_branch(cls, parent_operation: str, branch: str) -> Option:
        return Option('--metadata', parent_operation, branch)

    @classmethod
    def commits_branch(cls, parent_operation: str, branch: str) -> Option:
        return Option('--commits', parent_operation, branch)

    @classmethod
    def subsets(cls, parent_operation: str) -> Option:
        return Option('--subsets', parent_operation)

    @classmethod
    def subset_2(cls, parent_operation: str) -> Option:
        return Option('--subset', parent_operation)
        

class Flatpak(UniversalManager):

    class Install(Operation):
        operation = 'install'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'install'
            operation_alias = None
            default_options = '-y --noninteractive'

            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            '''Install the application or runtime in a per-user installation'''
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            '''Install the application or runtime in the default system-wide installation'''
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            '''Install the application or runtime in a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. 
            Using --installation=default is equivalent to using --system'''
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def arch(cls, apx: str) -> Option:
            '''The default architecture to install for, if not given explicitly in the REF . 
            See flatpak --supported-arches for architectures supported by the host'''
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def no_pull(cls) -> Option:
            '''Don't download the latest version, deploy whatever is locally available'''
            return _FlatpakOptions.no_pull(cls.operation)

        @classmethod
        def no_deploy(cls) -> Option:
            '''Download the latest version, but don't deploy it'''
            return _FlatpakOptions.no_deploy(cls.operation)

        @classmethod
        def no_related(cls) -> Option:
            '''Don't download related extensions, such as the locale data'''
            return _FlatpakOptions.no_related(cls.operation)

        @classmethod
        def no_deps(cls) -> Option:
            '''Don't verify runtime dependencies when installing'''
            return _FlatpakOptions.no_deps(cls.operation)

        @classmethod
        def no_auto_pin(cls) -> Option:
            return _FlatpakOptions.no_auto_pin(cls.operation)

        @classmethod
        def no_static_deltas(cls) -> Option:
            return _FlatpakOptions.no_static_deltas(cls.operation)

        @classmethod
        def runtime(cls) -> Option:
            '''Assume that all REF s are runtimes if not explicitly specified'''
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def app(cls) -> Option:
            '''Assume that all REF s are apps if not explicitly specified'''
            return _FlatpakOptions.app(cls.operation)

        @classmethod
        def include_sdk(cls) -> Option:
            return _FlatpakOptions.include_sdk(cls.operation)

        @classmethod
        def include_debug(cls) -> Option:
            return _FlatpakOptions.include_debug(cls.operation)

        @classmethod
        def bundle(cls) -> Option:
            '''Treat LOCATION as a single-bundle file. This is assumed if the argument ends with .flatpak'''
            return _FlatpakOptions.bundle(cls.operation)

        @classmethod
        def from_(cls) -> Option:
            '''Treat LOCATION as an application description file. This is assumed if the argument ends with .flatpakref'''
            return _FlatpakOptions.from_(cls.operation)

        @classmethod
        def gpg_file(cls, file_path: Path) -> Option:
            '''Check bundle signatures with GPG key from FILE (- for stdin)'''
            try:
                return _FlatpakOptions.gpg_file(cls.operation, file_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [gpg_file] method')

        @classmethod
        def subpath(cls, path: Path) -> Option:
            '''Install only a subpath of REF . This is mainly used to install a subset of locales. 
            This can be added multiple times to install multiple subpaths'''
            try:
                return _FlatpakOptions.subpath(cls.operation, path)
            except:
                logger.error(
                    'Failed to get optional parameter with [subpath] method')

        @classmethod
        def reinstall(cls) -> Option:
            '''Uninstall first if already installed'''
            return _FlatpakOptions.reinstall(cls.operation)

        @classmethod
        def or_update(cls) -> Option:
            '''Normally install just ignores things that are already installed (printing a warning), 
            but if --or-update is specified it silently turns it into an update operation instead'''
            return _FlatpakOptions.or_update(cls.operation)

        @classmethod
        def sideload_repo(cls, path: Path) -> Option:
            '''Adds an extra local ostree repo as source for installation. 
            This is equivalent to using the sideload-repos directories (see flatpak(1)), but can be done on a per-command basis. 
            Any path added here is used in addition to ones in those directories'''
            try:
                return _FlatpakOptions.sideload_repo(cls.operation, path)
            except:
                logger.error(
                    'Failed to get optional parameter with [sideload_repo] method')

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

       

    class Uninstall(Operation):
        operation = 'uninstall'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'uninstall'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def keep_ref(cls) -> Option:
            return _FlatpakOptions.keep_ref(cls.operation)

        @classmethod
        def no_related(cls) -> Option:
            return _FlatpakOptions.no_related(cls.operation)

        @classmethod
        def force_remove(cls) -> Option:
            return _FlatpakOptions.force_remove(cls.operation)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)

        @classmethod
        def unused(cls) -> Option:
            return _FlatpakOptions.unused(cls.operation)

        @classmethod
        def delete_data(cls) -> Option:
            return _FlatpakOptions.delete_data(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        

    class Update(Operation):
        operation = 'update'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'update'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)
        
        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def commit(cls) -> Option:
            return _FlatpakOptions.commit(cls.operation)
        
        @classmethod
        def force_remove(cls) -> Option:
            return _FlatpakOptions.force_remove(cls.operation)
        
        @classmethod
        def no_pull(cls) -> Option:
            return _FlatpakOptions.no_pull(cls.operation)
        
        @classmethod
        def no_deploy(cls) -> Option:
            return _FlatpakOptions.no_deploy(cls.operation)
        
        @classmethod
        def no_related(cls) -> Option:
            return _FlatpakOptions.no_related(cls.operation)
        
        @classmethod
        def no_deps(cls) -> Option:
            return _FlatpakOptions.no_deps(cls.operation)

        @classmethod
        def no_static_deltas(cls) -> Option:
            return _FlatpakOptions.no_static_deltas(cls.operation)
        
        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)
        
        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)
        
        @classmethod
        def appstream(cls) -> Option:
            return _FlatpakOptions.appstream(cls.operation)
        
        @classmethod
        def subpath(cls, path: Path) -> Option:
            try:
                return _FlatpakOptions.subpath(cls.operation, path)
            except:
                logger.error(
                    'Failed to get optional parameter with [subpath] method')

        @classmethod
        def sideload_repo(cls, path: Path) -> Option:
            try:
                return _FlatpakOptions.sideload_repo(cls.operation, path)
            except:
                logger.error(
                    'Failed to get optional parameter with [sideload_repo] method')
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        
    class Mask(Operation):
        operation = 'mask'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'mask'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)
        
        @classmethod
        def remove(cls) -> Option:
            return _FlatpakOptions.remove(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class Pin(Operation):
        operation = 'pin'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'pin'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def remove(cls) -> Option:
            return _FlatpakOptions.remove(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class List(Operation):
        operation = 'list'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'list'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def show_details(cls) -> Option:
            return _FlatpakOptions.show_details(cls.operation)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)
        
        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)
        
        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def app_runtime(cls, runtime: str) -> Option:
            return _FlatpakOptions.app_runtime(cls.operation, runtime)

        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        
    class Info(Operation):
        operation = 'info'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'info'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
    
        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def show_ref(cls) -> Option:
            return _FlatpakOptions.show_ref(cls.operation)

        @classmethod
        def show_commit(cls) -> Option:
            return _FlatpakOptions.show_commit(cls.operation)
        
        @classmethod
        def show_origin(cls) -> Option:
            return _FlatpakOptions.show_origin(cls.operation)

        @classmethod
        def show_size(cls) -> Option:
            return _FlatpakOptions.show_size(cls.operation)

        @classmethod
        def show_metadata(cls) -> Option:
            return _FlatpakOptions.show_metadata(cls.operation)
        
        @classmethod
        def show_runtime(cls) -> Option:
            return _FlatpakOptions.show_runtime(cls.operation)

        @classmethod
        def show_sdk(cls) -> Option:
            return _FlatpakOptions.show_sdk(cls.operation)

        @classmethod
        def show_permissions(cls) -> Option:
            return _FlatpakOptions.show_permissions(cls.operation)
        
        @classmethod
        def file_access(cls, path: Path) -> Option:
            try: 
                return _FlatpakOptions.file_access(cls.operation, path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')
                
        @classmethod
        def show_extensions(cls) -> Option:
            return _FlatpakOptions.show_extensions(cls.operation)

        @classmethod
        def show_location(cls) -> Option:
            return _FlatpakOptions.show_location(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class History(Operation):
        operation = 'history'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'history'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def since(cls, time: str) -> Option:
            return _FlatpakOptions.since(cls.operation, time)

        @classmethod
        def until(cls, time: str) -> Option:
            return _FlatpakOptions.until(cls.operation, time)

        @classmethod
        def reverse(cls) -> Option:
            return _FlatpakOptions.reverse(cls.operation)
        
        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Config(Operation):
        operation = 'config'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'config'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def list_(cls) -> Option:
            return _FlatpakOptions.list_(cls.operation)

        @classmethod
        def get(cls) -> Option:
            return _FlatpakOptions.get(cls.operation)

        @classmethod
        def set_(cls) -> Option:
            return _FlatpakOptions.set_(cls.operation)

        @classmethod
        def unset(cls) -> Option:
            return _FlatpakOptions.unset(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Repair(Operation):
        operation = 'repair'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'repair'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def dry_run(cls) -> Option:
            return _FlatpakOptions.dry_run(cls.operation)

        @classmethod
        def reinstall_all(cls) -> Option:
            return _FlatpakOptions.reinstall_all(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class CreateUSB(Operation):
        operation = 'create-usb'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'create-usb'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def destination_repo(cls, recognition: str) -> Option:
            return _FlatpakOptions.destination_repo(cls.operation, recognition)

        @classmethod
        def allow_partial(cls) -> Option:
            return _FlatpakOptions.allow_partial(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class Search(Operation):
        operation = 'search'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'search'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class Run(Operation):
        operation = 'run'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'run'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def command(cls, command: str) -> Option:
            return _FlatpakOptions.command(cls.operation, command)

        @classmethod
        def cwd(cls, dir: Path) -> Option:
            return _FlatpakOptions.cwd(cls.operation, dir)

        @classmethod
        def branch(cls, branch: str) -> Option:
            return _FlatpakOptions.branch(cls.operation, branch)

        @classmethod
        def devel(cls) -> Option:
            return _FlatpakOptions.devel(cls.operation)

        @classmethod
        def runtime(cls, env: str) -> Option:
            return _FlatpakOptions.runtime_env(cls.operation, env)

        @classmethod
        def runtime_version(cls, version: str) -> Option:
            return _FlatpakOptions.runtime_version(cls.operation, version)

        @classmethod
        def log_session_bus(cls) -> Option:
            return _FlatpakOptions.log_session_bus(cls.operation)

        @classmethod
        def log_system_bus(cls) -> Option:
            return _FlatpakOptions.log_system_bus(cls.operation)

        @classmethod
        def log_a11y_bus(cls) -> Option:
            return _FlatpakOptions.log_a11y_bus(cls.operation)

        @classmethod
        def no_a11y_bus(cls) -> Option:
            return _FlatpakOptions.no_a11y_bus(cls.operation)

        @classmethod
        def a11y_bus(cls) -> Option:
            return _FlatpakOptions.a11y_bus(cls.operation)

        @classmethod
        def no_session_bus(cls) -> Option:
            return _FlatpakOptions.no_session_bus(cls.operation)

        @classmethod
        def session_bus(cls) -> Option:
            return _FlatpakOptions.session_bus(cls.operation)

        @classmethod
        def session_bus(cls) -> Option:
            return _FlatpakOptions.session_bus(cls.operation)

        @classmethod
        def no_documents_portal(cls) -> Option:
            return _FlatpakOptions.no_documents_portal(cls.operation)

        @classmethod
        def file_forwarding(cls) -> Option:
            return _FlatpakOptions.file_forwarding(cls.operation)

        @classmethod
        def commit(cls) -> Option:
            return _FlatpakOptions.commit(cls.operation)

        @classmethod
        def runtime_commit(cls) -> Option:
            return _FlatpakOptions.runtime_commit(cls.operation)

        @classmethod
        def sandbox(cls) -> Option:
            return _FlatpakOptions.sandbox(cls.operation)

        @classmethod
        def die_with_parent(cls) -> Option:
            return _FlatpakOptions.die_with_parent(cls.operation)

        @classmethod
        def parent_pid(cls, pid: str) -> Option:
            return _FlatpakOptions.parent_pid(cls.operation, pid)

        @classmethod
        def parent_expose_pids(cls) -> Option:
            return _FlatpakOptions.parent_expose_pids(cls.operation)

        @classmethod
        def parent_share_pids(cls) -> Option:
            return _FlatpakOptions.parent_share_pids(cls.operation)

        @classmethod
        def instance_id_fd(cls) -> Option:
            return _FlatpakOptions.instance_id_fd(cls.operation)

        @classmethod
        def app_path(cls, path: Path) -> Option:
            return _FlatpakOptions.app_path(cls.operation, path)

        @classmethod
        def usr_path(cls, path: Path) -> Option:
            return _FlatpakOptions.usr_path(cls.operation, path)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        
        @classmethod
        def share(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.share(cls.operation, shared_resource)
        
        @classmethod
        def unshare(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.unshare(cls.operation, shared_resource)

        @classmethod
        def socket(cls, socket: str) -> Option:
            return _FlatpakOptions.socket(cls.operation, socket)

        @classmethod
        def nosocket(cls, socket: str) -> Option:
            return _FlatpakOptions.nosocket(cls.operation, socket)

        @classmethod
        def device(cls, device: str) -> Option:
            return _FlatpakOptions.device(cls.operation, device)

        @classmethod
        def nodevice(cls, device: str) -> Option:
            return _FlatpakOptions.nodevice(cls.operation, device)

        @classmethod
        def allow(cls, possibility: str) -> Option:
            return _FlatpakOptions.allow(cls.operation, possibility)

        @classmethod
        def disallow(cls, possibility: str) -> Option:
            return _FlatpakOptions.disallow(cls.operation, possibility)

        @classmethod
        def filesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.filesystem(cls.operation, file_system)

        @classmethod
        def nofilesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.nofilesystem(cls.operation, file_system)

        @classmethod
        def env(cls, variable: str, value: str) -> Option:
            return _FlatpakOptions.env(cls.operation, variable, value)

        @classmethod
        def env_fd(cls, file_descriptor: str) -> Option:
            return _FlatpakOptions.env_fd(cls.operation, file_descriptor)

        @classmethod
        def unset_env(cls, variable: str) -> Option:
            return _FlatpakOptions.unset_env(cls.operation, variable)

        @classmethod
        def own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.own_name(cls.operation, dbas_name)

        @classmethod
        def talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.talk_name(cls.operation, dbas_name)

        @classmethod
        def no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.no_talk_name(cls.operation, dbas_name)
        
        @classmethod
        def system_own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_own_name(cls.operation, dbas_name)

        @classmethod
        def system_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_no_talk_name(cls.operation, dbas_name)

        @classmethod
        def add_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.add_policy(cls.operation, subsystem, key, value)

        @classmethod
        def remove_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.remove_policy(cls.operation, subsystem, key, value)

        @classmethod
        def persist(cls, file_name: str) -> Option:
            return _FlatpakOptions.persist(cls.operation, file_name)
    
    class Override(Operation):
        operation = 'override'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'override'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def reset(cls) -> Option:
            return _FlatpakOptions.reset(cls.operation)

        @classmethod
        def show(cls) -> Option:
            return _FlatpakOptions.show(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

        @classmethod
        def share(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.share(cls.operation, shared_resource)

        @classmethod
        def unshare(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.unshare(cls.operation, shared_resource)

        @classmethod
        def socket(cls, socket: str) -> Option:
            return _FlatpakOptions.socket(cls.operation, socket)

        @classmethod
        def nosocket(cls, socket: str) -> Option:
            return _FlatpakOptions.nosocket(cls.operation, socket)

        @classmethod
        def device(cls, device: str) -> Option:
            return _FlatpakOptions.device(cls.operation, device)

        @classmethod
        def nodevice(cls, device: str) -> Option:
            return _FlatpakOptions.nodevice(cls.operation, device)

        @classmethod
        def allow(cls, possibility: str) -> Option:
            return _FlatpakOptions.allow(cls.operation, possibility)

        @classmethod
        def disallow(cls, possibility: str) -> Option:
            return _FlatpakOptions.disallow(cls.operation, possibility)

        @classmethod
        def filesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.filesystem(cls.operation, file_system)

        @classmethod
        def nofilesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.nofilesystem(cls.operation, file_system)

        @classmethod
        def env(cls, variable: str, value: str) -> Option:
            return _FlatpakOptions.env(cls.operation, variable, value)

        @classmethod
        def env_fd(cls, file_descriptor: str) -> Option:
            return _FlatpakOptions.env_fd(cls.operation, file_descriptor)
        
        @classmethod
        def unset_env(cls, variable: str) -> Option:
            return _FlatpakOptions.unset_env(cls.operation, variable)

        @classmethod
        def own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.own_name(cls.operation, dbas_name)

        @classmethod
        def talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.talk_name(cls.operation, dbas_name)

        @classmethod
        def no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.no_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_own_name(cls.operation, dbas_name)

        @classmethod
        def system_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_no_talk_name(cls.operation, dbas_name)

        @classmethod
        def add_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.add_policy(cls.operation, subsystem, key, value)

        @classmethod
        def remove_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.remove_policy(cls.operation, subsystem, key, value)

        @classmethod
        def persist(cls, file_name: str) -> Option:
            return _FlatpakOptions.persist(cls.operation, file_name)
    
    class MakeCurrent(Operation):
        operation = 'make-current'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'make-current'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Enter(Operation):
        operation = 'enter'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'enter'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class PS(Operation):
        operation = 'ps'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'ps'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class Kill(Operation):
        operation = 'kill'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'kill'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class Documents(Operation):
        operation = 'documents'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'documents'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class DocumentExport(Operation):
        operation = 'document-export'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'document-export'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def unique(cls) -> Option:
            return _FlatpakOptions.unique(cls.operation)

        @classmethod
        def transient(cls) -> Option:
            return _FlatpakOptions.transient(cls.operation)
        
        @classmethod
        def noexist(cls) -> Option:
            return _FlatpakOptions.noexist(cls.operation)

        @classmethod
        def allow_read(cls) -> Option:
            return _FlatpakOptions.allow_read(cls.operation)

        @classmethod
        def allow_write(cls) -> Option:
            return _FlatpakOptions.allow_write(cls.operation)

        @classmethod
        def allow_delete(cls) -> Option:
            return _FlatpakOptions.allow_delete(cls.operation)

        @classmethod
        def allow_grant_permission(cls) -> Option:
            return _FlatpakOptions.allow_grant_permission(cls.operation)

        @classmethod
        def forbid_read(cls) -> Option:
            return _FlatpakOptions.forbid_read(cls.operation)

        @classmethod
        def forbid_read(cls) -> Option:
            return _FlatpakOptions.forbid_write(cls.operation)

        @classmethod
        def forbid_read(cls) -> Option:
            return _FlatpakOptions.forbid_delete(cls.operation)

        @classmethod
        def forbid_read(cls) -> Option:
            return _FlatpakOptions.forbid_grant_permission(cls.operation)

        @classmethod
        def app(cls, app_id: str) -> Option:
            return _FlatpakOptions.appid(cls.operation, app_id)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    
    class DocumentUnexport(Operation):
        operation = 'document-unexport'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'document-unexport'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def doc_id(cls) -> Option:
            return _FlatpakOptions.doc_id(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class DocumentInfo(Operation):
        operation = 'document-info'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'document-info'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        
    class Permissions(Operation):
        operation = 'permissions'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'permissions'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class PermissionRemove(Operation):
        operation = 'permission-remove'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'permission-remove'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class PermissionSet(Operation):
        operation = 'permission-set'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'permission-set'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def data(cls, data: str) -> Option:
            return _FlatpakOptions.data(cls.operation, data)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class PermissionShow(Operation):
        operation = 'permission-show'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'permission-show'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class PermissionReset(Operation):
        operation = 'permission-reset'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'permission-reset'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def all(cls) -> Option:
            return _FlatpakOptions.all(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Remotes(Operation):
        operation = 'remotes'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remotes'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def show_details(cls) -> Option:
            return _FlatpakOptions.show_details(cls.operation)

        @classmethod
        def show_disabled(cls) -> Option:
            return _FlatpakOptions.show_disabled(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
        
        @classmethod
        def columns(cls, fields: list[str]) -> Option:
            try:
                return _FlatpakOptions.columns(cls.operation, fields)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')
        
    class RemoteAdd(Operation):
        operation = 'remote-add'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remote-add'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def no_gpg_verify(cls) -> Option:
            return _FlatpakOptions.no_gpg_verify(cls.operation)

        @classmethod
        def no_enumerate(cls) -> Option:
            return _FlatpakOptions.no_enumerate(cls.operation)
        
        @classmethod
        def no_use_for_deps(cls) -> Option:
            return _FlatpakOptions.no_use_for_deps(cls.operation)

        @classmethod
        def prio(cls, prio: str) -> Option:
            return _FlatpakOptions.prio(cls.operation, prio)

        @classmethod
        def subset(cls, subset: str) -> Option:
            return _FlatpakOptions.subset(cls.operation, subset)

        @classmethod
        def title(cls, title: str) -> Option:
            return _FlatpakOptions.title(cls.operation, title)

        @classmethod
        def comment(cls, comment: str) -> Option:
            return _FlatpakOptions.comment(cls.operation, comment)

        @classmethod
        def description(cls, description: str) -> Option:
            return _FlatpakOptions.description(cls.operation, description)

        @classmethod
        def homepage(cls, address: str) -> Option:
            return _FlatpakOptions.homepage(cls.operation, address)

        @classmethod
        def icon(cls, address: str) -> Option:
            return _FlatpakOptions.icon(cls.operation, address)

        @classmethod
        def default_branch(cls, branch: str) -> Option:
            return _FlatpakOptions.default_branch(cls.operation, branch)

        @classmethod
        def collection_id(cls, build_id: str) -> Option:
            return _FlatpakOptions.collection_id(cls.operation, build_id)

        @classmethod
        def gpg_import(cls, file_path: Path) -> Option:
            try:
                return _FlatpakOptions.gpg_import(cls.operation, file_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def filter(cls, file_path: Path) -> Option:
            try:
                return _FlatpakOptions.filter(cls.operation, file_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def disable(cls) -> Option:
            return _FlatpakOptions.disable(cls.operation)

        @classmethod
        def authenticator_name(cls, name: str) -> Option:
            return _FlatpakOptions.authenticator_name(cls.operation, name)

        @classmethod
        def authenticator_option(cls, key: str, value: str) -> Option:
            return _FlatpakOptions.authenticator_option(cls.operation, key, value)

        @classmethod
        def authenticator_install(cls) -> Option:
            return _FlatpakOptions.authenticator_install(cls.operation)

        @classmethod
        def no_authenticator_install(cls) -> Option:
            return _FlatpakOptions.no_authenticator_install(cls.operation)

        @classmethod
        def no_follow_redirect(cls) -> Option:
            return _FlatpakOptions.no_follow_redirect(cls.operation)

        @classmethod
        def if_not_exists(cls) -> Option:
            return _FlatpakOptions.if_not_exists(cls.operation)

        @classmethod
        def from_(cls) -> Option:
            return _FlatpakOptions.from_(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class RemoteModify(Operation):
        operation = 'remote-modify'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remote-modify'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def no_gpg_verify(cls) -> Option:
            return _FlatpakOptions.no_gpg_verify(cls.operation)

        @classmethod
        def no_enumerate(cls) -> Option:
            return _FlatpakOptions.no_enumerate(cls.operation)

        @classmethod
        def no_use_for_deps(cls) -> Option:
            return _FlatpakOptions.no_use_for_deps(cls.operation)

        @classmethod
        def prio(cls, prio: str) -> Option:
            return _FlatpakOptions.prio(cls.operation, prio)

        @classmethod
        def title(cls, title: str) -> Option:
            return _FlatpakOptions.title(cls.operation, title)

        @classmethod
        def comment(cls, comment: str) -> Option:
            return _FlatpakOptions.comment(cls.operation, comment)

        @classmethod
        def description(cls, description: str) -> Option:
            return _FlatpakOptions.description(cls.operation, description)

        @classmethod
        def homepage(cls, address: str) -> Option:
            return _FlatpakOptions.homepage(cls.operation, address)

        @classmethod
        def icon(cls, address: str) -> Option:
            return _FlatpakOptions.icon(cls.operation, address)

        @classmethod
        def default_branch(cls, branch: str) -> Option:
            return _FlatpakOptions.default_branch(cls.operation, branch)

        @classmethod
        def collection_id(cls, build_id: str) -> Option:
            return _FlatpakOptions.collection_id(cls.operation, build_id)

        @classmethod
        def gpg_import(cls, file_path: Path) -> Option:
            try:
                return _FlatpakOptions.gpg_import(cls.operation, file_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def filter(cls, file_path: Path) -> Option:
            try:
                return _FlatpakOptions.filter(cls.operation, file_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def disable(cls) -> Option:
            return _FlatpakOptions.disable(cls.operation)

        @classmethod
        def authenticator_name(cls, name: str) -> Option:
            return _FlatpakOptions.authenticator_name(cls.operation, name)

        @classmethod
        def authenticator_option(cls, key: str, value: str) -> Option:
            return _FlatpakOptions.authenticator_option(cls.operation, key, value)

        @classmethod
        def authenticator_install(cls) -> Option:
            return _FlatpakOptions.authenticator_install(cls.operation)

        @classmethod
        def no_authenticator_install(cls) -> Option:
            return _FlatpakOptions.no_authenticator_install(cls.operation)

        @classmethod
        def follow_redirect(cls) -> Option:
            return _FlatpakOptions.follow_redirect(cls.operation)

        @classmethod
        def gpg_verify(cls) -> Option:
            return _FlatpakOptions.gpg_verify(cls.operation)

        @classmethod
        def enumerate(cls) -> Option:
            return _FlatpakOptions.enumerate(cls.operation)

        @classmethod
        def use_for_deps(cls) -> Option:
            return _FlatpakOptions.use_for_deps(cls.operation)

        @classmethod
        def url(cls, address: str) -> Option:
            return _FlatpakOptions.url(cls.operation, address)

        @classmethod
        def enable(cls) -> Option:
            return _FlatpakOptions.enable(cls.operation)

        @classmethod
        def update_metadata(cls) -> Option:
            return _FlatpakOptions.update_metadata(cls.operation)

        @classmethod
        def subset(cls, subset: str) -> Option:
            return _FlatpakOptions.subset(cls.operation, subset)

        @classmethod
        def no_follow_redirect(cls) -> Option:
            return _FlatpakOptions.no_follow_redirect(cls.operation)

        @classmethod
        def if_not_exists(cls) -> Option:
            return _FlatpakOptions.if_not_exists(cls.operation)

        @classmethod
        def from_(cls) -> Option:
            return _FlatpakOptions.from_(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class RemoteDelete(Operation):
        operation = 'remote-delete'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remote-delete'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def force(cls) -> Option:
            return _FlatpakOptions.force(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class RemoteLs(Operation):
        
        operation = 'remote-ls'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remote-ls'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)

        @classmethod
        def updates(cls) -> Option:
            return _FlatpakOptions.updates(cls.operation)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def all(cls) -> Option:
            return _FlatpakOptions.all(cls.operation)

        @classmethod
        def app_runtime(cls, runtime: str) -> Option:
            return _FlatpakOptions.app_runtime(cls.operation, runtime)

        @classmethod
        def app_runtime(cls, fields: list[str]) -> Option:
            return _FlatpakOptions.columns(cls.operation, fields)
        
        @classmethod
        def cached(cls) -> Option:
            return _FlatpakOptions.cached(cls.operation)

        @classmethod
        def sideloaded(cls) -> Option:
            return _FlatpakOptions.sideloaded(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class RemoteInfo(Operation):

        operation = 'remote-info'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'remote-info'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def user(cls) -> Option:
            return _FlatpakOptions.user(cls.operation)

        @classmethod
        def system(cls) -> Option:
            return _FlatpakOptions.system(cls.operation)

        @classmethod
        def installation(cls, name: str) -> Option:
            return _FlatpakOptions.installation(cls.operation, name)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def commit(cls, commit: str) -> Option:
            return _FlatpakOptions.commit(cls.operation, commit)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def app(cls) -> Option:
            return _FlatpakOptions.app(cls.operation)

        @classmethod
        def log(cls) -> Option:
            return _FlatpakOptions.log(cls.operation)
        
        @classmethod
        def show_ref(cls) -> Option:
            return _FlatpakOptions.show_ref(cls.operation)

        @classmethod
        def show_commit(cls) -> Option:
            return _FlatpakOptions.show_commit(cls.operation)

        @classmethod
        def show_parent(cls) -> Option:
            return _FlatpakOptions.show_parent(cls.operation)

        @classmethod
        def show_metadata(cls) -> Option:
            return _FlatpakOptions.show_metadata(cls.operation)

        @classmethod
        def show_runtime(cls) -> Option:
            return _FlatpakOptions.show_runtime(cls.operation)

        @classmethod
        def show_sdk(cls) -> Option:
            return _FlatpakOptions.show_sdk(cls.operation)

        @classmethod
        def cached(cls) -> Option:
            return _FlatpakOptions.cached(cls.operation)

        @classmethod
        def sideloaded(cls) -> Option:
            return _FlatpakOptions.sideloaded(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class BuildInit(Operation):

        operation = 'build-init'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-init'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def var(cls, runtime_env: str) -> Option:
            return _FlatpakOptions.var(cls.operation, runtime_env)

        @classmethod
        def base(cls, app: str) -> Option:
            return _FlatpakOptions.base(cls.operation, app)

        @classmethod
        def base_version(cls, version: str) -> Option:
            return _FlatpakOptions.base_version(cls.operation, version)

        @classmethod
        def base_extension(cls, extension: str) -> Option:
            return _FlatpakOptions.base_extension(cls.operation, extension)

        @classmethod
        def extension_tag(cls, tag: str) -> Option:
            return _FlatpakOptions.extension_tag(cls.operation, tag)

        @classmethod
        def writable_sdk(cls) -> Option:
            return _FlatpakOptions.writable_sdk(cls.operation)
        
        @classmethod
        def type_(cls, type_: str) -> Option:
            return _FlatpakOptions.type_(cls.operation, type_)

        @classmethod
        def tag(cls, tag: str) -> Option:
            return _FlatpakOptions.tag(cls.operation, tag)

        @classmethod
        def sdk_extension(cls, extension: str) -> Option:
            return _FlatpakOptions.sdk_extension(cls.operation, extension)

        @classmethod
        def extension(cls, name: str, variable: str, value: str) -> Option:
            return _FlatpakOptions.extension(cls.operation, name, variable, value)

        @classmethod
        def sdk_dir(cls, dir_path: Path) -> Option:
            try: 
                return _FlatpakOptions.sdk_dir(cls.operation, dir_path)
            except:
                logger.error(
                    'Failed to get optional parameter with [columns] method')

        @classmethod
        def update(cls) -> Option:
            return _FlatpakOptions.update(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Build(Operation):

        operation = 'build'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)
        
        @classmethod
        def sdk_dir(cls, dir_path: Path) -> Option:
            return _FlatpakOptions.sdk_dir(cls.operation, dir_path)

        @classmethod
        def die_with_parent(cls) -> Option:
            return _FlatpakOptions.die_with_parent(cls.operation)

        @classmethod
        def log_session_bus(cls) -> Option:
            return _FlatpakOptions.log_session_bus(cls.operation)

        @classmethod
        def log_system_bus(cls) -> Option:
            return _FlatpakOptions.log_system_bus(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

        @classmethod
        def share(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.share(cls.operation, shared_resource)
        
        @classmethod
        def unshare(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.unshare(cls.operation, shared_resource)

        @classmethod
        def socket(cls, socket: str) -> Option:
            return _FlatpakOptions.socket(cls.operation, socket)

        @classmethod
        def nosocket(cls, socket: str) -> Option:
            return _FlatpakOptions.nosocket(cls.operation, socket)

        @classmethod
        def device(cls, device: str) -> Option:
            return _FlatpakOptions.device(cls.operation, device)

        @classmethod
        def nodevice(cls, device: str) -> Option:
            return _FlatpakOptions.nodevice(cls.operation, device)

        @classmethod
        def allow(cls, possibility: str) -> Option:
            return _FlatpakOptions.allow(cls.operation, possibility)

        @classmethod
        def disallow(cls, possibility: str) -> Option:
            return _FlatpakOptions.disallow(cls.operation, possibility)

        @classmethod
        def filesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.filesystem(cls.operation, file_system)

        @classmethod
        def nofilesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.nofilesystem(cls.operation, file_system)

        @classmethod
        def env(cls, variable: str, value: str) -> Option:
            return _FlatpakOptions.env(cls.operation, variable, value)

        @classmethod
        def env_fd(cls, file_descriptor: str) -> Option:
            return _FlatpakOptions.env_fd(cls.operation, file_descriptor)

        @classmethod
        def unset_env(cls, variable: str) -> Option:
            return _FlatpakOptions.unset_env(cls.operation, variable)

        @classmethod
        def own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.own_name(cls.operation, dbas_name)
        
        @classmethod
        def talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.talk_name(cls.operation, dbas_name)

        @classmethod
        def no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.no_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_own_name(cls.operation, dbas_name)

        @classmethod
        def system_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_no_talk_name(cls.operation, dbas_name)

        @classmethod
        def add_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.add_policy(cls.operation, subsystem, key, value)

        @classmethod
        def remove_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.remove_policy(cls.operation, subsystem, key, value)

        @classmethod
        def readonly(cls) -> Option:
            return _FlatpakOptions.readonly(cls.operation)
        
        @classmethod
        def bind_mount(cls, appointment: str, source: str) -> Option:
            return _FlatpakOptions.bind_mount(cls.operation, appointment, source)

        @classmethod
        def build_dir(cls, dir_path: str) -> Option:
            return _FlatpakOptions.build_dir(cls.operation, dir_path)

        @classmethod
        def metadata(cls, file_path: str) -> Option:
            return _FlatpakOptions.metadata(cls.operation, file_path)

        @classmethod
        def with_appdir(cls) -> Option:
            return _FlatpakOptions.with_appdir(cls.operation)

    class BuildFinish(Operation):
        operation = 'build-finish'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-finish'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def command(cls, command: str) -> Option:
            return _FlatpakOptions.command(cls.operation, command)
        
        @classmethod
        def require_version(cls, major: str, minor: str, micro: str) -> Option:
            return _FlatpakOptions.require_version(cls.operation, major, minor, micro)

        @classmethod
        def no_exports(cls) -> Option:
            return _FlatpakOptions.no_exports(cls.operation)

        @classmethod
        def extra_data(cls) -> Option:
            return _FlatpakOptions.extra_data(cls.operation)

        @classmethod
        def extension(cls, name: str, variable: str, value: str) -> Option:
            return _FlatpakOptions.extension(cls.operation, name, variable, value)

        @classmethod
        def remove_extension(cls, name: str) -> Option:
            return _FlatpakOptions.remove_extension(cls.operation, name)
        
        @classmethod
        def extension_priority(cls, value: str) -> Option:
            return _FlatpakOptions.extension_priority(cls.operation, value)

        @classmethod
        def sdk(cls, sdk: str) -> Option:
            return _FlatpakOptions.sdk(cls.operation, sdk)

        @classmethod
        def runtime(cls, env: str) -> Option:
            return _FlatpakOptions.runtime_env(cls.operation, env)

        @classmethod
        def metadata(cls, group: str, key: str, value: str) -> Option:
            return _FlatpakOptions.metadata_group(cls.operation, group, key, value)

        @classmethod
        def no_inherit_permissions(cls) -> Option:
            return _FlatpakOptions.no_inherit_permissions(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

        @classmethod
        def share(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.share(cls.operation, shared_resource)

        @classmethod
        def unshare(cls, shared_resource: str) -> Option:
            return _FlatpakOptions.unshare(cls.operation, shared_resource)

        @classmethod
        def socket(cls, socket: str) -> Option:
            return _FlatpakOptions.socket(cls.operation, socket)

        @classmethod
        def nosocket(cls, socket: str) -> Option:
            return _FlatpakOptions.nosocket(cls.operation, socket)

        @classmethod
        def device(cls, device: str) -> Option:
            return _FlatpakOptions.device(cls.operation, device)

        @classmethod
        def nodevice(cls, device: str) -> Option:
            return _FlatpakOptions.nodevice(cls.operation, device)

        @classmethod
        def allow(cls, possibility: str) -> Option:
            return _FlatpakOptions.allow(cls.operation, possibility)

        @classmethod
        def disallow(cls, possibility: str) -> Option:
            return _FlatpakOptions.disallow(cls.operation, possibility)

        @classmethod
        def filesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.filesystem(cls.operation, file_system)

        @classmethod
        def nofilesystem(cls, file_system: str) -> Option:
            return _FlatpakOptions.nofilesystem(cls.operation, file_system)

        @classmethod
        def env(cls, variable: str, value: str) -> Option:
            return _FlatpakOptions.env(cls.operation, variable, value)

        @classmethod
        def env_fd(cls, file_descriptor: str) -> Option:
            return _FlatpakOptions.env_fd(cls.operation, file_descriptor)

        @classmethod
        def unset_env(cls, variable: str) -> Option:
            return _FlatpakOptions.unset_env(cls.operation, variable)

        @classmethod
        def own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.own_name(cls.operation, dbas_name)

        @classmethod
        def talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.talk_name(cls.operation, dbas_name)

        @classmethod
        def no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.no_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_own_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_own_name(cls.operation, dbas_name)

        @classmethod
        def system_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_talk_name(cls.operation, dbas_name)

        @classmethod
        def system_no_talk_name(cls, dbas_name: str) -> Option:
            return _FlatpakOptions.system_no_talk_name(cls.operation, dbas_name)

        @classmethod
        def add_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.add_policy(cls.operation, subsystem, key, value)

        @classmethod
        def remove_policy(cls, subsystem: str, key: str, value: str) -> Option:
            return _FlatpakOptions.remove_policy(cls.operation, subsystem, key, value)

        @classmethod
        def persist(cls, file_name: str) -> Option:
            return _FlatpakOptions.persist(cls.operation, file_name)

    class BuildExport(Operation):
        operation = 'build-export'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-export'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)
        
        @classmethod
        def subject(cls, subject: str) -> Option:
            return _FlatpakOptions.subject(cls.operation, subject)
        
        @classmethod
        def body(cls, body: str) -> Option:
            return _FlatpakOptions.body(cls.operation, body)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)
        
        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def update_appstream(cls) -> Option:
            return _FlatpakOptions.update_appstream(cls.operation)
        
        @classmethod
        def no_update_summary(cls) -> Option:
            return _FlatpakOptions.no_update_summary(cls.operation)

        @classmethod
        def files(cls, sub_dir: Path) -> Option:
            return _FlatpakOptions.files(cls.operation, sub_dir)

        @classmethod
        def metadata(cls, file_path: Path) -> Option:
            return _FlatpakOptions.metadata(cls.operation, file_path)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def exclude(cls, example: str) -> Option:
            return _FlatpakOptions.exclude(cls.operation, example)
        
        @classmethod
        def include(cls, example: str) -> Option:
            return _FlatpakOptions.include(cls.operation, example)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)

        @classmethod
        def subset(cls, subset: str) -> Option:
            return _FlatpakOptions.subset(cls.operation, subset)

        @classmethod
        def end_of_life(cls, reason: str) -> Option:
            return _FlatpakOptions.end_of_life(cls.operation, reason)

        @classmethod
        def end_of_life_rebase(cls, id: str) -> Option:
            return _FlatpakOptions.end_of_life_rebase(cls.operation, id)

        @classmethod
        def token_type(cls, value: str) -> Option:
            return _FlatpakOptions.token_type(cls.operation, value)

        @classmethod
        def timestamp(cls, time_stamp: str) -> Option:
            return _FlatpakOptions.timestamp(cls.operation, time_stamp)

        @classmethod
        def collection_id(cls, build_id: str) -> Option:
            return _FlatpakOptions.collection_id(cls.operation, build_id)

        @classmethod
        def disable_fsync(cls) -> Option:
            return _FlatpakOptions.disable_fsync(cls.operation)

        @classmethod
        def disable_sandbox(cls) -> Option:
            return _FlatpakOptions.disable_sandbox(cls.operation)

        @classmethod
        def no_summary_index(cls) -> Option:
            return _FlatpakOptions.no_summary_index(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class BuildBundle(Operation):
        operation = 'build-bundle'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-bundle'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def repo_url(cls, address: str) -> Option:
            return _FlatpakOptions.repo_url(cls.operation, address)

        @classmethod
        def runtime_repo(cls, address: str) -> Option:
            return _FlatpakOptions.runtime_repo(cls.operation, address)

        @classmethod
        def gpg_keys(cls, file_path: Path) -> Option:
            return _FlatpakOptions.gpg_keys(cls.operation, file_path)
        
        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)
        
        @classmethod
        def from_commit(cls, commit: str) -> Option:
            return _FlatpakOptions.from_commit(cls.operation, commit)

        @classmethod
        def oci(cls) -> Option:
            return _FlatpakOptions.oci(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class BuildImportBundle(Operation):
        operation = 'build-import-bundle'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-import-bundle'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def ref(cls, ref: str) -> Option:
            return _FlatpakOptions.ref(cls.operation, ref)

        @classmethod
        def oci(cls) -> Option:
            return _FlatpakOptions.oci(cls.operation)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)

        @classmethod
        def update_appstream(cls) -> Option:
            return _FlatpakOptions.update_appstream(cls.operation)

        @classmethod
        def no_update_summary(cls) -> Option:
            return _FlatpakOptions.no_update_summary(cls.operation)

        @classmethod
        def no_summary_index(cls) -> Option:
            return _FlatpakOptions.no_summary_index(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)
    
    class BuildSign(Operation):
        operation = 'build-sign'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-sign'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def arch(cls, apx: str) -> Option:
            return _FlatpakOptions.arch(cls.operation, apx)

        @classmethod
        def runtime(cls) -> Option:
            return _FlatpakOptions.runtime(cls.operation)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class BuildUpdateRepo(Operation):
        operation = 'build-update-repo'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-update-repo'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def redirect_url(cls, address: str) -> Option:
            return _FlatpakOptions.redirect_url(cls.operation, address)

        @classmethod
        def title(cls, title: str) -> Option:
            return _FlatpakOptions.title(cls.operation, title)

        @classmethod
        def comment(cls, comment: str) -> Option:
            return _FlatpakOptions.comment(cls.operation, comment)

        @classmethod
        def description(cls, description: str) -> Option:
            return _FlatpakOptions.description(cls.operation, description)

        @classmethod
        def homepage(cls, address: str) -> Option:
            return _FlatpakOptions.homepage(cls.operation, address)

        @classmethod
        def icon(cls, address: str) -> Option:
            return _FlatpakOptions.icon(cls.operation, address)

        @classmethod
        def default_branch(cls, branch: str) -> Option:
            return _FlatpakOptions.default_branch(cls.operation, branch)

        @classmethod
        def collection_id(cls, build_id: str) -> Option:
            return _FlatpakOptions.collection_id(cls.operation, build_id)

        @classmethod
        def deploy_sideload_collection_id(cls) -> Option:
            return _FlatpakOptions.deploy_sideload_collection_id(cls.operation)

        @classmethod
        def deploy_collection_id(cls) -> Option:
            return _FlatpakOptions.deploy_collection_id(cls.operation)

        @classmethod
        def authenticator_name(cls, name: str) -> Option:
            return _FlatpakOptions.authenticator_name(cls.operation, name)

        @classmethod
        def authenticator_install(cls) -> Option:
            return _FlatpakOptions.authenticator_install(cls.operation)

        @classmethod
        def no_authenticator_install(cls) -> Option:
            return _FlatpakOptions.no_authenticator_install(cls.operation)

        @classmethod
        def authenticator_option(cls, key: str, value: str) -> Option:
            return _FlatpakOptions.authenticator_option(cls.operation, key, value)

        @classmethod
        def gpg_import(cls, file_path: Path) -> Option:
            return _FlatpakOptions.gpg_import(cls.operation, file_path)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)

        @classmethod
        def generate_static_deltas(cls) -> Option:
            return _FlatpakOptions.generate_static_deltas(cls.operation)

        @classmethod
        def no_update_summary(cls) -> Option:
            return _FlatpakOptions.no_update_summary(cls.operation)

        @classmethod
        def no_update_appstream(cls) -> Option:
            return _FlatpakOptions.no_update_appstream(cls.operation)

        @classmethod
        def static_delta_jobs(cls, num_tasks: int) -> Option:
            return _FlatpakOptions.static_delta_jobs(cls.operation, num_tasks)

        @classmethod
        def static_delta_ignore_ref(cls, sample: str) -> Option:
            return _FlatpakOptions.static_delta_ignore_ref(cls.operation, sample)

        @classmethod
        def prune(cls) -> Option:
            return _FlatpakOptions.prune(cls.operation)

        @classmethod
        def prune_dry_run(cls) -> Option:
            return _FlatpakOptions.prune_dry_run(cls.operation)

        @classmethod
        def prune_depth(cls, depth: int) -> Option:
            return _FlatpakOptions.prune_depth(cls.operation, depth)

        @classmethod
        def no_summary_index(cls) -> Option:
            return _FlatpakOptions.no_summary_index(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class BuildCommitFrom(Operation):
        operation = 'build-commit-from'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'build-commit-from'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def src_repo(cls, source_repo: str) -> Option:
            return _FlatpakOptions.src_repo(cls.operation, source_repo)

        @classmethod
        def src_ref(cls, source_ref: str) -> Option:
            return _FlatpakOptions.src_ref(cls.operation, source_ref)

        @classmethod
        def untrusted(cls) -> Option:
            return _FlatpakOptions.untrusted(cls.operation)

        @classmethod
        def force(cls) -> Option:
            return _FlatpakOptions.force(cls.operation)

        @classmethod
        def extra_collection_id(cls, build_id: str) -> Option:
            return _FlatpakOptions.extra_collection_id(cls.operation, build_id)

        @classmethod
        def subset(cls, subset: str) -> Option:
            return _FlatpakOptions.subset(cls.operation, subset)

        @classmethod
        def subject(cls, subject: str) -> Option:
            return _FlatpakOptions.subject(cls.operation, subject)

        @classmethod
        def body(cls, body: str) -> Option:
            return _FlatpakOptions.body(cls.operation, body)

        @classmethod
        def update_appstream(cls) -> Option:
            return _FlatpakOptions.update_appstream(cls.operation)

        @classmethod
        def no_update_summary(cls) -> Option:
            return _FlatpakOptions.no_update_summary(cls.operation)

        @classmethod
        def gpg_sign(cls, key_id: str) -> Option:
            return _FlatpakOptions.gpg_sign(cls.operation, key_id)

        @classmethod
        def gpg_homedir(cls, home_dir: Path) -> Option:
            return _FlatpakOptions.gpg_homedir(cls.operation, home_dir)

        @classmethod
        def end_of_life(cls, reason: str) -> Option:
            return _FlatpakOptions.end_of_life(cls.operation, reason)

        @classmethod
        def end_of_life_rebase(cls, old_id: str, new_id: str) -> Option:
            return _FlatpakOptions.end_of_life_rebase_2(cls.operation, old_id, new_id)

        @classmethod
        def token_type(cls, value: str) -> Option:
            return _FlatpakOptions.token_type(cls.operation, value)

        @classmethod
        def timestamp(cls, time_stamp: str) -> Option:
            return _FlatpakOptions.timestamp(cls.operation, time_stamp)

        @classmethod
        def disable_fsync(cls) -> Option:
            return _FlatpakOptions.disable_fsync(cls.operation)

        @classmethod
        def no_summary_index(cls) -> Option:
            return _FlatpakOptions.no_summary_index(cls.operation)

        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    class Repo(Operation):
        operation = 'repo'

        def __init__(self) -> None:
            parent_label = pkgm.flatpak
            operation = 'repo'
            operation_alias = None
            default_options = '-y --noninteractive'
            super().__init__(parent_label, operation, operation_alias, default_options)

        @classmethod
        def info(cls) -> Option:
            return _FlatpakOptions.info(cls.operation)

        @classmethod
        def branches(cls) -> Option:
            return _FlatpakOptions.branches(cls.operation)

        @classmethod
        def metadata(cls, branch: str) -> Option:
            return _FlatpakOptions.metadata_branch(cls.operation, branch)

        @classmethod
        def commits(cls, branch: str) -> Option:
            return _FlatpakOptions.commits_branch(cls.operation, branch)

        @classmethod
        def subsets(cls) -> Option:
            return _FlatpakOptions.subsets(cls.operation)

        @classmethod
        def subset(cls) -> Option:
            return _FlatpakOptions.subset(cls.operation)
        
        @classmethod
        def verbose(cls) -> Option:
            return _FlatpakOptions.verbose(cls.operation)

        @classmethod
        def ostree_verbose(cls) -> Option:
            return _FlatpakOptions.ostree_verbose(cls.operation)

    @classmethod
    def __prepare(cls, *params: str) -> str:
        print(params)
        list_par = [arg for arg in params]
        print(list_par)
        str_par = " ".join(list_par)
        print(str_par)
        return str_par

    @classmethod
    def install(cls, arg: str, options: list[Option] = None, head_options: list[Option] = None) -> str:
        cmd = cls.Install().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def remove(cls, arg: str, options: list[Option] = None, head_options: list[Option] = None) -> str:
        cmd = cls.Uninstall().get_cmd(arg, options, head_options)
        return cmd

    @classmethod
    def update(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Update().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def mask(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Mask().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def pin(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Pin().get_cmd(arg, options=options)
        return cmd
    
    @classmethod
    def list_(cls, options: list[Option] = None) -> str:
        cmd = cls.List().get_cmd(options=options)
        return cmd

    @classmethod
    def info(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Info().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def history(cls, options: list[Option] = None) -> str:
        cmd = cls.History().get_cmd(options=options)
        return cmd

    @classmethod
    def config(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Config().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def repair(cls, options: list[Option] = None) -> str:
        cmd = cls.Repair().get_cmd(options=options)
        return cmd
    
    @classmethod
    def create_usb(cls, mnt_path: str = None, ref: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(mnt_path, ref)
        cmd = cls.CreateUSB().get_cmd(str_par, options=options)
        return cmd

    @classmethod
    def search(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Search().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def run(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Run().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def override(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Override().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def make_current(cls, app: str, branch: str, options: list[Option] = None) -> str:
        str_par = cls.__prepare(app, branch)
        cmd = cls.MakeCurrent().get_cmd(str_par, options=options)
        return cmd

    @classmethod
    def enter(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Enter().get_cmd(arg, options=options)
        return cmd
    
    @classmethod
    def enter(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Enter().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def ps(cls, options: list[Option] = None) -> str:
        cmd = cls.PS().get_cmd(options=options)
        return cmd
    
    @classmethod
    def kill(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Kill().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def kill(cls, arg: str = None, options: list[Option] = None) -> str:
        cmd = cls.Kill().get_cmd(arg, options=options)
        return cmd

    @classmethod
    def documents(cls, id_: str = None, options: list[Option] = None) -> str:
        cmd = cls.Documents().get_cmd(id_, options=options)
        return cmd

    @classmethod
    def documents(cls, id_: str = None, options: list[Option] = None) -> str:
        cmd = cls.Documents().get_cmd(id_, options=options)
        return cmd
    
    @classmethod
    def document_export(cls, file_: str, options: list[Option] = None) -> str:
        cmd = cls.DocumentExport().get_cmd(file_, options=options)
        return cmd

    @classmethod
    def document_unexport(cls, file_: str, options: list[Option] = None) -> str:
        cmd = cls.DocumentUnexport().get_cmd(file_, options=options)
        return cmd

    @classmethod
    def document_info(cls, file_: str, options: list[Option] = None) -> str:
        cmd = cls.DocumentInfo().get_cmd(file_, options=options)
        return cmd
    
    @classmethod
    def permissions(cls, table: str = None, id_: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(table, id_)
        cmd = cls.Permissions().get_cmd(str_par, options=options)
        return cmd
    
    @classmethod
    def permission_remove(cls, table: str, id_: str, options: list[Option] = None) -> str:
        str_par = cls.__prepare(table, id_)
        cmd = cls.PermissionRemove().get_cmd(str_par, options=options)
        return cmd

    @classmethod
    def permission_set(cls, table: str, id_: str, app_id: str, access: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(table, id_, app_id, access)
        cmd = cls.PermissionSet().get_cmd(str_par, options=options)
        return cmd
    
    @classmethod
    def permission_show(cls, app_id: str, options: list[Option] = None) -> str:
        cmd = cls.PermissionShow().get_cmd(app_id, options=options)
        return cmd
    
    @classmethod
    def permission_reset(cls, app_id: str, options: list[Option] = None) -> str:
        cmd = cls.PermissionReset().get_cmd(app_id, options=options)
        return cmd
    
    @classmethod
    def remotes(cls, options: list[Option] = None) -> str:
        cmd = cls.Remotes().get_cmd(options=options)
        return cmd

    @classmethod
    def remote_add(cls, name: str, location: str, options: list[Option] = None) -> str:
        str_par = cls.__prepare(name, location)
        cmd = cls.RemoteAdd().get_cmd(str_par, options=options)
        return cmd

    @classmethod
    def remote_modify(cls, name: str, options: list[Option] = None) -> str:
        cmd = cls.RemoteModify().get_cmd(name, options=options)
        return cmd

    @classmethod
    def remote_delete(cls, name: str, options: list[Option] = None) -> str:
        cmd = cls.RemoteDelete().get_cmd(name, options=options)
        return cmd

    @classmethod
    def remote_ls(cls, storage_or_address: str, options: list[Option] = None) -> str:
        cmd = cls.RemoteLs().get_cmd(storage_or_address, options=options)
        return cmd
    
    @classmethod
    def remote_info(cls, storage: str, name: str, options: list[Option] = None) -> str:
        str_par = cls.__prepare(storage, name)
        cmd = cls.RemoteInfo().get_cmd(str_par, options=options)
        return cmd
    
    def build(cls, dir_path: str, commands: list[str] = None, options: list[Option] = None) -> str:
        ### ????
        str_par = ' '
        list_par = [dir_path]
        list_par.extend(commands)
        for el in list_par:
            if el:
                str_par.join(el)
        cmd = cls.Build().get_cmd(str_par, options=options)
        return cmd

    def build_finish(cls, dir_path: str, options: list[Option] = None) -> str:
        cmd = cls.BuildFinish().get_cmd(dir_path, options=options)
        return cmd

    def build_export(cls, location: str, dir_path: str, brunch: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(location, dir_path, brunch)
        cmd = cls.BuildExport().get_cmd(str_par, options=options)
        return cmd

    def build_bundle(cls, location: str, file_name: str, name: str, brunch: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(location, file_name, name, brunch)
        cmd = cls.BuildBundle().get_cmd(str_par, options=options)
        return cmd

    def build_import_bundle(cls, location: str, file_name: str, options: list[Option] = None) -> str:
        str_par = cls.__prepare(location, file_name)
        cmd = cls.BuildImportBundle().get_cmd(str_par, options=options)
        return cmd

    def build_sign(cls, location: str, ids: list[str] = None, options: list[Option] = None) -> str:
        #### ????
        str_par = ' '
        list_par = [location]
        list_par.extend(ids)
        for el in list_par:
            if el:
                str_par.join(el)
        cmd = cls.BuildSign().get_cmd(str_par, options=options)
        return cmd

    def build_update_repo(cls, location: str, options: list[Option] = None) -> str:
        cmd = cls.BuildUpdateRepo().get_cmd(location, options=options)
        return cmd

    def build_commit_from(cls, dst_repo: str, dst_ref: str = None, options: list[Option] = None) -> str:
        str_par = cls.__prepare(dst_repo, dst_ref)
        cmd = cls.BuildCommitFrom().get_cmd(str_par, options=options)
        return cmd

    def build_update_repo(cls, location: str, options: list[Option] = None) -> str:
        cmd = cls.Repo().get_cmd(location, options=options)
        return cmd

    def __str__(self) -> str:
        return self.__class__.__name__
