import pika

params = pika.ConnectionParameters(host="rabbitmq")

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)


# enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
