# Dockerfile wiki
Summary of Docker environments for various applications 


## Contents

* [Python runtime environment](#python-runtime-environment)
    * [Python3](#python3)
    * [Jupyterlab](#jupyterlab)
* [WebUI](#webui)
    * [Dash](#dash)
    * [Streamlit](#streamlit)
    * [Gradio](#gradio)
* [Machine Learning Development](#machine-learning-development)
    * [MLflow](#mlflow)
    * [Aimflow](#aimflow)
    * [Weight&BIases](#weightbiases)
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
<img src="images/python3.png" width="100">

### JupyterLab
<img src="images/Jupyterlab.png" width="100">

### GPU


## WebUI

### Dash
<img src="images/Dash.png" width="100">
* [code](https://github.com/fuyu-quant/dockerfile-wiki/tree/develop/webui/dash)
* [image](https://github.com/fuyu-quant/dockerfile-wiki/pkgs/container/webui%2Fdash)


### Streamlit
<img src="images/Streamlit.png" width="100">
* [code](https://github.com/fuyu-quant/dockerfile-wiki/tree/develop/webui/streamlit)
* [image](https://github.com/fuyu-quant/dockerfile-wiki/pkgs/container/webui%2Fstreamlit)


### gradio
<img src="images/gradio.png" width="100">
* [code](https://github.com/fuyu-quant/dockerfile-wiki/tree/develop/webui/gradio)
* [image](https://github.com/fuyu-quant/dockerfile-wiki/pkgs/container/webui%2Fgradio)



## Machine Learning Development

### MLflow
<img src="images/MLflow.png" width="100">

### Aimflow
<img src="images/Aimflow.png" width="100">

### Weights&Biases
<img src="images/wandb.png" width="100">



## Pipeline Tools

### Prefect
<img src="images/prefect.png" width="100">




## WebAPI

### FastAPI
<img src="images/FastAPI.png" width="100">




## Data Transformation

### dbt
<img src="images/dbt.png" width="100">





## Basic docker operations
### Basic docker commands
* docker build
```bash
docker build -t fuyuquant/image_name .
```
* docker run
```bash
docker run --name container_name -d fuyuquant/image_name
```
* docker push
```bash
docker push fuyuquant/image_name
```

## Reference
* [Docker best practice](https://docs.docker.jp/develop/develop-images/dockerfile_best-practices.html)



