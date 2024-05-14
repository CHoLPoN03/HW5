import configparser
def read_initial_money():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['Settings']['MY_MONEY'])