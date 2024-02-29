class Components:
    def __init__(self, config):
        keys = ['memcached.active.host', 'memcached.active.port', 'memcached.standBy.host', 'memcached.standBy.port',
                'rabbitmq.address', 'rabbitmq.port', 'rabbitmq.username', 'rabbitmq.password',
                'elasticsearch.host', 'elasticsearch.port', 'elasticsearch.cluster', 'elasticsearch.node']

        for key in keys:
            setattr(self, key.replace('.', '_'), config.get(key))

# Usage:
# config = {
#     'memcached.active.host': 'localhost',
#     'memcached.active.port': '11211',
#     'memcached.standBy.host': 'localhost',
#     'memcached.standBy.port': '11212',
#     'rabbitmq.address': 'localhost',
#     'rabbitmq.port': '5672',
#     'rabbitmq.username': 'guest',
#     'rabbitmq.password': 'guest',
#     'elasticsearch.host': 'localhost',
#     'elasticsearch.port': '9200',
#     'elasticsearch.cluster': 'elasticsearch',
#     'elasticsearch.node': 'node-1'
# }
# components = Components(config)