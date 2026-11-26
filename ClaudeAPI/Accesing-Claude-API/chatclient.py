
from chatserver import ChatServer

# class chatclient:
#     chatserver = None
#     def __init__(self):
#         self.chatserver = ChatServer()

#     def send_user_message(self, user_message):
#         self.server.add_user_message(user_message)
#         response = self.server.send_message()
#         assistant_message = response['completion']
#         self.server.add_assistant_message(assistant_message)
#         return assistant_message


chat_server = ChatServer()
chat_server.set_ai_proovider("Anthropic")  # Set the AI provider to Anthropic
chat_server.set_model_to_use("claude-sonnet-5-5")  # Set the model to use    
chat_server.set_max_tokens(100)  # Set the maximum number of tokens to generate
chat_server.model_temperature(0.7)  # Set the temperature for randomness
chat_server.should_steam_response(True)  # Enable streaming for real-time responses 
 # Set the system prompt for the assistant


chat_server.add_user_message("Hello, what is the capital of France?")
answer = chat_server.send_message()
print(answer)
chat_server.add_assistant_message(answer)

chat_server.add_user_message("Tell me a more about it in one sentence.")
answer = chat_server.send_message()
print(answer)