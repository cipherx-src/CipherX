from assets.embeds import EmbedFactory
from assets.icons import Icons


class FAQUI:

    @staticmethod
    def create_dashboard(faqs: list[dict]):
        embed = EmbedFactory.primary(
            title=f"{Icons.FAQ} CipherX FAQ",
            description="Frequently asked questions about CipherX.",
        )

        for faq in faqs:
            embed.add_field(
                name=f"<:question_mark:1528565507333034024> {faq['question']}",
                value=faq["answer"],
                inline=False,
            )

        return embed