from confluent_kafka import Producer

bootstrap_servers = '20.6.0.141:9092,20.6.0.142:9092,20.6.0.143:9092'
producer = Producer({
    'bootstrap.servers': bootstrap_servers
})
topic = 'foo'
batch_size = 100

for i in range(1, 1000000 + 1):
    key = f'key_{i}'
    value = f'message_{i}'
    producer.produce(topic, key=key, value=value)

    if i % batch_size == 0:
        producer.flush()
        print(f'Sent {i} messages')

producer.flush()