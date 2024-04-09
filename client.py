from protocollo import client
if __name__ == '__main__':
    client = Client()
    client.set('kx', {'vx': {'vy': 0, 'vz': [1, 2, 3]}})
