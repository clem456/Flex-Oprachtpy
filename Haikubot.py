import selfcord
import json
import requests
from selfcord.ext.commands import Bot

config = ''

sentances = ["hallo", "mijn naam is", "clement"]

client = Bot(
    command_prefix='.',
    self_bot=True
)

@client.event
async def on_ready():
    print("im ready")

@client.command()
async def haiku(ctx, *, keyword='haiku'):
    print("it works", str(haiku))
    url = "https://haiku.kremer.dev/?keyword=haiku"
    resp = requests.get(url).json()

    print(resp)

    msg = ""

    for index, sentance in enumerate(resp, 1):
        if index == 1:
            msg += sentance
        else:
            msg += "\n"+sentance

    await ctx.send(msg)

if __name__ == "__main__":
    client.run(config)