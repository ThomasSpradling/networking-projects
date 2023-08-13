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