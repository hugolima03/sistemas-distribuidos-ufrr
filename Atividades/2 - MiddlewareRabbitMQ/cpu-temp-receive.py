import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Fire detected!')
channel.queue_declare(queue='CPU temperature')

def callback(ch, method, properties, temperature):
    print("Receiving temperature: ", float(temperature))
    if (float(temperature) > 70):
        print("High temperature!")
        channel.basic_publish(exchange='', routing_key='Fire detected!', body="true")

channel.basic_consume(queue='CPU temperature', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages on cpu temp channel. To exit press CTRL+C')
channel.start_consuming()

connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
