import discord
from datetime import datetime

class Invite():
    # Create a docstring for class
    """Class to manage invites.
    Track invitations
    """
    def __init__(self, bot) -> None:
        """
        Initialize the Invite class.

        Parameters:
        bot (discord.Client): The Discord bot client.

        Attributes:
        _invite_cache (dict): A dictionary to store cached invites.
        """
        self.bot = bot
        self._invite_cache = {}
        self.add_listeners()

    def add_listeners(self):
        """
        Add event listeners for various Discord events to manage invites.
        """
        self.bot.add_listener(self.cache_invites, "on_ready")
        self.bot.add_listener(self.update_invites_cache, "on_invite_create")
        self.bot.add_listener(self.remove_invites_cache, "on_invite_delete")
        self.bot.add_listener(self.add_cache_guild, "on_guild_join")
        self.bot.add_listener(self.remove_cache_guild, "on_guild_remove")

    async def add_cache_guild(self, guild):
        """
        Add a guild to the invite cache.

        Parameters:
        guild (discord.Guild): The guild to add to the cache.
        """
        self._invite_cache[guild.id] = {}
        for invite in await guild.invites():
            self._invite_cache[guild.id][invite.code] = invite

    async def remove_cache_guild(self, guild):
        """
        Remove a guild from the invite cache.

        Parameters:
        guild (discord.Guild): The guild to remove from the cache.
        """
        self._invite_cache.pop(guild.id)

    async def cache_invites(self):
        """
        Cache invites for all guilds the bot is in.
        """
        for guild in self.bot.guilds:
            try:
                self._invite_cache[guild.id] = {}
                for invite in await guild.invites():
                    self._invite_cache[guild.id][invite.code] = invite
            except:
                return

    async def remove_invites_cache(self, invite):
        """
        Remove an invite from the cache if conditions are met.

        Parameters:
        invite (discord.Invite): The invite to potentially remove from the cache.
        """
        if invite.guild.id not in self._invite_cache.keys():
            return
        ref_invite = self._invite_cache[invite.guild.id][invite.code]
        if (ref_invite.created_at.timestamp()+ref_invite.max_age > datetime.now().timestamp() or ref_invite.max_age == 0) and ref_invite.max_uses > 0 and ref_invite.uses == ref_invite.max_uses-1:
            try:
                async for entry in invite.guild.audit_logs(limit=1, action=discord.AuditLogAction.invite_delete):
                    if entry.target.code != invite.code:
                        self._invite_cache[invite.guild.id][ref_invite.code].revoked = True
                        return
                    else:
                        self._invite_cache[invite.guild.id][ref_invite.code].revoked = True
                        return
            except:
                self._invite_cache[invite.guild.id][ref_invite.code].revoked = True
                return

    async def update_invites_cache(self, invite):
        """
        Update the invite cache with a new or updated invite.

        Parameters:
        invite (discord.Invite): The invite to update in the cache.
        """
        if invite.guild.id not in self._invite_cache.keys():
            return
        self._invite_cache[invite.guild.id][invite.code] = invite

    async def fetch_invite(self, member):
        """
        Fetch an invite for a member and update the cache accordingly.

        Parameters:
        member (discord.Member): The member for whom to fetch the invite.
        """
        for new_invite in await member.guild.invites():
            for cached_invite in self._invite_cache[member.guild.id].values():
                if new_invite.code == cached_invite.code and new_invite.uses - cached_invite.uses == 1 or cached_invite.revoked:
                    if cached_invite.revoked:
                        self._invite_cache[member.guild.id].pop(cached_invite.code)
                    elif new_invite.inviter == cached_invite.inviter:
                        self._invite_cache[member.guild.id][cached_invite.code] = new_invite
                    else:
                        self._invite_cache[member.guild.id][cached_invite.code].uses += 1
                    return cached_invite