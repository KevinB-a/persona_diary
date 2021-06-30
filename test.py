import sys
sys.path.insert(0, "/home/apprenant/simplon_project/personal_diary/")

from view.clientview import ClientView
from view.messageview import MessageView

message = MessageView()
client = ClientView()

client.new_client() 
#message.new_message() 

#client.to_show_clients() 
#message.to_show_messages()

#client.to_update_client()
#message.to_update_message()