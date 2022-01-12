import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import pubsub_v1


if __name__ == '__main__':
  try:
    user_name = 'Bugra'
    message_json = json.dumps({
        'data': {'user_name': user_name},
    })
    message_bytes = message_json.encode('utf-8')
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("cmpe48a-project", "payment_message")
    future = publisher.publish(topic_path, data=message_bytes)
    future.result()
    print("ok")
  except:
    print("not ok")
