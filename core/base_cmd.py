from core import log
import subprocess
import shlex

logger = log.get_logger(__name__)


class ValidatedCmd:
    def __init__(self) -> None:
        self.__cmd = None
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

class BaseCmd:
    def __init__(self, cmd: str = None):
        self.__cmd = cmd

    @property
    def cmd(self):
        return self.__cmd

    def __str__(self) -> str:
        return self.cmd

    def _check_has_password(self, password):
        if password and password != '':
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
                      stdin=subprocess.PIPE
                      ):
        sudo_cmd = ['sudo', '-S']
        cmd = shlex.split(cmd)
        sudo_cmd.extend(cmd)

        p = subprocess.Popen(
            sudo_cmd,
            stdout=stdout,
            stderr=stderr,
            stdin=stdin
        )

        p.stdin.write(f'{password}\n'.encode('utf-8'))
        p.stdin.flush()

        return p

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

    def _process_runner_handler(self, cmd: str, process: subprocess.Popen[bytes]) -> subprocess.CompletedProcess[bytes]:
        """ with process:
            errs = []
            for line in iter(process.stderr.readline, b''):
                logger.error(
                    f'Command: {cmd} - Error: {line.decode().rstrip()}')
                errs.append(line) """
        returncode = process.wait()
        stdout, stderr = process.communicate()
        
        if returncode != 0:
            logger.error(f'Return code is not 0. Error: {stderr.decode("utf-8")}')
        
        result = subprocess.CompletedProcess(
            cmd, returncode, stdout, stderr)

        return result

    def _check_error(completed: subprocess.CompletedProcess[bytes]):
        if completed.stderr and completed.returncode != 0:
            logger.error(
                f"Error execution of command: {completed.stderr.decode('utf-8')}")
            raise Exception()
        else:
            return

    def run(self, cmd: str) -> subprocess.CompletedProcess[bytes]:
        """ if isinstance(cmd, ValidatedCmd) == False:
            logger.warning(
                'Failed to pass validation because the passed value has unsafe attributes!')
            return """

        try:
            process = self.run_cmd(cmd)
            completed = self._process_runner_handler(cmd, process)
            if completed.stderr and completed.returncode != 0:
                logger.error(f"Error execution of command: {completed.stderr.decode('utf-8')}")
                raise Exception()
            """ self._check_error(completed) """
            return completed
        except OSError:
            logger.error(
                f'Process cannot be created and transferred to [_process_runner_handler]. Command: {cmd}')
        
    def root_run(self, cmd: str, password: str, shell: bool = False) -> subprocess.CompletedProcess[bytes]:
        if self._check_has_password(password) == False:
            logger.info('Password is empty!')
            return
        
        if shell == False:
            try:
                process = self.root_run_cmd(cmd, password) 
                completed = self._process_runner_handler(cmd, process)
                if completed.stderr and completed.returncode != 0:
                    raise Exception()
                """ self._check_error(completed) """
                return completed
            except OSError:
                logger.error(
                    f'Process cannot be created and transferred to [_process_runner_handler]. Command: {cmd}')
        else:
            try:
                process = self.shellroot_run_cmd(cmd, password)
                completed = self._process_runner_handler(cmd, process)
                if completed.stderr and completed.returncode != 0:
                    raise Exception()
                """ self._check_error(completed) """
                return completed
            except OSError:
                logger.error(
                    f'Process cannot be created and transferred to [_process_runner_handler]. Command: {cmd}')


    def decode_process(self, process: subprocess.Popen[bytes], format = 'utf-8'):
        # Вихід результату виконання команд, можна передати для декодування у цю функцію
        output = process.stdout.read().decode(f'{format}')
        error = process.stderr.read().decode(f'{format}')

        return output, error

    def decode(self, result: subprocess.CompletedProcess[bytes]):
        output = None
        error = None

        if result == None:
            return output, error

        if result.stdout:
            output = result.stdout.decode('utf-8')
        
        if result.stderr:
            error = result.stderr.decode('utf-8')
        

        return output, error

    def chained_run(self, *cmds: str, password=None, root=False):
        temporal_proc = self._cmd(cmds[0], password, root)
        for i in range(len(cmds) - 1):
            temporal_proc = self._cmd(cmds[i + 1], password, root)

    def apply():
        pass
