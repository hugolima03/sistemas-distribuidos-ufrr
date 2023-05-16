import pika
from playsound import playsound

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Fire detected!')

def callback(ch, method, properties, temperature):
    print("Fire alert received")
    playsound('./assets/alarm.mp3')

channel.basic_consume(queue='Fire detected!', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
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
