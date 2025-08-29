
from azure.eventhub import EventHubProducerClient, EventData
import json, datetime, random, time

producer = EventHubProducerClient.from_connection_string(
    conn_str="Endpoint=sb://traffic-demo.servicebus.windows.net/;SharedAccessKeyName=traffic-policy;SharedAccessKey=PU8yH9p9XVMvnU5odDnUWCxddYrGUbkYu+AEhJpOVMI=;EntityPath=traffic-iot",
    eventhub_name="traffic-iot"
)

while True:
    data = {
        "vehicle_id": random.randint(1000, 9999),
        "speed": random.randint(20, 120),
        "timestamp": str(datetime.datetime.now())
    }
    event = EventData(json.dumps(data))
    with producer:
        producer.send_batch([event])
    print("Sent:", data)
    time.sleep(2)
