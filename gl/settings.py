try:
    import redis
    REDIS_INS = True
except ImportError:
    REDIS_INS = False

# Global variables

DEBUG = False

PLUGINS = {}
ALL_PLUGINS = set()
ENABLED_PLUGINS = set()
DISABLED_PLUGINS_ON_CHAT = {}
SUDO_USERS = set()
DISABLED_CHANNELS = set()
OUR_ID = 0
