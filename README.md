# Dockerfile for data scientists
Summary of docker environments for tools that data scientists might launch with docker   

## Contents

* [Python runtime environment](#python-runtime-environment)
    * [Python3](#python3)
    * [Jupyterlab](#jupyterlab)
* [WebUI](#webui)
    * [Dash](#dash)
    * [Streamlit](#streamlit)
* [Machine Learning Development](#machine-learning-development)
    * [MLflow](#mlflow)
    * [Aimflow](#aimflow)
    * [Weight&BIases](#weightbiaseshttpsgithubcomwandbserver)
* [Pipeline Tools](#pipeline-tools)
    * [Prefect](#prefect)
* [WebAPI](#webapi)
    * [FastAPI](#fastapi)
* [Data Transformation](#data-transformation)
    * [dbt](#dbt)

* [Basic docker operations](#basic-docker-operations)
    * [Basic docker commands](#basic-docker-commands)
    * [How to run the Dockerfile](#how-to-run-the-dockerfile)

* [Inter-Container Cooperation](#others)
    * [Docker network](#docker-network)
    * [Docker outside of docker](#docker-outside-of-docker-dood)





## Python runtime environment

### Python3
<img src="images/python3.png" width="200">

### [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
https://github.com/fuyu-quant/jupyterlab-docker



## WebUI

### [Dash](https://dash.plotly.com/)
https://github.com/fuyu-quant/dash-docker

### [Streamlit](https://docs.streamlit.io/)
https://github.com/fuyu-quant/streamlit-docker

### [gradion](https://github.com/gradio-app/gradio)
<img src="images/gradio.png" width="200">



## Machine Learning Development

### [MLflow](https://mlflow.org/docs/latest/index.html)
https://github.com/fuyu-quant/mlflow-docker

### [Aimflow](https://github.com/aimhubio/aimlflow)
https://github.com/fuyu-quant/aimflow-docker


### [Weight&Biases](https://github.com/wandb/server)



## Pipeline Tools

### [Prefect](https://docs.prefect.io/getting-started/overview/)
https://github.com/fuyu-quant/prefect-docker





## WebAPI

### [FastAPI](https://fastapi.tiangolo.com/)
https://github.com/fuyu-quant/fastapi-docker





## Data Transformation

### [dbt](https://docs.getdbt.com/docs/collaborate/documentation)
https://github.com/fuyu-quant/dbt-docker




### utils
dockerfile templates, etc.



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

# Container to container http communication
# container name : Container name for communication destination
# port : Open ports of the container to which you are communicating
curl http://[container name]:[port]/
# example
curl http://fastapi:8040/
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



## Inter-Container Cooperation
How to make dockers work together

### Docker network
* Reference  
    * https://qiita.com/shundayo/items/8b24af5239d9162b253c  
    * https://qiita.com/dhiki1234/items/9a673107eb9310d6aafa

### Docker outside of docker (dood)
* Reference  
    * https://hub.docker.com/layers/library/docker/20.10.7-dind/images/sha256-778521a7c301de26994f7aca616ab10c1bc35b8f66b802345d0cad89af381dcb  
    * https://qiita.com/t_katsumura/items/d5be6afadd6ec6545a9d  
    * https://qiita.com/tkosht/items/7a0721fa9cc69eabf531  

## Reference
* [Docker best practice](https://docs.docker.jp/develop/develop-images/dockerfile_best-practices.html)