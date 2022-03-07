from kafka import KafkaConsumer
from json import loads
from time import sleep



# Listener
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9091'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(.1)

# Pull (snapshot)
# consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9091'])
# consumer.subscribe(topics=('test'))
# while True:
#     msg = consumer.poll(timeout_ms=5)   #從kafka獲取訊息
#     print(msg)
#     sleep(2)