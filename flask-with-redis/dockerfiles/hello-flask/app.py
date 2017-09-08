import os
import logging
import logging.config
import logging.handlers
from flask import Flask, Blueprint, request
from redis import Redis

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('hello-flask');
logger = logging.LoggerAdapter(logger, {'hostname': os.environ['HOSTNAME']})

b1 = Blueprint('frontend', __name__, url_prefix=os.environ['URL_PREFIX'])

app = Flask(__name__)
redis = Redis(host='redis-server', port=6379)

@b1.route('/')
def hello():
    count = redis.incr('hits')
    logger.info('Received %s' % (request))
    return 'Hello World! (%d times).\n' %(count)


if __name__ == "__main__":
    app.register_blueprint(b1)
    app.run(host="0.0.0.0", debug=True)
