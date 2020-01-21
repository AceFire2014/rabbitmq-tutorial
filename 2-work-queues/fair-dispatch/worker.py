import time
import pika

params = pika.ConnectionParameters(host="rabbitmq")

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count("."))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)

# enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
