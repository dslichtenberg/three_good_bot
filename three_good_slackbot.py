import time, sys, re
import slack

import config_file as cfg

from absl import flags



def sendDMtoAllUsers(customer_name, message):
  slackclient= slack.WebClient(token =  customer_codes[customer_name])
  members = slackclient.users_list()['members']
  for member in members:
    name = member['name']
    if not member['is_bot']:
      conversation_id = slackclient.conversations_open(users=  member['id'])
      slackclient.chat_postMessage(  
        channel = conversation_id['channel']['id'], 
        text = f':potable_water::potable_water:Hi, {name}! {message}:potable_water::potable_water:'
      )
  return f'Sent message "{message}" to users: {[member["name"] for member in members]} at client {customer_name}'


flags.DEFINE_string('config_file', None, 'location of the config xlsx file.')
FLAGS = flags.FLAGS
FLAGS(sys.argv)

def main():
  customer_codes ,msg_queue = cfg.read_config()

  for i in range(msg_queue.message.count()):
    if(msg_queue.sent[i] != True): 
      print(sendDMtoAllUsers(msg_queue.client_to[i].strip(), msg_queue.message[i].strip()))
      #cfg.update_messaging_status()

if __name__ == '__main__':
  main()
