#pip install openai
# install dependencies for ai service providers Anthorpic and OpenAI 
#pip install anthropic openai
from dotenv import load_dotenv

from matplotlib import text
load_dotenv()

from anthropic import Anthropic
from openai import OpenAI

class ChatServer:
    messages = []
    def __init__(self):
        self.client = None
        self.model = None
        self.max_tokens = 0
        self.temperature = 1
        self.enable_streaming = False
        self.system_prompt = "You are a helpful assistant."
    
    def set_ai_proovider(self, ai_provider_name):
        if ai_provider_name not in ["Anthropic", "OpenAI"]:
            self.client = None
            raise ValueError("Invalid AI provider name. Please choose 'Anthropic' or 'OpenAI'.")
        if ai_provider_name == "Anthropic":
            self.client = Anthropic()
        if ai_provider_name == "OpenAI":
             self.client = OpenAI()

    def set_model_to_use(self, model_name):
        self.model = model_name

    def set_max_tokens(self, max_tokens):
        self.max_tokens = max_tokens

    def add_user_message(self, text):
        user_message = {"role": "user", "content": text}
        self.messages.append(user_message)

    def add_assistant_message(self, text):
        assistant_message = {"role": "assistant", "content": text}
        self.messages.append(assistant_message)

    def model_temperature(self, temperature):
        self.temperature = temperature

    def should_steam_response(self, enable_streaming):
        self.enable_streaming = enable_streaming

    def set_system_prompt(self, system_prompt):
        self.system_prompt = system_prompt

    def send_message(self):
        response = self.client.messages.create(
            model = self.model,
            max_tokens = 100,
            messages = self.messages,
            extra_body={"temperature": self.temperature}, ## Adjust the temperature for randomness
            system = self.system_prompt, ## You can customize the system prompt message to set the behavior of the assistant
            stream = self.enable_streaming ## Enable streaming for real-time responses
       )
        print(response)
        print(response.content)
        return response.content[0].text

