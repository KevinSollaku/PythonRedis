from protocollo import Server
if __name__ == '__main__':
    from gevent import monkey; monkey.patch_all()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    Server().run()