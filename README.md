# Dockerfile wiki
[Docker hub](https://hub.docker.com/u/fuyuquant)\\
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

### [Python3](https://github.com/fuyu-quant/python3-docker)
<img src="images/python3.png" width="200">

### [JupyterLab](https://github.com/fuyu-quant/jupyterlab-docker)
<img src="images/Jupyterlab.png" width="200">




## WebUI

### [Dash](https://github.com/fuyu-quant/dash-docker)
<img src="images/Dash.png" width="200">

### [Streamlit](https://github.com/fuyu-quant/streamlit-docker)
<img src="images/Streamlit.png" width="200">

### [gradion](https://github.com/fuyu-quant/gradio-docker)
<img src="images/gradio.png" width="200">




## Machine Learning Development

### [MLflow](https://github.com/fuyu-quant/mlflow-docker)
<img src="images/MLflow.png" width="200">

### [Aimflow](https://github.com/fuyu-quant/aimflow-docker)
<img src="images/Aimflow.png" width="200">

### [Weights&Biases](https://github.com/fuyu-quant/wandb-docker)
<img src="images/wandb.png" width="200">



## Pipeline Tools

### [Prefect](https://github.com/fuyu-quant/prefect-docker)
<img src="images/Prefect.png" width="200">




## WebAPI

### [FastAPI](https://github.com/fuyu-quant/fastapi-docker)
<img src="images/FastAPI.png" width="200">




## Data Transformation

### [dbt](https://github.com/fuyu-quant/dbt-docker)
<img src="images/dbt.png" width="200">





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



