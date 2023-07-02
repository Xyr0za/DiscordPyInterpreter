from discord.ext import commands
from discord.ui import Button, View
import discord
import time
import logging
from hotreload import Loader


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    script = Loader("exece.py")

BOT_TOKEN = 
CHANNEL_ID = None
1
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Main funcs


def validity_query(msg):
    lines = msg.split("\n")

    if (lines[0][0:] != "```py") or (lines[-1] != "```") or ("input(" in msg):

        if lines[0][0:] != "```py":
            return False, "Language Error"

        return False, "Syntax Error"
    return True, None


def refactor(code):
    out = []
    outer = []
    code = code.split("\n")[1:-1]

    for i in code:
        out.append(f"    {i}")

    for i in out:
        i = i.replace('print', 'main_output_array.append')
        outer.append(i)

    outer = ["def main():", "    main_output_array = []"] + outer + ["    return main_output_array"]
    return "\n".join(outer)

# Bot funcs


@bot.command()
async def run(ctx, arg):

    button = Button(label="Rerun", style=discord.ButtonStyle.green)
    blank = View()
    view = View()
    view.add_item(button)

    # async def button_callback(interaction):
    #     global editable
    #     await interaction.response.defer()
    #
    #     currentMessage = await ctx.fetch_message(arg)
    #     isValid = validity_query(message.content)
    #
    #     if valid[0]:
    #
    #         editable = await ctx.channel.send(f"**{arg}**\n```py\nRefactoring...\n```", view=blank)
    #
    #         await editable.edit(content=f"\n```py\nCompiling...\n```")
    #         open('exece.py', 'w').close()
    #         with open("exece.py", "a") as f:
    #             f.write(refactor(message.content))
    #             f.close()
    #
    #         # Time for the file to update and save for the hotreload to work
    #
    #         time.sleep(5)
    #
    #         await editable.edit(content=f"\n```py\nExecuting...\n```")
    #
    #         # Sets the content box to the output of the file
    #         cont = None
    #         cont = "\n".join([str(x) for x in script.main()])
    #
    #         if cont != None:
    #             await editable.edit(content=f"\n```py\n{cont}\n```", view=view)
    #             return None
    #
    #         # If the
    #         await editable.edit(content=f"\n```py\nEXECUTION FAILED\nSYNTAX ERROR\n```")
    #
    #     else:
    #
    #         editable = await ctx.channel.send("Output:\n```py\nExecuting...\n```")
    #         await editable.edit(content=f"\n```py\nEXECUTION FAILED\n-----------------\n{valid[1]}\n```")

    # REPEAT- DRY be dammed

    # button.callback = button_callback

    await ctx.message.delete()
    message = await ctx.fetch_message(arg)
    valid = validity_query(message.content)

    if valid[0]:

        editable = await ctx.channel.send(f"**{arg}**\n```py\nRefactoring...\n```", view=blank)

        time.sleep(1)
        await editable.edit(content=f"**{arg}**\n```py\nCompiling...\n```")
        open('exece.py', 'w').close()
        with open("exece.py", "a") as f:
            f.write(refactor(message.content))
            f.close()

        # Time for the file to update and save for the hotreload to work

        time.sleep(5)

        await editable.edit(content=f"**{arg}**\n```py\nExecuting...\n```")

        # Sets the content box to the output of the file
        cont = None
        cont = "\n".join([str(x) for x in script.main()])

        if cont != None:
            await editable.edit(content=f"**{arg}**\n```py\n{cont}\n```", view=blank) # view)
            return None

        # If the
        await editable.edit(content=f"**{arg}**\n```py\nEXECUTION FAILED\nSYNTAX ERROR\n```")

    else:

        editable = await ctx.channel.send(f"**{arg}**\n```py\nExecuting...\n```")
        await editable.edit(content=f"**{arg}**\n```py\nEXECUTION FAILED\n-----------------\n{valid[1]}\n```")


@bot.command()
async def reruner(ctx):
    await ctx.message.delete()
    editable = await ctx.channel.send("Output:\n```py\nExecuting...\n```")
    cont = "\n".join([str(x) for x in script.main()])
    await editable.edit(content=f"Output:\n```py\n{cont}\n```")


@bot.command()
async def refact(ctx, arg):
    await ctx.message.delete()
    message = await ctx.fetch_message(arg)
    valid = validity_query(message.content)

    title = await ctx.channel.send(f"{arg}: ")
    editable = await ctx.channel.send("Output:\n```py\nRefactoring...\n```")

    time.sleep(1)

    if valid[0]:
        await editable.edit(content=f"Output:\n```py\n{refactor(message.content)}\n```")
    else:
        await editable.edit(content=f"\n```py\nEXECUTION FAILED\n-----------------\n{valid[1]}\n```")


bot.run(BOT_TOKEN)
