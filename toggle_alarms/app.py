# code largely derived from https://medium.com/geekculture/enable-or-disable-aws-alarms-at-given-intervals-d2f867aa9aa4

import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def disable_alarms(alarm_names):
  try:
      logger.info(f'Disabling alarms {alarm_names}')
      disable_alarm = client.disable_alarm_actions(AlarmNames=alarm_names)
      return disable_alarm
  except Exception as e:
    logger.error(f'Error while disabling alarms: {alarm_names}, {e}')


def enable_alarms(alarm_names):
  try:
      logger.info(f'Enabling alarms: {alarm_names}')
      enable_alarm = client.enable_alarm_actions(AlarmNames=alarm_names)
      return enable_alarm
  except Exception as e:
    logger.error(f'Error while enable alarms: {alarm_names}, {e}')


def lambda_handler(event, context):
    logger.info(f'## EVENT: {event}')
    
    global client
    client = boto3.client('cloudwatch')

    if event['enable'] == True:
        enable_alarms(event['alarm'])
    else:
        disable_alarms(event['alarm'])
    
    return {
        'statusCode': 200,
    }
