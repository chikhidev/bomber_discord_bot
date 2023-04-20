import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else message.channel.send(response)

    except Exception as e:
        await message.author.send(e)






def run_discord_bot():
    TOKEN = 'MTA5ODQwMDg4MTkxNDk1Nzg4NA.GU9hje.BnFi4Usq48P7SFAQAb5_Aqd3xfuUg85lqaYpIw'
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("start working")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_name = str(message.author),
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{user_name} said {user_message} in {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)
    
    client.run(TOKEN)
