from datetime import datetime
from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# producer.send('test', value={'msg':'test'})

# for j in range(9999):
#     print("Iteration", j)
#     data = {'counter': j}
#     producer.send('test', value={'msg':'test'})
#     sleep(1)

# print("Iteration","test1")
producer.send('test', value={'msg': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
producer.flush()
