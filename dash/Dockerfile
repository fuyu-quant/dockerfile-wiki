# dood用
FROM teracy/ubuntu:16.04-dind-17.06.0-ce
USER root


# 環境系
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV TZ JST-9


#USER root
#RUN apk update && apk add build-base libffi-dev python3 python3-dev py3-pip gcc linux-headers musl-dev util-linux

# pythonのinstallに必要
RUN apt-get update && \
    apt-get install -y \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
RUN apt-get update && apt-get install -y --no-install-recommends wget build-essential libreadline-dev \ 
libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev

#任意バージョンのpython install
RUN wget --no-check-certificate https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz \
&& tar -xf Python-3.9.5.tgz \
&& cd Python-3.9.5 \
&& ./configure --enable-optimizations\
&& make \
&& make install
#サイズ削減のため不要なものは削除
RUN apt-get autoremove -y


#RUN apt-get update
#RUN apt-get install -y vim less
#RUN apt-get install -y zsh less
#RUN pip3 install --upgrade pip
#RUN pip3 install --upgrade setuptools
#RUN apt-get install -y \
#    python-pip

# パッケージのインストール
COPY requirements.txt /root
WORKDIR /root
RUN pip3 install --no-cache-dir -r requirements.txt

# dashの不具合のため
#RUN pip uninstall werkzeug
#RUN pip install werkzeug==2.0.0




#EXPOSE 5050
CMD ["bash"]