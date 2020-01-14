import os.path
import json
import datetime
import slack  
import time, sys
from slack import RTMClient
from absl import flags


import config_file as cfg


@RTMClient.run_on(event="message")
def logMessage(**payload):
  data = payload['data']
  logfile = f'log-{datetime.datetime.now().strftime("%Y%m%d")}.csv'
  if not os.path.exists(logfile):
    with open(logfile, 'a') as file:
      file.write('text,user,team,user_team,source_team,channel,event_ts,ts\n')

  with open(logfile, 'a') as file:
    message = f"{data['text']}, {data['user']}, {data['team']}, {data['user_team']},{data['source_team']}, {data['channel']}, {data['event_ts']}, {data['ts']}\n"
    file.write(message)


flags.DEFINE_string('config_file', None, 'location of the config xlsx file.')
flags.DEFINE_string('customer', None, 'location of the config xlsx file.')
FLAGS = flags.FLAGS
FLAGS(sys.argv)

def main():
  customer_codes ,msg_queue = cfg.read_config()

  rtm_client = RTMClient(token=customer_codes['customer1'])
  rtm_client.start()

if __name__ == '__main__':
  main()

#TODO define a main method that takes customer name 
# as argument and starts a listener
# there will be one running process per client.
# maybe there's some way to monitor they are all healthy

#also need to give some thought to how to save the messages - json file ? database  