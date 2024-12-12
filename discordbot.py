# Imports
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import token, apikey

# Bot Configuration
intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='/')

#Sync
@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Bot is running and has synced.')

# Establish Command Name and Description 
@bot.tree.command(name='ip_lookup', description='Provides High Level Information about an IP Address')

# Bot Prompt, API Call, and Response Functionality
@app_commands.describe(user_input = "Please Enter an IP Address: ")                 # Prompt User for Input
async def ip lookup(interaction: discord.Interaction, user_input: str):                 

    # Use Requests to Obtain Data from API
    url =f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={user_input}'
    response = requests.get(url)
    json_response = response.json()

    # Send Message Containing Requested Data to User
    await interaction.response.send_message(f'IP: {json_Response["ip"]\nCountry:{json_response["country_name"]}\nISP: {jsone_response["isp"]}', ephemeral=True)
    return

bot.run(token) # Run Bot
