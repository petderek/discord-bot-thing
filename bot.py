#!/usr/bin/env python3
from datetime import date
import calendar
import configparser

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

day_of_week = calendar.day_name[date.today().weekday()].lower()

# string replace will give us sunday/monday/tuesday
wod_file_name = '/etc/discordbot/wod.{}'.format(day_of_week) 

# get the list of messages and pick based on day of week
with open(wod_file_name) as file:
    message = file.read()
    # use the webhook object to send the message
    webhook.send(message)