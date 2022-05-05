import pika

try:
    connection_params = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue="PyRabbit")
    channel.basic_publish(exchange='',routing_key='PyRabbit',body="Message to Rabbit from Python !")
    connection.close()
    print('Message Sent')
except:
    print('Some error occured please try later !')
