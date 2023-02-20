FROM python:3.9.13-buster
USER root


# 環境系
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9



COPY requirements.txt /root
WORKDIR /root
RUN pip install --no-cache-dir -r requirements.txt