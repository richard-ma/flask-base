class Config:
    TESTING = False

    def __str__(self):
        return "/".join([k+": "+v for k, v in vars(self.__class__).items() if not k.startswith('_')])

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DATABASE_URI = ''

class TestingConfig(Config):
    DATABASE_URI = ''
    TESTING = True