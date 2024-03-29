import time


class LoggerWriterToFile:
    def __init__(self, logger):
        self.__logger = logger

    def log_info_to_file(self, filename, message):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        with open(filename, 'a') as file:
            file.write(f'[INFO]{current_time}: {message}\n')
        self.__logger.log_info(message)

    def log_error_to_file(self, filename, message):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        with open(filename, 'a') as file:
            file.write(f'[ERROR]{current_time}: {message}\n')
        self.__logger.log_error(message)

    def log_error_to_stderr(self, message):
        self.__logger.log_error(message)

    def log_warning_to_file(self, filename, message):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        with open(filename, 'a') as file:
            file.write(f'[WARNING]{current_time}: {message}\n')
        self.__logger.log_warning(message)
