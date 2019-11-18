TCP server and client
========

Start a server in one terminal and as many clients in other terminals. Concurrency in the server is done by threading.

```sh
$ python client.py
  >> Hello World!
  Received: 'HELLO WORLD!'
```

```sh
$ python server.py
  Received: 'Hello World!'
  Sending: 'HELLO WORLD!'

```
