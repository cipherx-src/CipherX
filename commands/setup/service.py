from commands.key.service import KeyService


class SetupService:
    """Business logic for the setup dashboard."""

    @staticmethod
    def get_status(guild_id: int) -> dict:

        return {
            "permission": True,
            "settings": True,
            "key": KeyService.has_key(guild_id),
        }