import disnake
class Icons:
    """
    Centralized icon registry for CipherX.
    Replace values with custom Discord emojis anytime
    without changing the rest of the project.
    """

    # =========================
    # Bot
    # =========================
    BOT = "<:bot:1528568856862396458>"

    # =========================
    # Status
    # =========================
    SUCCESS = "<a:verified_black2:1527768457192669344>"
    WARNING = "<:warning:1528084129986641981>"
    ERROR = "<a:wrong:1527770746137608473>"
    INFO = "<:info:1528798910301343804>"

    # =========================
    # Commands
    # =========================
    HELP = "<:question_mark:1528565507333034024>"
    SETUP = "<:gradient_tools:1528799592554958949>"
    SETTINGS = "<a:gear1:1528799498866921523>"
    PERMISSION = "<:verified_shield:1527768677523394590>"
    ROTATE = "<:rotate:1528807352223141919>"
    ENCRYPT = "<:locked:1527772559754399744>"
    DECRYPT = "<:unlock:1528086339533144214>"

    KEY = "<:key:1528086792925089863>"
    FILE = "<:file:1528088067280212131>"

    FAQ = "<:faq:1527772431056507112>"

    # =========================
    # UI
    # =========================
    ARROW = "<a:red:1527765129163313332>"
    HOME = "<:home:1528565559871017091>"
    BACK = "<a:left_arrow:1527769630179987688>"
    NEXT = "<a:right_arrow:1527769628573700157>"

    # =========================
    # Misc
    # =========================
    VERSION = "<:owner:1528566387671437433>"
    SERVER = "<:global:1528087825860395179>"
    USER = "<:id:1528799792426389606>"
    @staticmethod
    def emoji(icon: str):
     return disnake.PartialEmoji.from_str(icon)