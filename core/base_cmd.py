import getpass
import subprocess
import shlex


class BaseCmd:
    def __init__(self):
        self.output_exec = None

    def _subprocess_handler(self, result: subprocess.Popen[bytes]):
        # повертає typle[bytes, bytes] з виводом та помилками, попередньо обробив результати
        output, error = result.communicate()

        if output:
            print(
                f"All done! Returned code is: {result.returncode}")
        if error:
            print(f"Returned code is: {result.returncode}")
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
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )

    def run(self, cmd: str, password=None, root=False):
        result = self._cmd(cmd, password, root)
        output, error = self._subprocess_handler(result=result)
        self.output_exec = output.decode('utf-8')
        print(self.output_exec)

    def chained_run(self, *cmds: str, password=None, root=False):
        temporal_proc = self._cmd(cmds[0], password, root)
        for i in range(len(cmds) - 1):
            temporal_proc = self._cmd(cmds[i + 1], password, root)
