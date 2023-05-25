class Config:
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DATABASE_URI = ''

class TestingConfig(Config):
    DATABASE_URI = ''
    TESTING = True