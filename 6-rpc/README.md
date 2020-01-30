# Tutorial 6: RPC

This service is implemented with [tutorial 6](https://www.rabbitmq.com/tutorials/tutorial-six-python.html)
There are 3 terminals should be opened:

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 2 : To receive all the logs
   1. `make bash`
   2. `python3.6 6-rpc/rpc_server.py`
3. Terminal 3: To receive all logs from the facility "kern"
   1. `make bash`
   2. `python3.6 6-rpc/rpc_client.py`
