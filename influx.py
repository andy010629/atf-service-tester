from influxdb import InfluxDBClient
from datetime import datetime

# using Http
client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root',database="testdb")

# client.create_database('testdb')

# print(client.get_list_database())

body = [{
        "measurement": "test",
        # "time": datetime.now().isoformat(),
        "fields": {
             "test":123
        },
},]

client.write_points(body)
print(client.query("select * from testdb;"))