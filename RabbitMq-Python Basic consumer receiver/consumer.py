import pika

def on_message_received(channel,method,properties,body):
    print(f"Received message:{body}")

try:
    connection_params = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue="PyRabbit")
    channel.basic_consume(queue="PyRabbit",auto_ack=True,on_message_callback=on_message_received)
    
    print('Starting consumer')
    channel.start_consuming()

except:
    print('Some error occured please try later !')
