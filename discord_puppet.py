import requests
from discord import Webhook, RequestsWebhookAdapter
import sys
import argparse

parser = argparse.ArgumentParser(description="Discord Puppet Integration",
                                 usage="echo $DISCORD_SERVER_URL | python3 discord_puppet.py [options]")
parser.add_argument('-f', metavar='-file',
                    help="Send a file to a discord server")
parser.add_argument('-m', metavar='-message',
                    help="Send a message to a discord server")
parser.add_argument('-c', metavar='-code',
                    help="Send a code formatted message to a discord server")
args = parser.parse_args()

web = sys.stdin.readlines()[0].strip("\n")
webhook = Webhook.from_url(web, adapter=RequestsWebhookAdapter())

# Sending message to discord server
if (args.m):
    print(args.m)
    webhook.send(args.m)
    exit(0)

# Sending file to discord server
if (args.f):
    with open(file=args.f, mode='rb') as f:
        my_file = discord.File(f)
        webhook.send(file=my_file)
        exit(0)

# Sending message in code format to discord server
if (args.c):
    with open(args.c) as file:
        results = ""
        results += "```\n"
        for line in file:
            results += line
        results += "```\n"
        webhook.send(results)
        exit(0)
