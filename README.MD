Simple TCP and UDP servers and clients
===============

## TCP

Start a server in one terminal and as many clients in other terminals. Concurrency in the server is done by threading.

```sh
$ python tcp/client.py
  >> Hello World!
  Received: 'HELLO WORLD!'
```

```sh
$ python tcp/server.py
  Received: 'Hello World!'
  Sending: 'HELLO WORLD!'

```
### Client

![TCP Server UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/mlndz28/820dc32e1af51287c95e95c42ef0fa62/raw/2512cdd434a92c33206e9a75a26fbd87f96846a7/tcp-client.puml)

### Server


![TCP client UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.githubusercontent.com/mlndz28/7ff42646e16f15c29fc22d11ed47782f/raw/b82bfbb3481e7f91bc82c8dd98ee2dd3ec0e76e9/tcp-server.puml)


## UDP

Start a server in one terminal and as many clients in other terminals.

```sh
$ python udp/client.py
  >> Hello World!
  Received: 'HELLO WORLD!'
```

```sh
$ python udp/server.py
  Received: 'Hello World!'
  Sending: 'HELLO WORLD!'

```
### Client

![UDP Client UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.github.com/mlndz28/c40a4adff4c6a2120d2e679a6952202f/raw/bc8013ce4a122ce6dfecd00427ce024b9b66b4d7/udp-client.puml)

### Server

![UDP Server UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.github.com/mlndz28/ff49386f3163a9243b111a051c7df714/raw/4cbe970135dc43ca642fed53303db120f2f3b61d/udp-server.puml)
