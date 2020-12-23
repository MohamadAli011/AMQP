import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://bqnpmbjb:lnpCxdFf-q7KsTZF0nkI5RKUkMxlaCTb@chimpanzee.rmq.cloudamqp.com/bqnpmbjb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='Testing') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='Testing',
                      body='waow')

print(" [x] Sent 'Hello World!'")
connection.close()