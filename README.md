# Networking Projects
This repository consists up of a few projects I'm working on as I read through [Computer Networking: A Top-Down Approach](https://www.amazon.com/Computer-Networking-Top-Down-Approach-7th/dp/0133594149/). For each project I work on, here, I'll give a brief description of the project as well as anything I learned from its completion.

## Projects

### Project 01: Mini Socket Application
*Language: Python*

In this folder, there will be two sub-directories for the UDP and TCP transport protocols. The network application will be equivalent in each directory and only accomplish that of a client sending some textual data to a server, which will convert that data to uppercase and eventually send it back to the client.

To use, open up one terminal and from either of the directories, run:
```bash
python3 server.py
```
If there aren't any errors, then upon opening up additional terminals, we run multiple client programs for this single server using:
```bash
python3 client.py
```

### Project 02: Web Server
*Language: Python*

Here, I will build a simple web server. The server will do nothing more than parse a request from a client to grab the filename that's attempting to be accessed, open that file (if it exists), and respond with its contents. If the client is a browser, and the file is an HTML file (which is the format assumed here), then we can test this application by seeing the file rendered. You can try that by running,
```bash
python3 server.py
```
then opening your favorite browser (perferably in incognito mode) to `localhost:3000/example.html`. Doing this will send an HTTP request, which is just an attempt to start a TCP connection with the server under an HTTP protocol.

I additionally made an HTTP client here as well, so you can view the response outside of a browser. You can start a client using:
```bash
client.py [server_host] [server_port] [filename]
```
where here, it is best to use `server_host=localhost` and `server_port=3000`. Just make sure to include the `/` in the filename, as in `/example.html`. If done correctly, you should get an HTTP response back printed to the console.

## Upcoming
- [x] ~~Mini Socket Application~~
- [x] ~~Web Server~~
- [ ] Ping program
- [ ] Mail client
- [ ] Multi-threaded Web Proxy