from config.bootstrap import get_config
from chat.views import add_message


def set_routes(router):
    config = get_config()

    router.add_get('/add', add_message)
    router.add_static('/static', config['base_path'] + '/static')