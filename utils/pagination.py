import discord
from typing import List

class Pagination(discord.ui.View):
    
    def __init__(self, author: discord.User, pages: List[discord.SelectOption], embeded: bool,error_message: str="Your don't have permission to use this menu"):
        """
        Create your best pagination menu with this

        ### Arguments:
        author = discord.User
        pages = List of message / embed
        embeded = boolean
        error_message = if author != user then error_message
        ### Example:
        author = discord.User\n
        embeds = []\n
        embed = discord.Embed()...\n
        embeds.append(embed)\n
        view=Pagination(author, pages=embeds, embeded=True)
        """
        super().__init__()
        self.author = author
        self.pages = pages
        self.embeded = embeded
        self.error_message = error_message

        self.current_page = 0
    # Check if the user is the author
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.author:
            return True
        else:
            if isinstance(self.error_message, discord.Embed):
                await interaction.response.send_message(embed=self.error_message, ephemeral=True)
            else:
                await interaction.response.send_message(self.error_message, ephemeral=True)
    # Update the children
    async def update_children(self, interaction: discord.Interaction):
        # check if the next page is the end
        self.next.disabled = (self.current_page + 1 == len(self.pages))
        # check if the previous page is the start
        self.previous.disabled = (self.current_page <= 0)

        # setup message with embed
        kwargs = {'content': self.pages[self.current_page]} if not (self.embeded) else {'embed': self.pages[self.current_page]}
        # setup view
        kwargs['view'] = self
        # update message
        await interaction.response.edit_message(**kwargs)

    # Buttons
    @discord.ui.button(label="◀", style=discord.ButtonStyle.blurple, row=1)
    async def previous(self, button: discord.ui.Button, interaction: discord.Interaction):
        # sub 1 to current page
        self.current_page -= 1
        # update message
        await self.update_children(interaction)

    @discord.ui.button(label="▶", style=discord.ButtonStyle.blurple, row=1)
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        # add 1 to current page
        self.current_page += 1
        # update message
        await self.update_children(interaction)