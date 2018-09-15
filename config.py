"""
module config
"""
class Config:
    """
    parent config class
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True

class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """
    class for production configuration
    """
    DEBUG = False
    TESTING = False