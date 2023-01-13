import getpass
import subprocess
import shlex


class BaseCmd:
    def __init__(self):
        self.output_exec = None

    def _get_sudo_str_list_cmd(self, cmd: str):
        sudo_cmd = ['sudo', '-S']
        cmd = shlex.split(cmd)
        sudo_cmd.extend(cmd)
        return sudo_cmd

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

    def _cmd(self, cmd: str, password=None, root=None, timeout=30):

        try:
            if root:
                if password:
                    sub_proc = subprocess.Popen(
                        ['echo', password], stdout=subprocess.PIPE)

                    return subprocess.Popen(
                        self._get_sudo_str_list_cmd(cmd),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdin=sub_proc.stdout
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

        except OSError as e:
            print(
                f"OSError: {e.errno} \n OSError: {e.strerror} \n OSError: {e.filename}")

    def run(self, cmd: str, password=None, root=False):
        result = self._cmd(cmd, password, root)
        output, error = self._subprocess_handler(result=result)
        self.output_exec = output.decode('utf-8')
        print(self.output_exec)