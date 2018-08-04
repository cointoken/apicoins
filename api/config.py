LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(lineno)s:  %(asctime)s - %(name)s - %(levelname)s - %(message)s',
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
            'filename': 'log/logging.log',
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