import discord
import responses


async def send_messages(message, user_message, user_id, is_private):
    try:
        async with message.channel.typing():
            response = responses.handle_response(user_message) + f" <@{user_id}>"
            await message.author.send(response) if is_private else await  message.channel.send(response)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = #Your dicord app TOKEN
    URL = #Your discord bot url
    intents = discord.Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} funciona!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_id = str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel)
        if user_message[0] == '?': 
           user_message = user_message[1:]
           await send_messages(message, user_message, user_id, is_private=True)
        elif user_message[0] == '!':
           await send_messages(message, user_message, user_id, is_private=False) 
        
    client.run(TOKEN)
