FROM python:3.9.13-buster
USER root

# 環境系
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
ENV TZ JST-9



# パッケージのインストール
COPY requirements.txt /root
WORKDIR /root
RUN pip install --no-cache-dir -r requirements.txt