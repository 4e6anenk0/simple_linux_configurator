import getpass
import subprocess
import shlex


class BaseCmd:
    def __init__(self):
        self.result_exec = None
    
    def _cmd(self, cmd: str, password = None, root = None, timeout = 30):
        print(password)
        try:
            if root:
                if password:
                    sudo_cmd = ['sudo', '-S']
                    command = shlex.split(cmd)
                    sudo_cmd.extend(command)                  
                    proc = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
                    
                    return subprocess.Popen(
                    sudo_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=proc.stdout
                    )
                else:
                    print("Password is empty!")
                    return
            else:
                print("Without root")
                return subprocess.Popen(
                    shlex.split(cmd),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE
                )
                
        except FileNotFoundError as ex:
            print(f"Command [{cmd}] failed because the executable could not be found.\n{ex}")
        except subprocess.CalledProcessError as ex:
            print(
                f"Command [{cmd}] failed because did not return a successful return code. "
                f"Returned {ex.returncode}\n{ex}"
            )
        except subprocess.TimeoutExpired as ex:
            print(f"Command [{cmd}] timed out.\n{ex}")

    def root_run(self, cmd: str, password: str):
        result = self._cmd(cmd, password, root=True)
        if result == None:
            print('Result is None!')
            return
        self.result_exec = result.stdout.read().decode('utf-8')
        print(self.result_exec)

    def run(self, cmd: str):
        result = self._cmd(cmd)
        if result == None:
            print('Result is None!')
            return
        self.result_exec = result.stdout.read().decode('utf-8')
        print(self.result_exec)