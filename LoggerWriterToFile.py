class LoggerWriterToFile:
    def __init__(self, logger):
        self.__logger = logger

    def log_info_to_file(self, filename, message):
        with open(filename, 'a') as file:
            file.write(f'[INFO]: {message}\n')
        self.__logger.log_info(message)

    def log_error_to_file(self, filename, message):
        with open(filename, 'a') as file:
            file.write(f'[ERROR]: {message}\n')
        self.__logger.log_error(message)

    def log_error_to_stderr(self, message):
        self.__logger.log_error(message)

    def log_warning_to_file(self, filename, message):
        with open(filename, 'a') as file:
            file.write(f'[WARNING]: {message}\n')
        self.__logger.log_warning(message)
