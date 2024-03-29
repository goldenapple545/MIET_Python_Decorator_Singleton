import sys


class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log_info(self, message):
        print(f'[INFO]: {message}')

    def log_error(self, message):
        print(f'[ERROR]: {message}', file=sys.stderr)

    def log_warning(self, message):
        print(f'[WARNING]: {message}')
