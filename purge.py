import asyncio
import discord
from discord.ext.commands import Bot
Token = 'MzkyODA3MzQyMjQ2MTk5Mjk3.DRsl6A.U_Ecd90uVdEpgKVoQlg5b5Th44A'
Client = Bot('!')


@Client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await Client.delete_messages(mgs)

Client.run(Token)
