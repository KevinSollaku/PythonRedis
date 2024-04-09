from protocollo import Client
from collections import namedtuple
from io import BytesIO
from socket import error as socket_error
import logging
import json

logger = logging.getLogger(__name__)

class CommandError(Exception): pass
class Disconnect(Exception): pass

Error = namedtuple('Error', ('message',))

if __name__ == '__main__':
    client = Client()
    client.set('kx', {'vx': {'vy': 0, 'vz': [1, 2, 3]}})
