# DiscordPyInterpreter
Takes in python code using discord code embeds, validates it, then reformats to return the data within print statements. This data is then outputed in the discord channel that the request was made in.

# Modules

~ HotReload

~ Discord.py

~ Logging

~ Time

# Algorithm Explanations

Waits for a discord code embed in .py format, then reformats the code to have it append to an array instead of output. This reformated code is written into a function, hot reloaded then ran. The output of this is then returned in the previous discord channel.
