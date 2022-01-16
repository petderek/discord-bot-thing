# discord-bot-thing

### About
 
This is a discord robit, mainly to learn how discord webhooks work.

For now, we're keeping it simple. It uses [cron](https://man7.org/linux/man-pages/man8/cron.8.html) and a [python3](https://www.python.org/) script to post to the [discord api](https://discord.com/developers/docs/resources/webhook#execute-webhook)

Its config file is expected to be in `/etc/discordbot/config` and it looks for messages in `/etc/discordbot/wod.${day-of-week}`.

Config files use the python [configparser library](https://docs.python.org/3/library/configparser.html). The config options are as follows:

```
# this is the webhook url you get from discord
webhook=https://example.com/blah
```

### Dependencies

Your system needs to be running python3 and it needs `dhooks` installed via pip:

```
pip install dhooks
```

### How to run

After creating the config and message files, you can run this like:

```
python bot.py
```

However, the intended use is to be invoked as a cron job. 