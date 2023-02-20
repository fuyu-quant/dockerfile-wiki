# Dockerfile for data scientists
Summary of docker environments for tools that data scientists might launch with docker   

## Contents
* [Basic docker operations](#basic-docker-operations)
    * [Basic docker commands](#basic-docker-commands)
    * [How to run the Dockerfile](#how-to-run-the-dockerfile)
* [Dockerfiles](#dockerfiles)
    * [Python3](#python3)
    * [Jupyterlab](#jupyterlab)
    * [Dash](#dash)
    * [Streamlit](#streamlit)
    * [MLflow](#mlflow)
    * [Aimflow](#aimflow)
    * [dbt](#dbt)
    * [Prefect](#prefect)
    * [FastAPI](#fastapi)
* [Inter-Container Cooperation](#others)
    * [Docker network](#docker-network)
    * [Docker outside of docker](#docker-outside-of-docker-dood)



## Basic docker operations
### Basic docker commands
```Dockerfile
# Enter the container
docker-compose exec Docker-service-name bash

# Docker image list
docker images

# Remove docker image
dokcer rmi Image-name

# Check active containers
docker ps -a

# Docker network list
docker network ls

# Details of any docker network
docker network inspect Network-name
```


### How to run the Dockerfile
How to start a dockerfile using Docker compose
```bash
# Start container
bash docker.sh up

# Rebuild the docker image and start container
bash docker.sh force

# Stop container
bash docker.sh down

# Stop the container and delete the image
bash docker.sh rm 
```


## Dockerfiles
Explanation of the use and contents of various dockerfiles

### Python3
<img src="images/python3.png" width="200">

```bash
docker compose exec python3 bash
```

### [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
<img src="images/Jupyterlab.png" width="200">

* Link　　
http://localhost:8080/lab
* Reference  


### [Dash](https://dash.plotly.com/)
<img src="images/Dash.png" width="200">
Execution command

```bash
docker-compose exec dash bash -c "python dash/src/app.py"
```
When you want to exit, press [control + c]
* Link  
http://127.0.0.1:8050/
* Reference  
https://qiita.com/NobuYoshi/items/9078d0689fef748486ac

### [Streamlit](https://docs.streamlit.io/)
<img src="images/Streamlit.png" width="200">

unimplemented
* Link  
* Reference  


### [MLflow](https://mlflow.org/docs/latest/index.html)
<img src="images/MLflow.png" width="200">

unimplemented 
* Link　 
http://localhost:15000/#/
* Reference  
a


### [Aimflow](https://github.com/aimhubio/aimlflow)
<img src="images/Aimflow.png" width="200">

unimplemented
* Link　
* Reference 


### [dbt](https://docs.getdbt.com/docs/collaborate/documentation)
<img src="images/dbt.png" width="200">

unimplemented
* Reference



### [Prefect](https://docs.prefect.io/getting-started/overview/)
<img src="images/prefect.png" width="200">

unimplemented
* Link　
* Reference



### [FastAPI](https://fastapi.tiangolo.com/)
<img src="images/FastAPI.png" width="200">

Execution command
```bash
ocker build -t tech_blog_18 ./  
docker run -it --rm -p 8000:8000 tech_blog_18  
ローカルから  
curl -XGET "http://localhost:8000"
```
* Link　
* Reference  
https://buildersbox.corp-sansan.com/entry/tech18_container



### utils
dockerfile templates, etc.





## Inter-Container Cooperation
How to make dockers work together

### Docker network
* Reference  
    https://qiita.com/shundayo/items/8b24af5239d9162b253c  
    https://qiita.com/dhiki1234/items/9a673107eb9310d6aafa

### Docker outside of docker (dood)
* Reference  
    https://hub.docker.com/layers/library/docker/20.10.7-dind/images/sha256-778521a7c301de26994f7aca616ab10c1bc35b8f66b802345d0cad89af381dcb  
    https://qiita.com/t_katsumura/items/d5be6afadd6ec6545a9d  
    https://qiita.com/tkosht/items/7a0721fa9cc69eabf531  