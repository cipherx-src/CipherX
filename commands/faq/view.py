
import disnake


class FAQView(disnake.ui.View):
    
    def __init__(self):
        super().__init__(timeout=300)