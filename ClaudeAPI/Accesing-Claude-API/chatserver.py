from dotenv import load_dotenv
from matplotlib import text
load_dotenv()

from anthropic import Anthropic

class ChatServer:
    messages = []
    def __init__(self):
        self.client = Anthropic()
        self.model = "claude-sonnet-5-5"

    def add_user_message(self, text):
        user_message = {"role": "user", "content": text}
        self.messages.append(user_message)

    def add_assistant_message(self, text):
        assistant_message = {"role": "assistant", "content": text}
        self.messages.append(assistant_message)


    def send_message(self):
        response = self.client.messages.create(
            model=self.model,
            max_tokens=100,
            messages= self.messages 
       )
        print(response)
        print(response.content)
        return response.content[0].text

