# Advance_cli_using_click
Click, pytest, pylint, Makefile, Docker, Github Actions, etc

[![Python CI](https://github.com/devendraaa/Advance_cli_using_click/actions/workflows/main.yml/badge.svg)](https://github.com/devendraaa/Advance_cli_using_click/actions/workflows/main.yml)


### To call Microservice

somethings like this
```bash 
curl -X 'POST' \
  'https://psychic-couscous-7rj56vv94jj3rqjp-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build Container

`docker build -t myapp .`
`docker images `

### Run Container 

` docker run -p 127.0.0.1:8080:8080 myapp `

### Invoke Post Request

run `invoke.sh`
