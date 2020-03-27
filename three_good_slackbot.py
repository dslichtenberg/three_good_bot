import time, sys, re
import slack
import math
import config_file as cfg
import numpy as np
from absl import flags



def sendDMtoUser(customer_codes,user_name, customer_name, message):
  slackclient= slack.WebClient(token =  customer_codes[customer_name])
  members = slackclient.users_list()['members']
  
  for member in members:
    if member['name'] == user_name:
      
      conversation_id = slackclient.conversations_open(users=  member['id'])
      slackclient.chat_postMessage(  
        channel = conversation_id['channel']['id'] ,
        text = f':potable_water::potable_water:Hi, {user_name}!:potable_water::potable_water:\n {message} '
      )
      #slackclient.files_upload (channel = conversation_id['channel']['id'], 
      #  file  =   './content/geckoboard_snap.png',
      #  title = "today's 3 good stats")
      #slackclient.files_sharedPublicURL(id =  conversation_id['channel']['id'] )
  return f'Sent message "{message}" to users: {[member["name"]  for member in members if member["name"] == user_name]} at client {customer_name}'

def sendDMtoAllUsers(customer_codes,customer_name, message):
  slackclient= slack.WebClient(token =  customer_codes[customer_name])
  members = slackclient.users_list()['members']
  for member in members:
    name = member['name']
    if not member['is_bot']:
      conversation_id = slackclient.conversations_open(users=  member['id'])
      slackclient.chat_postMessage(  
        channel = conversation_id['channel']['id'], 
        text = f':potable_water::potable_water:Hi, {name}! {message} :potable_water::potable_water:'
      )
  return f'Sent message "{message}" to users: {[member["name"] for member in members]} at client {customer_name}'


flags.DEFINE_string('config_file', None, 'location of the config xlsx file.')
FLAGS = flags.FLAGS
FLAGS(sys.argv)

def main():
  customer_codes ,msg_queue = cfg.read_config()
  msg_queue = msg_queue.replace(np.nan, '', regex=True)

  for i in range(msg_queue.message.count()):
    if(msg_queue.sent[i] != True): 
      if(msg_queue.user[i] == ''):
        print(sendDMtoAllUsers(customer_codes, msg_queue.client_to[i].strip(), msg_queue.message[i].strip()))
      else:
        print(sendDMtoUser(customer_codes,msg_queue.user[i].strip(), msg_queue.client_to[i].strip(), msg_queue.message[i].strip()))
      #
      cfg.update_messaging_status()

if __name__ == '__main__':
  main()
