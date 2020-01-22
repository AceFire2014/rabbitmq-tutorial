# Tutorial 4: Routing

This service is implemented with [tutorial 4](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
There are four terminals should be opened:

1. Terminal 1: run the rabbitmq service: `docker-compose up`
2. Terminal 2 : run this service with `receive_logs_direct`:
   1. `make bash`
   2. `python3.6 4-routing/receive_logs_direct.py warning error > logs_from_rabbit.log`, save only 'warning' and 'error' (and not 'info') log messages to a file
3. Terminal 3: run this service with another `receive_logs_direct`:
   1. `make bash`
   2. `python3.6 4-routing/receive_logs_direct.py info warning error`, to see all the log messages on your screen.
4. Terminal 4: run this service with `emit_log_direct`:
   1. `make bash`
   2. `python3.6 4-routing/emit_log_direct.py error "Run. Run. Or it will explode"`
   3. `python3.6 4-routing/emit_log_direct.py info "Run. Run. Or it will explode"`
5. Let's see what is delivered to the receive_logs
