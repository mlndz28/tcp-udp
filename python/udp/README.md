UDP server and client
========

Start a server in one terminal and as many clients in other terminals.

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
## Client

![UDP Client UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.github.com/mlndz28/c40a4adff4c6a2120d2e679a6952202f/raw/bc8013ce4a122ce6dfecd00427ce024b9b66b4d7/udp-client.puml)

## Server

![UDP Server UML Diagram](http://www.plantuml.com/plantuml/proxy?src=https://gist.github.com/mlndz28/ff49386f3163a9243b111a051c7df714/raw/4cbe970135dc43ca642fed53303db120f2f3b61d/udp-server.puml)
