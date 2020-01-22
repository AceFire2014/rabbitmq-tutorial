# Tutorial 2: Work Queues

This service is implemented with [tutorial 3](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
There are four terminals should be opened:

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 3 and 4: run this service with `receive_logs`:
   1. `make bash`
   2. `python3.6 3-publish-subscribe/receive_logs.py`
3. Terminal 2: run this service with `emit_log`:
   1. `make bash`
   2. `python3.6 3-publish-subscribe/emit_log.py`
   3. run following commands:
      1. `python3.6 3-publish-subscribe/emit_log.py First message.`
      2. `python3.6 3-publish-subscribe/emit_log.py Second message..`
      3. `python3.6 3-publish-subscribe/emit_log.py Third message...`
      4. `python3.6 3-publish-subscribe/emit_log.py Fourth message....`
      5. `python3.6 3-publish-subscribe/emit_log.py Fifth message.....`
4. Let's see what is delivered to the receive_logs
