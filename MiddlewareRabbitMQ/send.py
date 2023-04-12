import pika

print()

temperature = 40.5;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='CPU temperature')

channel.basic_publish(exchange='', routing_key='CPU temperature', body=str(temperature))

connection.close()
