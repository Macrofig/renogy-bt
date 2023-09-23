import logging
import configparser
import os
from renogybt import RoverClient

logging.basicConfig(level=logging.DEBUG)

config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

def on_data_received(client, data):
    logging.debug("{} => {}".format(client.device.alias(), data))
    client.disconnect()


# start client
RoverClient(config, on_data_received).connect() 
