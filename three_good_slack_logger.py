import os.path
import json
import datetime
import slack  
import time, sys
from slack import RTMClient
from absl import flags
import json

import config_file as cfg

flags.DEFINE_string('config_file', None, 'location of the config xlsx file.')
flags.DEFINE_string('customer', None, 'customer.')
FLAGS = flags.FLAGS
FLAGS(sys.argv)

CUSTOMER_NAME =''

@RTMClient.run_on(event="message")
def logCSVMessage(**payload):
  data = payload['data']
  data['customer']= FLAGS.customer

  logfile = f'log-{datetime.datetime.now().strftime("%Y%m%d")}.csv'
  if not os.path.exists(logfile):
    with open(logfile, 'a') as file:
      file.write('customer,text,user,team,user_team,source_team,channel,event_ts,ts\n')

  with open(logfile, 'a') as file:
    message = f"{data['customer']},{data['text']}, {data['user']}, {data['team']}, {data['user_team']},{data['source_team']}, {data['channel']}, {data['event_ts']}, {data['ts']}\n"
    file.write(message)
  print(f'CSVLogger: logged message to {logfile}')

@RTMClient.run_on(event="message")
def logJSONMessage(**payload):
  data = payload['data']
  data['customer']= FLAGS.customer
  logfile = f'log-{datetime.datetime.now().strftime("%Y%m%d")}.json'
   
  if not os.path.exists(logfile):
    empty_data = []
    with open(logfile, 'w') as file:  
      json.dump(empty_data,file)
  
  json_log =''
  with open(logfile, 'r') as file:  
      json_log = json.load(file)
  with open(logfile, 'w') as file:  
      json_log.append(data)  
      json.dump(json_log,file)
  print(f'JSONLogger: logged message to {logfile}')


def main():
  flags.mark_flag_as_required('customer')

  CUSTOMER_NAME = FLAGS.customer
  customer_codes ,msg_queue = cfg.read_config()

  rtm_client = RTMClient(token=customer_codes['customer1'])
  print(f'logging {FLAGS.customer}:{customer_codes["customer1"]}')  
  rtm_client.start()

if __name__ == '__main__':
  main()


#also need to give some thought to how to save the messages - json file ? database  