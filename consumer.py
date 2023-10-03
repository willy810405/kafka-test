from confluent_kafka import Consumer, KafkaError

bootstrap_servers = '20.6.0.141:9092,20.6.0.142:9092,20.6.0.143:9092'
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'foo_group',
    'auto.offset.reset': 'earliest' 
})
topic = 'foo'
consumer.subscribe([topic])
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error: {}'.format(msg.error()))
    else:
        print('Received message: {}'.format(msg.value()))