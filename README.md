# feb22python
Python course at ICC-SC in Feb. 2022

Completed all exercises by 1st April, some issues in pika that need to be discussed

import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = "amqp://abkhan:abkhan@abkhan.tplinkdns.com:5672"
credentials = pika.PlainCredentials('update', 'update')
params = pika.ConnectionParameters('abkhan.tplinkdns.com', 5672, '/', credentials)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
# send a message

channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')
print ("[x] Message sent to consumer")
connection.close()

-----------------------Error-------------------------- may be the IP 174.108.10.72 is not open
ERROR:pika.adapters.utils.io_services_utils:Socket failed to connect: <socket.socket fd=1472, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('0.0.0.0', 2506)>; error=10061 (Unknown error)
ERROR:pika.adapters.utils.connection_workflow:TCP Connection attempt failed: ConnectionRefusedError(10061, 'Unknown error'); dest=(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('174.108.10.72', 5672))
ERROR:pika.adapters.utils.connection_workflow:AMQPConnector - reporting failure: AMQPConnectorSocketConnectError: ConnectionRefusedError(10061, 'Unknown error')
ERROR:pika.adapters.utils.connection_workflow:AMQP connection workflow failed: AMQPConnectionWorkflowFailed: 1 exceptions in all; last exception - AMQPConnectorSocketConnectError: ConnectionRefusedError(10061, 'Unknown error'); first exception - None.
ERROR:pika.adapters.utils.connection_workflow:AMQPConnectionWorkflow - reporting failure: AMQPConnectionWorkflowFailed: 1 exceptions in all; last exception - AMQPConnectorSocketConnectError: ConnectionRefusedError(10061, 'Unknown error'); first exception - None
ERROR:pika.adapters.blocking_connection:Connection workflow failed: AMQPConnectionWorkflowFailed: 1 exceptions in all; last exception - AMQPConnectorSocketConnectError: ConnectionRefusedError(10061, 'Unknown error'); first exception - None
ERROR:pika.adapters.blocking_connection:Error in _create_connection().
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\site-packages\pika\adapters\blocking_connection.py", line 451, in _create_connection
    raise self._reap_last_connection_workflow_error(error)
pika.exceptions.AMQPConnectionError
---------------------------------------------------------------------------
AMQPConnectionError                       Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_4260/2405892442.py in <module>
      9 params.socket_timeout = 5
     10 
---> 11 connection = pika.BlockingConnection(params) # Connect to CloudAMQP
     12 channel = connection.channel() # start a channel
     13 channel.queue_declare(queue='pdfprocess') # Declare a queue

C:\ProgramData\Anaconda3\lib\site-packages\pika\adapters\blocking_connection.py in __init__(self, parameters, _impl_class)
    358         # Perform connection workflow
    359         self._impl = None  # so that attribute is created in case below raises
--> 360         self._impl = self._create_connection(parameters, _impl_class)
    361         self._impl.add_on_close_callback(self._closed_result.set_value_once)
    362 

C:\ProgramData\Anaconda3\lib\site-packages\pika\adapters\blocking_connection.py in _create_connection(self, configs, impl_class)
    449                 error = on_cw_done_result.value.result
    450                 LOGGER.error('Connection workflow failed: %r', error)
--> 451                 raise self._reap_last_connection_workflow_error(error)
    452             else:
    453                 LOGGER.info('Connection workflow succeeded: %r',
