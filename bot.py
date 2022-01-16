#!/usr/bin/env python3
import configparser
import random

# https://github.com/kyb3r/dhooks
from dhooks import Webhook

# open the config file
parser = configparser.ConfigParser()
parser.read('/etc/discordbot/config')

# grab the webhook url from the config file
cfg = parser['discord']
webhook_url = cfg.get('webhook')

# use dhooks to create a webhook object
webhook = Webhook(webhook_url)

# pick a random line from the message file to send
with open('/etc/discordbot/messages') as file:
    all_messages = file.read().splitlines()
    random_message = random.choice(all_messages)

    # use the webhook object to send the message
    webhook.send(random_message)