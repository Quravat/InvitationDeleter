import discord
import time

DISCORD_TOKEN = ""  # token for your bot
SERVER_ID = 12345679  # server id

class InviteCleanerBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        guild = self.get_guild(SERVER_ID)
        if guild is None:
            print(f"The server with ID {SERVER_ID} cannot be found.")
            return

        invitations = await guild.invites()
        if not invitations:
            print("No invitations to delete.")
            return

        print(f"Deleting {len(invitations)} invitations...")
        for invite in invitations:
            time.sleep(1)
            try:
                await invite.delete()
                print(f"The invitation with code {invite.code} has been removed.")
            except discord.HTTPException as e:
                print(f"Unable to delete invitation {invite.code}: {e}")

        print("All invitations have been deleted.")

bot = InviteCleanerBot(intents=discord.Intents.all())
bot.run(DISCORD_TOKEN)
