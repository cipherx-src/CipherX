class FAQService:
    
    @staticmethod
    def get_questions():
        return [
            {
                "question": "How do I encrypt a file?",
                "answer": "<a:green:1527765266501734521> Use /encrypt and upload a file."
            },
            {
                "question": "How do I decrypt a file?",
                "answer": "<a:green:1527765266501734521> Use /decrypt with the correct encryption key."
            },
            {
                "question": "Where are encryption keys stored?",
                "answer": "<a:green:1527765266501734521> The keys are stored confidentially."
            },
            {
                "question": "How do I configure CipherX?",
                "answer": "<a:green:1527765266501734521> Run /setup to configure the bot."
            },
        ]