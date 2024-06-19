import asyncio
import config
import nextcord
from datetime import datetime, timezone
from nextcord.ext import commands


class Basic(commands.Cog):

  def __init__(self, bot):
    self.bot = bot





  #test command
  @commands.command()
  async def test(self, ctx):
    await ctx.send("its a test command nigga")







  #uSER joins WELCOME
  @commands.Cog.listener()
  async def on_member_join(self, member):
    guild = member.guild
    channel_id = config.WELCOME_CHANNEL_ID
    channel = guild.get_channel(channel_id)

    if channel:
      embed = nextcord.Embed(
          title="Hey there!",
          description=
          f"Welcome to {guild.name}, {member.mention} Enjoy your stay!",
          color=nextcord.Colour.green())

    if member.avatar:
      avatar_url = member.avatar.url
    else:
      avatar_url = member.default_avatar.url

    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Information",
                    value="Please consider exploring our server!",
                    inline=False)

    await channel.send(embed=embed)








  #goodbye
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    guild = member.guild
    channel_id = config.GOODBYE_CHANNEL_ID
    channel = guild.get_channel(channel_id)

    if channel:
      embed = nextcord.Embed(
          title="Goodbye!",
          description=f"Goodbye {member.mention} Thanks for yo visit!",
          color=nextcord.Colour.red())

    if member.avatar:
      avatar_url = member.avatar.url
    else:
      avatar_url = member.default_avatar.url

    embed.set_thumbnail(url=avatar_url)

    await channel.send(embed=embed)








  #Ping command
  @commands.command(description="Shows the current latency of the bot.")
  async def ping(self, ctx):
    latency = self.bot.latency * 1000

    embed = nextcord.Embed(
        title="Ping!",
        description=f"Current ping is of {latency: .2f}ms :>",
        color=nextcord.Color.orange())
    embed.set_thumbnail(url=ctx.author.avatar.url)

    await ctx.reply(embed=embed)



  
  



  
  #userInfo
  @commands.command(name="userinfo", description="Shows info of the user.")
  async def userinfo(self, ctx, member: nextcord.Member = None):
    member = member or ctx.author

    # utc = datetime.now().astimezone().tzinfo

    # ist_offset = timedelta(hours=5, minutes=30)

    # def convert_to_ist(time):
    #   return time + ist_offset

    # joined_at_utc = member.joined_at.astimezone(utc)
    # joined_at_ist = convert_to_ist(joined_at_utc)

    join_date = member.joined_at.strftime("%d-%m-%Y %H:%M:%S")
    current_time = datetime.now(timezone.utc)
    time_on_server = current_time - member.joined_at
    time_on_server_minutes = divmod(time_on_server.total_seconds(), 60)
    hours, minutes = divmod(time_on_server_minutes[0], 60)

    embed = nextcord.Embed(title="User Information",
                           color=nextcord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url)

    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=join_date, inline=False)
    embed.add_field(name="Time on Server",
                    value=f"{int(hours)} hours, {int(minutes)} minutes",
                    inline=False)

    await ctx.send(embed=embed)









  #Serverinfo command
  @commands.command(name='serverinfo', description="info of server")
  async def serverInfo(self, ctx):
    server_created_at = ctx.guild.created_at.strftime("%d-%M-%Y %H:%M")
    member_count = ctx.guild.member_count
    uptime = datetime.now(timezone.utc) - self.bot.user.created_at
    uptime_hours = uptime.seconds  #3600
    uptime_min = (uptime.seconds % 3600)

    embed = nextcord.Embed(title="Server's fuckin Info",
                           color=nextcord.Color.yellow())
    embed.set_thumbnail(url=self.bot.user.avatar.url)

    embed.add_field(name="Server created at: ",
                    value=server_created_at,
                    inline=False)
    embed.add_field(name="Member Count: ", value=member_count, inline=False)
    embed.add_field(name="Uptime: ",
                    value=f"{uptime_hours} hours {uptime_min} minutes",
                    inline=False)

    await ctx.send(embed=embed)


#ADD MORE FUNCTIONALITY ksjdfkjaskdj;jalkjdkfj;jaskldfj


def setup(bot):
  bot.add_cog(Basic(bot))
  print("cog has been loaded")
  print("----------------------")
