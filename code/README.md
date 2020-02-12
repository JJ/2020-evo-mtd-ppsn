# Moving target defense for PPSN - code

Contains code for performing the experiments. Read below for installation instructions.

## Installation instructions

You need to install docker and docker-compose, which are used to host
the tested sites.

The code here can be installed in the usual way

    pip install -r requirements.txt

and

    sudo apt-get install nginx

And then tested via `pytest`

## Running the evolutionary algorithm

```
docker-compose build
docker-compose up -d
docker-compose exec www.exampletfm.com python3 genetic.py --individuals=16
```

Spin down containers with

    docker-compose down

