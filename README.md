# GetGig
## Django | MySQL | HTML | CSS | Bootstrap | JavaScript | Isotophe | Docker | Prometheus | Grafana

Welcome to GetGig, your festival database! You will be able to discover new festivals and book tickets for each. 

![alt text](image.png)
## Requirements
- Docker
- Docker Compose 
## Instructions
Navigate to GetGig directory, which contains Dockerfile and docker-compose.yml.

Starting the application is as simple as running: 
`docker-compose up -d --build`

The application can be accessed at http://localhost:8000 

Prometheus: http://localhost:9090 | Grafana: http://localhost:3000 

## Superuser 
GetGig uses Django's in-built admin superuser, which is created on startup. In order to change the superuser login/password, open `GetGig/backend/backend/management/commands/seed_db.py` and modify the `get_user_model`.

## Data 
The default setup comes with sample MySQL data, which can be found at `backend/backend/sql`. In the folder you will find two files, `01_schema_example.sql` and `02_dml.sql`. 

The schema outlines the raw MySQL schema, and the DML contains insert statements that the `seed_db.py` command with preform when running docker-compose. Feel free to delete/add/modify the sample data. 
## Prometheus | Grafana 
At the moment, Prometheus/Grafana do have no persistent data. The first time the container is started, you will need to set up Grafana with Prometheus.

Navigate to http://localhost:3000 > Login: admin | Password: admin > Add your first data source > Prometheus > Connection > Prometheus server url: `http://prometheus:9090` > Save & Test

In order to import the sample dashboard: Dashboards > Import dashboard > pase the code contained in `grafana-dashboard.json`.