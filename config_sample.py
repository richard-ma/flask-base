class Config:
    TESTING = False
    LOGGING_FILE_MAX_BYTES = 1024 * 1024
    LOGGING_FILE_BACKUP_COUNT = 10

    def __str__(self):
        return "/".join([k+": "+v for k, v in vars(self.__class__).items() if not k.startswith('_')])

class ProductionConfig(Config):
    DATABASE_URI = ''
    LOGGING_FILENAME = 'production.log'

class DevelopmentConfig(Config):
    DATABASE_URI = ''
    LOGGING_FILENAME = 'development.log'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = ''
    LOGGING_FILENAME = 'testing.log'