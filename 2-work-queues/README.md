# Tutorial 2: Work Queues

This service is implemented with [tutorial 2](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
There are four terminals should be opened:

## Round-robin dispatching

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 3 and 4: run this service with `worker`:
   1. `make bash`
   2. `python3.6 round-robin-dispatching/worker.py`
3. Terminal 2: run this service with `new_task`:
   1. `make bash`
   2. `python3.6 round-robin-dispatching/new_task.py`
   3. run following commands:
      1. `python3.6 round-robin-dispatching/new_task.py First message.`
      2. `python3.6 round-robin-dispatching/new_task.py Second message..`
      3. `python3.6 round-robin-dispatching/new_task.py Third message...`
      4. `python3.6 round-robin-dispatching/new_task.py Fourth message....`
      5. `python3.6 round-robin-dispatching/new_task.py Fifth message.....`
4. Let's see what is delivered to the workers

## Message Acknowledgement

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 3 and 4: run this service with `worker`:
   1. `make bash`
   2. `python3.6 message-acknowledgement/worker.py`
3. Terminal 2: run this service with `new_task`:
   1. `make bash`
   2. `python3.6 message-acknowledgement/new_task.py`
   3. run following commands:
      1. `python3.6 message-acknowledgement/new_task.py First message.`
      2. `python3.6 message-acknowledgement/new_task.py Second message..`
      3. `python3.6 message-acknowledgement/new_task.py Third message...`
      4. `python3.6 message-acknowledgement/new_task.py Fourth message....`
      5. `python3.6 message-acknowledgement/new_task.py Fifth message.....`
4. Let's see what is delivered to the workers

## message durability

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 3 and 4: run this service with `worker`:
   1. `make bash`
   2. `python3.6 message-durability/worker.py`
3. Terminal 2: run this service with `new_task`:
   1. `make bash`
   2. `python3.6 message-durability/new_task.py`
   3. run following commands:
      1. `python3.6 message-durability/new_task.py First message.`
      2. `python3.6 message-durability/new_task.py Second message..`
      3. `python3.6 message-durability/new_task.py Third message...`
      4. `python3.6 message-durability/new_task.py Fourth message....`
      5. `python3.6 message-durability/new_task.py Fifth message.....`
4. Let's see what is delivered to the workers
