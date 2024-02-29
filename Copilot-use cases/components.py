class Components:
    def __init__(self, config):
        self.active_host = config.get('memcached.active.host')
        self.active_port = config.get('memcached.active.port')
        self.stand_by_host = config.get('memcached.standBy.host')
        self.stand_by_port = config.get('memcached.standBy.port')

        self.rabbit_mq_host = config.get('rabbitmq.address')
        self.rabbit_mq_port = config.get('rabbitmq.port')
        self.rabbit_mq_user = config.get('rabbitmq.username')
        self.rabbit_mq_password = config.get('rabbitmq.password')

        self.elasticsearch_host = config.get('elasticsearch.host')
        self.elasticsearch_port = config.get('elasticsearch.port')
        self.elasticsearch_cluster = config.get('elasticsearch.cluster')
        self.elasticsearch_node = config.get('elasticsearch.node')

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