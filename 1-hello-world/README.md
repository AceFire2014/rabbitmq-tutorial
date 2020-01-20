# Tutorial 1: Hello World

There are three terminals should be created:

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 2: run this service with message listener:
   1. `make bash`
   2. `python3.6 1-hello-world-app/receive.py`
3. Terminal 3: run this service with message sender:
   1. `make bash`
   2. `python3.6 1-hello-world-app/sender.py`
