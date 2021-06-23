import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from view.clientview import ClientView
from view.messageview import MessageView

message = MessageView()
client = ClientView()

#client.new_client()
#message.new_message()

#message.to_show_messages()
client.to_show_clients()