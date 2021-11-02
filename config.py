class CommonConfig(object):
    """
    公共配置
    """


class DevelopmentConfig(CommonConfig):
    """
    开发环境配置
    """
    DEBUG = True
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(CommonConfig):
    """
    正式环境配置
    """
    DEBUG = False
    FLASK_DEBUG = False


class TestingConfig(CommonConfig):
    """
    测试环境配置
    """

    TESTING = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
