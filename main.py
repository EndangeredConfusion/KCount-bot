import discord
from ignore_keys import BOT_TOKEN
import json
from json_model import JsonModel


def update_json(serverID: str, counting: bool):
    with open('variables.json', 'r', encoding='utf-8') as outfile:
        data = {serverID: counting}
        try:
            data = json.load(outfile)
            data[serverID] = counting
        except json.decoder.JSONDecodeError:
            pass

    with open('variables.json', 'w', encoding='utf-8') as outfile:
        outfile.seek(0)
        outfile.truncate()
        outfile.write(json.dumps(data))


def read_json(serverID: str):
    with open('variables.json', 'r', encoding='utf-8') as infile:
        try:
            data = json.load(infile)
            print(data)
            if str(serverID) in data.keys():
                return data[str(serverID)]
        except json.decoder.JSONDecodeError:
            return False

def runBot():
    discord_token = BOT_TOKEN
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    @client.event
    async def on_message(message):
        print("message")

        if message.author == client.user:
            print("own message")
            return

        else:
            if message.content.lower() == '!start':
                await message.channel.send(":)")
                update_json(message.guild.id, True)

            elif message.content.lower() == '!stop':
                await message.channel.send(":(")
                update_json(message.guild.id, False)

            else:
                if read_json(message.guild.id):
                    try:
                        num = int(message.content.lower())
                        print(f"{num} sent")
                        await message.channel.send(num + 1)

                    except ValueError:
                        return

    client.run(discord_token)


if __name__ == '__main__':
    runBot()
