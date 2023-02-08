import configparser
from enum import Enum
from pathlib import PosixPath


class Sections(Enum):
    '''
    Нові секції для ini файлу треба додати сюди, та з точно таким ключем до 
    класу конфігурації з дефолтними значеннями у вигляді словаря. Це 
    забезпечить відповідність значення, для функцій генерації та ініціалізації
    '''
    logging = 'Logging'
    localization = 'Localization'
    project = 'Project'

class Levels(Enum):
    notset = 'NOTSET'
    debug = 'DEBUG'
    Info = 'INFO'
    warning = 'WARNING'
    error = 'ERROR'
    critical = 'CRITICAL'

class Langs(Enum):
    ukranian = 'ukr'
    russian = 'rus'
    english = 'eng'

class Modes(Enum):
    '''
    Use [dev] setting for verbose console output, use [prod] setting for compact console output
    '''
    dev = 'dev'
    prod = 'prod'

class EqualBetweenParams(Enum):
    '''Use to globally determine whether to use "=" between parameters. If [True] then "=" will be used'''
    true = 'True'
    false = 'False'


class CompactCommands(Enum):
    '''Use to globally determine whether to use "=" between parameters. If [True] then "=" will be used'''
    true = 'True'
    false = 'False'

class Settings:
    def __init__(self):
        # root_path - папка з проєектом
        self.root_path = PosixPath(__file__).parent.parent
        self.log_path = self.root_path.joinpath('logs/logs.txt')
        self.path_to_ini_file = self.root_path.joinpath('settings.ini')
        # default settings:
        self.logging = {'level' : Levels.debug.value}
        self.localization = {'lang' : Langs.english.value}
        self.project = {'mode' : Modes.dev.value,
                        'equal' : EqualBetweenParams.false.value,
                        'use_compact_commands' : CompactCommands.false.value}
        
    @staticmethod
    def get_section(section) -> dict:
        '''
        get_section - функція для прямого отримання налаштувань з файлу за конкретною секцією
        '''
        parserINI = configparser.ConfigParser()
        mapped_dict = {}
        options = parserINI.options(section)
        for option in options:
            try:
                mapped_dict[option] = parserINI.get(section, option)
                if mapped_dict[option] == -1:
                    print(f'skip: {option}')
            except:
                print(f'exeption on {option}!!!')
                mapped_dict[option] = None
        return mapped_dict

    def generate_default_ini(self):
        '''
        generate_default_ini - це допоміжна функція для генерації шаблону settings.ini 
        з дефолтними значеннями
        '''
        default_ini = configparser.ConfigParser()
        try:
            for section in Sections:
                default_ini.add_section(section.value)
                try: 
                    atr = dict(getattr(self, section.name))

                    for key, value in atr.items():
                        default_ini.set(section.value, key, value)

                except: 
                    print(
                        f"Error. Can't to set section with class attribute values. \
                            Used method [ConfigParser.set()] with [{section}] section")
                    return False
        except:
            print(f"Error. Can't to prepare ConfigParser with Settings class attributes")
            return False

        with open(f'{self.path_to_ini_file}', 'w') as f:
            print(f'A new file was created at the path: {self.path_to_ini_file}')
            default_ini.write(f)
        
        return True
    
    def check_and_create_logs_file(self):
        if PosixPath(self.log_path).is_file:
            return
        else:
            #create logs file
            PosixPath.touch(self.log_path)

    
    def init(self) -> bool:
        '''
        init - це функція яка оновлює значення налаштувань з файлу ini. Параметри класу відповідатимуть
        параметрам вказаним у файлі налаштувань. Важливо, щоб файл був створений відповідно до шаблону. 
        Для цього можна скористуватись функцією [generate_default_ini]
        '''

        # Initializing from a file settings.ini
        if PosixPath(self.path_to_ini_file).is_file:
            parserINI = configparser.ConfigParser()
            
            try:
                parserINI.read(f"{self.path_to_ini_file}")
                
                for section in Sections:
                    atr = dict(getattr(self, section.name))
                    for key in atr:
                        try: 
                            new_value = parserINI.get(section.value, key)
                            atr[key] = new_value
                        except:
                            return False
                        
                        setattr(self, section.name, atr)
                        
            except:
                print('Init Error!')
                return False
        else:
            print("Configuration file not created. It will be created...")
            self.generate_default_ini()
            self.init("Initialization again...")

        # other init scripts
        self.check_and_create_logs_file()

        return True



settingsObj = Settings()
#settingsObj.init()


def init_settings():
    settingsObj.init()