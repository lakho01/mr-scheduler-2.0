from email.mime import image
from turtle import back, title
from discord.ext import commands
import discord
from discord import app_commands
import interactions
from datetime import date
from discord.ui import Button, View


bot = interactions.Client(
    token=""
)

#----------------------------Start of CWs------------------------------------------ 

Week1S = ("COMP23111 SWE1 Basic Git IndCwk1")
Week1F = ("")

Week2S = ("COMP21111 L&M Propositional Logic")
Week2F = ("")

Week3S = ("COMP21111 L&M Satisfiability \nCOMP23111 SWE1 Conflicts in Git IndCwk2")
Week3F = ("")

Week4S = ("COMP21111 L&M Propositional Formalisations \nCOMP26020 PLP Lab1 Matrix Multiplication in C \nCOMP22111 PM Lab1 ALU \nCOMP23111 DS Database Design")
Week4F = ("")

Week5S = ("COMP21111 L&M DPLL/Random Formulas \nCOMP26120 A&DS Recursive Complexity \nCOMP23311 SWE1 Fixing Bugs TeamCwk1")
Week5F = ("")

Week6S = ("COMP24011 AI Games")
Week6F = ("")

Week7S = ("COMP21111 L&M Randomized Algorithms/Tableaux \nCOMP26020 PLP Lab2 Library Management in C++")
Week7F = ("")

Week8S = ("COMP21111 L&M BDT/BDDs/OBDDs")
Week8F = ("")

Week9S = ("COMP21111 L&M QBF Basics \nCOMP26120 A&DS Spell Checking Data Structures \nCOMP22111 PM Lab3 FSM")
Week9F = ("")

Week10S = ("COMP21111 L&M QBF Algorithms \nCOMP23111 DS Advanced Databases \nCOMP23311 SWE1 Adding Features TeamCwk2")
Week10F = ("")

Week11S = ("COMP21111 L&M PLDF / State Transition Systems \nCOMP26020 PLP Haskell \nCOMP24011 AI SLAM")
Week11F = ("")

Week12S = ("COMP21111 L&M LTL \nCOMP22111 PM Control Implementation \nCOMP22111 PM Signal Using Charts")
Week12F = ("")
#----------------------------------------End of stupid section------------------------------------------
course_abb = "SWE1: Software Engineering 1 \nL&M: Logic & Modelling \nPLP: Programming Languages & Paradigms \nA&DS: Algorithms & Data Structures \nPM: Processor Microarchitecture \nDS: Database Systems \nAI: Introduction to AI"


Dates = {
    1 : "26 September - 30 September",
    2 : "03 October - 07 October",
    3 : "10 October - 14 October",
    4 : "17 October - 21 October",
    5 : "24 October - 28 October",
    6 : "31 October - 4 November",
    7 : "07 November - 11 November",
    8 : "14 November - 18 November",
    9 : "21 November - 25 November",
    10 : "28 November - 02 December",
    11 : "05 December - 09 December",
    12 : "12 December - 16 December"
}

Summatives = {
    1 : "No tasks",
    2 : "COMP21111 L&M Propositional Logic \nCOMP23111 SWE1 Basic Git IndCwk1",
    3 : "COMP21111 L&M Satisfiability",
    4 : "COMP21111 L&M Propositional Formalisations \nCOMP23111 SWE1 Conflicts in Git IndCwk2 \nCOMP26020 PLP Lab1 Matrix Multiplication in C \nCOMP22111 PM Lab1 ALU \nCOMP23111 DS Database Design",
    5 : "COMP21111 L&M DPLL/Random Formulas \nCOMP26120 A&DS Recursive Complexity \nCOMP23311 SWE1 Fixing Bugs TeamCwk1",
    6 : "COMP24011 AI Games",
    7 : "COMP21111 L&M Randomized Algorithms/Tableaux",
    8 : "COMP21111 L&M BDT/BDDs/OBDDs",
    9 : "COMP21111 L&M QBF Basics \nCOMP22111 PM Lab3 FSM",
    10 : "COMP21111 L&M QBF Algorithms \nCOMP23111 DS Implementation \nCOMP24011 AI Fuzzy Logic \nCOMP26020 PLP Lab2 C++",
    11 : "COMP21111 L&M PLDF / State Transition Systems \nCOMP26120 A&DS Spell Checking Data Structures \nCOMP23311 SWE1 Adding Features TeamCwk2",
    12 : "COMP21111 L&M LTL \nCOMP22111 PM Control Implementation \nCOMP22111 PM Signal Using Charts \nCOMP24011 AI SLAM"
}

Formatives = {
    1 : "No tasks",
    2 : "COMP26120 A&DS Analysing Algorithms",
    3 : "COMP26120 A&DS Introducing Complexity Analysis",
    4 : "COMP26120 A&DS Spellchecking 1",
    5 : "No tasks",
    6 : "No tasks",
    7 : "No tasks",
    8 : "COMP26120 A&DS Spellchecking 2",
    9 : "No tasks",
    10 : "No tasks",
    11 : "No tasks",
    12 : "COMP26120 A&DS Priority Queues"
}


#----------------------------End of CWs--------------------------------------

#-------------------Start of initialising next and back buttons---------------------

# next_button = interactions.Button(
#     style=interactions.ButtonStyle.DANGER,
#     # color = "grey",
#     label="Next",
#     custom_id="next",
#     disabled = False
# )

# next_button_disabled = interactions.Button(
#     style=interactions.ButtonStyle.PRIMARY,
#     label="Next",
#     custom_id="next1",
#     disabled = True
# )


# back_button = interactions.Button(
#     style=interactions.ButtonStyle.PRIMARY,
#     label = "Back",
#     custom_id="back"
# )

# row = interactions.ActionRow(
#     components=[back_button, next_button]
# )


#-------------------End of initialising next and back buttons---------------------
my_id = "<@467264405097283594>"
dan_id = "<@455501686023389186>"
hsdg_id = "<@325213623091986434>"
help_desc = "Note: The bot is currently being developed, any suggestions please DM: "
comb_ali_dan = my_id +"\n" + dan_id
data_link = "https://docs.google.com/spreadsheets/d/11XvSfBHq-kSYZquztFrkjaJJpn6OxDu1uPAkBn-Cie0/edit#gid=1202261217"

data_page = interactions.Button(
    style=interactions.ButtonStyle.LINK,
    label="Data Taken From",
    # custom_id="data",
    url = data_link,
    disabled = False
)

@bot.command(
    name = "help",
    description = "View help"
)

async def help(ctx: interactions.CommandContext):
    embeds_help = interactions.Embed(
        title="Mr. Scheduler v2.0",
        description=help_desc+str(my_id)+" or "+str(dan_id),
        color=0x00ff00
        )
    embeds_help.add_field(name="Developed by", value=comb_ali_dan, inline=False)
    embeds_help.add_field(name="Tested by", value=hsdg_id, inline=False)
    embeds_help.add_field(name="Course Abbreviations", value=course_abb, inline=False)
    await ctx.send(embeds = embeds_help, components = data_page)

global WEEK_NUM


@bot.command(
    name="week_choose",
    description="Choose a week number",
    options = [
        interactions.Option(
            name="week_number",
            description="Choose a week number from 1 - 12",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)



async def week_choose(ctx: interactions.CommandContext, week_number: int):
    # global msg
    if (week_number>12) or (week_number<1):
        await ctx.send(":x: Choose between 1 - 12")
    else:

        global WEEK_NUM
        WEEK_NUM = week_number
        embeds = interactions.Embed(
        title=f"Deadlines for Week {week_number}",
        description=Dates[week_number],
        color=0x00ff00
        )
        embeds.add_field(name="Summatives:", value=Summatives[week_number], inline=False)
        embeds.add_field(name="Formatives:", value=Formatives[week_number], inline=False)
        # msg = await ctx.send(embeds = embeds, components = next_button)
        if (week_number == 6):
            embeds.title = (embeds.title+"\nReading Week")
            embeds.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        # if (week_number == 1):
        #     # await ctx.send(embeds = embeds, components = next_button)
        #     await ctx.send(embeds = embeds)
        # if (week_number==12):
        #     await ctx.send(embeds = embeds)
        # if (week_number>1) and (week_number<12):
        #     await ctx.send(embeds = embeds)
        await ctx.send(embeds = embeds)




    @bot.component("next")
    async def button_response(ctx):
        # await msg.delete()
        # await ctx.send(embeds = embeds, components = next_button_disabled)
        global WEEK_NUM
        forward = WEEK_NUM
        WEEK_NUM += 1
        forward = forward + 1
        embeds1 = interactions.Embed(
        title=f"Deadlines for Week {forward}",
        description=Dates[forward],
        color=0x00ff00
        )
        embeds1.add_field(name="Summatives:", value=Summatives[forward], inline=False)
        if (forward == 6):
            embeds1.title = (embeds1.title+"\nReading Week")
            embeds1.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        await ctx.send(embeds = embeds1, ephemeral=False)
        # next_button.disabled = True
        # await ctx.send(embeds = embeds1, ephemeral=False, components=next_button)
    

    @bot.component("back")
    async def button_response(ctx):
        # await msg.delete()
        backward = WEEK_NUM
        backward = backward - 1
        embeds0 = interactions.Embed(
        title=f"Deadlines for Week {backward}",
        description=Dates[backward],
        color=0x00ff00
        )
        embeds0.add_field(name="Summatives:", value=Summatives[backward], inline=False)
        if (backward == 6):
            embeds0.title = (embeds0.title+"\nReading Week")
            embeds0.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
        await ctx.send(embeds = embeds0, ephemeral=False)


bot.start()

#---------------------------------------------End of code----------------------------------------------------














#---------------------------------Archived code blocks start---------------------------------------


# button = interactions.Button(
#     style=interactions.ButtonStyle.PRIMARY,
#     label="🡺",
#     # label2 = "🡸",
#     custom_id="hello"
# )

# @bot.command(
#     name="button_test",
#     description="This is the first command I made!"
#     # scope=the_id_of_your_guild,
# )
# async def button_test(ctx):
#     await ctx.send("testing", components=button)

# @bot.component("hello")
# async def button_response(ctx):
#     await ctx.send("You clicked the Button :O", ephemeral=True)





# @bot.command(
#     name="week1",
#     description="Tasks in Week 1",
# )
# async def week1(ctx: interactions.CommandContext):
#     embedVar = discord.Embed(title="Deadlines for Week 1", description="26 September - 30 September", color=0x00ff00)
#     await ctx.send(embedVar = embedVar)

# @bot.command(
#     name="test",
#     description="Tasks in Week 1"
# )
# async def test(ctx: interactions.Embed):
#     embed = interactions.Embed(
#         title="testing",
#         description="test purposes"
#     )
#     await ctx.channel.send(embed = embed)

# @bot.command(
#     name="test",
#     description="Tasks in Week 1"
#     )
# async def test(ctx):
#     embeds=interactions.Embed(
#         title="Sample Embed",
#         description="",
#         color=0xFF5733
#         )
#     await ctx.send(embeds=embeds)





# @bot.command(
#     name="embed",
#     description="Test"
# )
# async def embed(ctx: interactions.Embed):
#     embeds = interactions.Embed(
#         title="your title",
#         description="your description",
#     )
#     # embed = discord.Embed(
#     #     title="your title",
#     #     description="your description",
#     #     color=0x00ff00
#     #     )
#     await ctx.channel.send(embeds)




# -------------------------Button--------------------------------
# button = interactions.Button(
#     style=interactions.ButtonStyle.PRIMARY,
#     label="hello world!",
#     custom_id="hello"
# )

# @bot.command(
#     name="button_test",
#     description="This is the first command I made!"
#     # scope=the_id_of_your_guild,
# )
# async def button_test(ctx):
#     await ctx.send("testing", components=button)

# @bot.component("hello")
# async def button_response(ctx):
#     await ctx.send("You clicked the Button :O", ephemeral=True)
# ----------------------End of Button------------------------------

# ----------------------Nested Commands------------------------------
# @bot.command(
#     name="base_command",
#     description="This description isn't seen in UI (yet?)",
#     # scope=guild_id,
#     options=[
#         interactions.Option(
#             name="command_name",
#             description="A descriptive description",
#             type=interactions.OptionType.SUB_COMMAND,
#             options=[
#                 interactions.Option(
#                     name="option",
#                     description="A descriptive description",
#                     type=interactions.OptionType.INTEGER,
#                     required=False,
#                 ),
#             ],
#         ),
#         interactions.Option(
#             name="second_command",
#             description="A descriptive description",
#             type=interactions.OptionType.SUB_COMMAND,
#             options=[
#                 interactions.Option(
#                     name="second_option",
#                     description="A descriptive description",
#                     type=interactions.OptionType.STRING,
#                     required=True,
#                 ),
#             ],
#         ),
#     ],
# )
# async def cmd(ctx: interactions.CommandContext, sub_command: str, second_option: str = "", option: int = None):
#     if sub_command == "command_name":
#         await ctx.send(f"You selected the command_name sub command and put in {option}")
#     elif sub_command == "second_command":
#         await ctx.send(f"You selected the second_command sub command and put in {second_option}")
# -----------------------------End of Nested Commands-----------------------------------

#------------------------------Archived---------------------------------------------
# @bot.command(
#     name="week1",
#     description="Tasks for Week 1"
# )
# async def week1(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 1",
#         description="26 September - 30 September",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week1S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week2",
#     description="Tasks for Week 2"
# )
# async def week2(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 2",
#         description="03 October - 07 October",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week2S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week3",
#     description="Tasks for Week 3"
# )
# async def week3(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 3",
#         description="10 October - 14 October",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week3S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week4",
#     description="Tasks for Week 4"
# )
# async def week4(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 4",
#         description="17 October - 21 October",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week4S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week5",
#     description="Tasks for Week 5"
# )
# async def week5(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 5",
#         description="24 October - 28 October",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week5S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week6",
#     description="Tasks for Week 6"
# )
# async def week6(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 6 \nReading Week",
#         description="31 October - 4 November",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week6S, inline=False)
#     embeds.set_thumbnail(url = "https://i.pinimg.com/originals/66/8a/8c/668a8cccacc792924fa588b4adca8f68.gif")
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week7",
#     description="Tasks for Week 7"
# )
# async def week7(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 7",
#         description="07 November - 11 November",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week7S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week8",
#     description="Tasks for Week 8"
# )
# async def week8(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 8",
#         description="14 November - 18 November",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week8S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week9",
#     description="Tasks for Week 9"
# )
# async def week9(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 9",
#         description="21 November - 25 November",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week9S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week10",
#     description="Tasks for Week 10"
# )
# async def week10(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 10",
#         description="28 November - 02 December",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week10S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week11",
#     description="Tasks for Week 11"
# )
# async def week11(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 11",
#         description="05 December - 09 December",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week11S, inline=False)
#     await ctx.send(embeds = embeds)

# @bot.command(
#     name="week12",
#     description="Tasks for Week 11"
# )
# async def week12(ctx: interactions.CommandContext):
#     embeds = interactions.Embed(
#         title="Deadlines for Week 12",
#         description="12 December - 16 December",
#         color=0x00ff00
#     )
#     embeds.add_field(name="Summatives:", value=Week12S, inline=False)
#     await ctx.send(embeds = embeds)

#-----------------------End of Archive----------------------------------