LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(filename)s: %(funcName)s: %(lineno)s:  %(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'log/errors.log',
            'level': 'ERROR',
            'formatter': 'default'
        },
    },
    'loggers':{
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            # 'propagate': True,
        },
        'default': {
            'handlers': ['console', 'file'],
            'level': 'WARN',
        }
    }
}

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toApx08@c#@localhost:3307/exchange'