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
### Client

![TCP Server UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/mlndz28/820dc32e1af51287c95e95c42ef0fa62/raw/2512cdd434a92c33206e9a75a26fbd87f96846a7/tcp-client.puml)

### Server


![TCP client UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/mlndz28/7ff42646e16f15c29fc22d11ed47782f/raw/b82bfbb3481e7f91bc82c8dd98ee2dd3ec0e76e9/tcp-server.puml)
