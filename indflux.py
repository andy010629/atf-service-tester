from influxdb import InfluxDBClient
from datetime import datetime

# using Http
client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='test-db2')

# client.create_database('test-db2')

# print(client.get_list_database())
print(client.query("select * from test-db2;"))

body = [{
        "measurement": "testests",
        "time": datetime.now().isoformat(),
        # "tags": {
        #     "class": 1,
        #     "age": 123
        # },  
        "fields": {
             "test":123
        },
},]

client.write_points(body)