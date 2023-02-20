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
```bash
docker compose exec python3 bash
```

### JupyterLab
* Link　　
http://localhost:8080/lab


### Dash
Execution command
```bash
docker-compose exec dash bash -c "python dash/src/app.py"
```
When you want to exit, press [control + c]
* Link　　
http://127.0.0.1:8050/
* Reference
https://qiita.com/NobuYoshi/items/9078d0689fef748486ac

### streamlit
unimplemented
* Link


### MLflow
unimplemented  
* Link
http://localhost:15000/#/


### Aimflow
unimplemented
* Link
* 参考サイト
https://github.com/aimhubio/aimlflow

### dbt
unimplemented


### Prefect
unimplemented


### FastAPI
unimplemented  
* 参考サイト
https://buildersbox.corp-sansan.com/entry/tech18_container
* APIの実行
docker build -t tech_blog_18 ./  
docker run -it --rm -p 8000:8000 tech_blog_18  
ローカルから  
curl -XGET "http://localhost:8000"



### utils
dockerfile templates, etc.




## Inter-Container Cooperation


### Docker network
* 参考サイト
https://qiita.com/shundayo/items/8b24af5239d9162b253c
