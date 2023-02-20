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
docker-compose exec Dockerのサービス名 bash

### How to run the Dockerfile
How to start a dockerfile using Docker compose
```shell-session
# start container
bash docker.sh up

# rebuild the docker image and start container
bash docker.sh force

# stop container
bash docker.sh down

# stop the container and delete the image
bash docker.sh rm 
```


## Dockerfiles
Explanation of the use and contents of various dockerfiles

### Python3
docker compose exec python3 bash


### JupyterLab
http://localhost:8080/lab


### Dash
* 実行コマンド
docker-compose exec dash bash -c "python dash/src/app.py"
* リンク　　
http://127.0.0.1:8050/
* 終了コマンド
control + c
* 参考リンク
https://qiita.com/NobuYoshi/items/9078d0689fef748486ac

### streamlit
unimplemented


### MLflow
unimplemented  
http://localhost:15000/#/


### Aimflow
unimplemented  
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
