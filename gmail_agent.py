from typing import Optional, Generator
from vocode.streaming.user_implemented_agent.base_agent import BaseAgent
from gmail_api import GmailAPI

class GmailAgent(BaseAgent):
    
    # Build Gmail API
    def __init__(self):
        self.gmail_api = GmailAPI()

    # is_interrupt is True when the human has just interrupted the bot's last response
    def respond(
        self, human_input, is_interrupt: bool = False
    ) -> tuple[Optional[str], bool]:
        # Read the last email if requested
        if "read email" in human_input:
            # Get email contents
            sender, subject, body = self.gmail_api.get_last_unread_message()
            # Return email info
            return f"email from {sender}. subject is {subject}. {body}", False
        # Else don't respond
        return None, False

    def generate_response(
        self, human_input, is_interrupt: bool = False
    ) -> Generator[str, None, None]:
        """Returns a generator that yields the agent's response one sentence at a time."""
        pass

    def update_last_bot_message_on_cut_off(self, message: str):
        """Updates the last bot message in the agent's state when the human cuts off the bot's response."""
        return ""