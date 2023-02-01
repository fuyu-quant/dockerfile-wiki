FROM python:3.9.7-buster as builder

#ENV PROJECT_DIR opt
#WORKDIR /${PROJECT_DIR}
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt
 
#sqlalchemy 
#psycopg2-binary google-cloud-storage azure-storage-blob boto3

CMD [ "mlflow", "server", "--backend-store-uri", "/opt/outputs", "--default-artifact-root", "/opt/outputs", "--host", "0.0.0.0" ]