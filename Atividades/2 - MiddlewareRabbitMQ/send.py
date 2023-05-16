import pika
import time
import psutil

def sendMessage():
  while True:
    # temperature = 150.5
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    channel.basic_publish(exchange='', routing_key='CPU temperature', body=str(temperature))
    time.sleep(5)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='CPU temperature')

sendMessage()

connection.close()
