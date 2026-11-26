
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
chat_server.add_user_message("Hello, what is the capital of France?")
answer = chat_server.send_message()
print(answer)
chat_server.add_assistant_message(answer)

chat_server.add_user_message("Tell me a more about it in one sentence.")
answer = chat_server.send_message()
print(answer)