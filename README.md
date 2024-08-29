# Basic HTTP Server

Sets up a toy HTTP/1.0 IPv4 server

## Launch HTTP Server 

```
$ python server.py
```

## Make raw HTTP requests 

To make raw text HTTP requests to the server I'd recommend using `telnet`. To open up a client connection to the server run `telnet localhost 8000`. A few examples of how to interface with telnet from there are provided below.

### GET Request
```
$ telnet localhost 8000
Connected to localhost.
Escape character is '^]'.
GET /about HTTP/1.0

<h1>Hello, world!</h1>
```

### Resources
- [Joao's awesome guide to setting up a basic HTTP server](https://joaoventura.net/blog/2017/python-webserver/)
- [Brief HTTP history](https://hpbn.co/brief-history-of-http/)
- [Great documentation on general BSD socket APIs](https://en.wikipedia.org/wiki/Berkeley_sockets)
- [Python Socket HOWTO](https://docs.python.org/3/howto/sockets.html#socket-howto)