# Tutorial 5: Topics

This service is implemented with [tutorial 5](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)
There are 6 terminals should be opened:

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 2 : To receive all the logs
   1. `make bash`
   2. `python3.6 5-topics/receive_logs_topic.py "#"`
3. Terminal 3: To receive all logs from the facility "kern"
   1. `make bash`
   2. `python3.6 5-topics/receive_logs_topic.py "kern.*"`
4. Terminal 4: to hear only about "critical" logs:
   1. `make bash`
   2. `python3.6 5-topics/receive_logs_topic.py "*.critical"`
5. Terminal 5: to create multiple bindings
   1. `make bash`
   2. `python3.6 5-topics/receive_logs_topic.py "kern.*" "*.critical"`
6. Terminal 6: to emit a log with a routing key "kern.critical" type:
   1. `make bash`
   2. `python3.6 5-topics/emit_log_topic.py "kern.critical" "A critical kernel error"`
7. Let's see what is delivered to the receive_logs
