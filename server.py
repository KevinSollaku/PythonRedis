from protocollo import Server
from collections import namedtuple
from io import BytesIO
from socket import error as socket_error
import logging
import json

logger = logging.getLogger(__name__)

class CommandError(Exception): pass
class Disconnect(Exception): pass

Error = namedtuple('Error', ('message',))