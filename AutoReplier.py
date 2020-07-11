import discord
import __future__

TOKEN = input("Token: ") # Prompt the user for the bot token

reply_dict = {}

while True:

    user_id = input(

        "Type person {}'s user id. This can be found by right clicking on their profile and selecting 'Copy ID.' Type 'DONE' when finished inputting users. \n".format(
            len(reply_dict) + 1))
    print("\n")

    if user_id == 'DONE':

        print("You have finished inputting users and replies. The bot will now start.\n")
        break

    try:
        int(user_id)

    except:

        print("User ID's can only contain numbers. Type 'DONE' if you have finished inputting users.\n")

        continue

    reply_message = input("Type the message that the bot should reply to this user with. \n")
    print("\n")

    reply_dict[user_id] = reply_message

    print("The bot will reply to the user with the ID {} with '{}' whenever they send a message. \n".format(user_id, reply_message))


client = discord.Client()

@client.event
async def on_message(message):

    print(message.content)

    if str(message.author.id) in reply_dict and not message.author.bot:

        await message.channel.send(reply_dict[str(message.author.id)])

        return

client.run(TOKEN)
