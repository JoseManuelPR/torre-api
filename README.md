# Torre API

## Installation

You can use Docker with Dockerfile to create a image of this project or using this DockerCompose creating the file outside of both directories and it's going to install all for you in containers exposing ports in you local.

```bash
version: '3'

services: 
  api-torre:
    stdin_open: true
    restart: unless-stopped
    container_name: api-torre
    build: ./torre-api
    tty: true
    ports:
      - 5023:5000
    volumes:
      - ./torre-api:/var/api-torre

  front-torre:
    stdin_open: true
    restart: unless-stopped
    container_name: front-torre
    build: ./torre-front
    ports:
      - 3023:3000
    links:
      - api-torre
    depends_on:
      - api-torre
    volumes:
      - ./torre-front:/var/front-torre
```

## Usage
### Docs
```bash
http://localhost:5023/docs
```

### Server Status
```bash
http://localhost:5023/health-check
```
