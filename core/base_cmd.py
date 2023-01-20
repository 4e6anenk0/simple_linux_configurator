import getpass
from functools import wraps
import subprocess
import shlex


class BaseCmd:
    def __init__(self):
        self.outputs = {}
        self.errors = {}

    def _postprocess_handler(self, procces: subprocess.Popen[bytes]):
        # повертає typle[bytes, bytes] з виводом та помилками, попередньо обробив результати
        
        output, error = procces.communicate()
        if output:
            print(
                f"All done! Returned code is: {procces.returncode}")
        if error:
            print(f"Returned code is: {procces.returncode}")
            print(f"Error: {error.decode('utf-8').strip()}")

        return output, error

    def _check_has_password(self, password):
        if password:
            return True
        else:
            return False

    def shellroot_run_cmd(self,
                           cmd: str,
                           password: str,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE
                           ):
        
        if not self._check_has_password(password):
            print('Password is empty!')
            return
        
        sudo_cmd = ['sh', '-c',
                    f'echo {password} | sudo -S {cmd}']
        
        return subprocess.Popen(
            sudo_cmd,
            stdout=stdout,
            stderr=stderr,
            stdin=stdin
        )

    def root_run_cmd(self,
                      cmd: str,
                      password: str,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      ):
        def get_sudo_str(cmd: str):
            sudo_cmd = ['sudo', '-S']
            cmd = shlex.split(cmd)
            sudo_cmd.extend(cmd)
            return sudo_cmd

        if not self._check_has_password(password):
            print('Password is empty!')
            return
        
        sub_proc = subprocess.Popen(
            ['echo', password], stdout=subprocess.PIPE)
        
        return subprocess.Popen(
            get_sudo_str(cmd),
            stdout=stdout,
            stderr=stderr,
            stdin=sub_proc.stdout
        )

    def run_cmd(self,
                 cmd: str,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 stdin=subprocess.PIPE
                 ):
        return subprocess.Popen(
            shlex.split(cmd),
            stdout=stdout,
            stderr=stderr,
            stdin=stdin
        )
    
    def postprocess(func):
        @wraps(func)
        def wraper(*args, **kwargs):
            self = args[0]
            procces = func(*args, **kwargs)
            output, error = self._postprocess_handler(procces)
            self.outputs[f'{procces}']
            return procces 
        return wraper

    def run(self, cmd: str, password=None, root=False):
        procces = self._cmd(cmd, password, root)
        output, error = self._postprocess_handler(procces=procces)
        self.output = output.decode('utf-8')
        print(self.output)

    def decode(self, procces: subprocess.Popen[bytes], format = 'utf-8'):
        # Вихід результату виконання команд, можна передати для декодування у цю функцію
        output = procces.stdout.read().decode(f'{format}')
        error = procces.stderr.read().decode(f'{format}')

        return output, error

    def chained_run(self, *cmds: str, password=None, root=False):
        temporal_proc = self._cmd(cmds[0], password, root)
        for i in range(len(cmds) - 1):
            temporal_proc = self._cmd(cmds[i + 1], password, root)
