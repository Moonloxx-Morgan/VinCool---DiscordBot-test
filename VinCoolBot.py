import discord
from discord import app_commands
from discord.ext import commands
import os


intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "!", intents = intents)
slash = SlashCommand(bot, sync_commands = True)
bot.remove_command('help')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True




    

@slash.slash(name="Help", guild_ids=[1150472714260320416],  description="Voir Les Commandes du bot") 
async def lancer(ctx):
    await ctx.send("test")

# Start ###########################################################################################################
@bot.event
async def on_ready():
    print(f"{bot.user.name} bot open")
    activity = discord.Game(name="VinCool", type=3)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VinCool Bot-Vinted💰"))
    
    try:
        synced = await bot.tree.sync()
        
        
    
    
    
#Commmande Help #####################################################################################################
@bot.command()
async def help(ctx):
    await ctx.message.delete()#suprime l'appel
    '''Envoie la liste des commandes et leurs fonctions par message privé'''
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='Liste des commandes')

    #Commandes User ###################################################################################################
    embed.add_field(name="**!help**", value="Regardez toute les commandes possible", inline=False)
    embed.add_field(name="**!clear**", value="Supprimer Un nombre de message(!clear (nombre))", inline=False)
    embed.add_field(name="**!vinted**", value="Ajoutez le bot sur un salon", inline=False)
    embed.add_field(name="**!join**", value="Faire rejoindre le bot sur son salon vocal", inline=False)
    embed.add_field(name="**!autobuy**", value="Pour Setup L'autoBuy", inline=False)
    #Commandes Admin ###################################################################################################
    for role in ctx.message.author.roles:
        if role.name == 'ଘ･🍓﹕Owner﹕₊˚⊹':
            embed.add_field(name="**!load [extension]**", value="Charge l'extension mentionnée", inline=False)
            embed.add_field(name="**!unload [extension]**", value="Désactive l'extension mentionnée", inline=False)
            embed.add_field(name="**!reload [extension]**", value="Recharge l'extension mentionnée", inline=False)
    
    await ctx.author.send(embed=embed)
    


# Commande Join-Vocal #####################################################################################################
@bot.command()
async def rejoindre(ctx):
    await ctx.message.delete()#suprime l'appel
    # Vérifie si l'auteur de la commande est dans un canal vocal #####################################################################################################
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        # Rejoint le canal vocal de l'auteur de la commande #####################################################################################################
        await channel.connect()
        # Envoie un message pour confirmer que le bot a rejoint le canal vocal #####################################################################################################
        await ctx.send('Je viens de rejoindre le canal vocal!')
    else:
        # Si l'auteur de la commande n'est pas dans un canal vocal, envoie un message d'erreur #####################################################################################################
        await ctx.send('Vous devez d\'abord rejoindre un canal vocal!')
 
 

# Commande Join Voc #####################################################################################################

@bot.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await bot.join_voice_channel(channel)
 
#Commande Clear Message  #####################################################################################################

@bot.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)  
        await ctx.send(f'{amount} messages ont été **supprimés** par {ctx.author.mention}', delete_after=5)  
    else:
        await ctx.send("Vous n'avez pas la permission de gérer les messages.")
        
        
        
        
        

# Commande Purge #####################################################################################################

@bot.command()
async def purge(ctx, nombre: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=nombre)
        embed = discord.Embed(
            title="Messages supprimés",
            description=f"{nombre} messages ont été supprimés.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Erreur!",
            description="◼ Vous n'avez pas la permission de gérer les messages.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        
        

# Run Bot #####################################################################################################





bot.run('MTE2MTM0MjkzNDU4MzYxOTY5NQ.GoihUa.Zmek2mPZT8aut3_91deFaWMQQgp3NUp9-3tZ_8')
