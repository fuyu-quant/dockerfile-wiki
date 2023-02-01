FROM python:3.7.3
USER root

RUN apt-get update
RUN apt-get install -y vim less
RUN apt-get install -y zsh less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# dashの不具合のため
#RUN pip uninstall werkzeug
#RUN pip install werkzeug==2.0.0

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

EXPOSE 5050
CMD ["bash"]