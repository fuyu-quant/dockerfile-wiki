# dood用
FROM teracy/ubuntu:16.04-dind-17.06.0-ce
USER root


# 環境系
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9


#RUN apt-get update && apt-get install -y \
#    python3.8 \
#    python3-pip

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    vim \
#    zsh \
#    wget \
#    curl \
#    python3.9 \
#    python3.9-dev \
#&&  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \ 
#&&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
# apt-getのキャッシュを削除するためのコード
# https://nykergoto.hatenablog.jp/entry/2020/07/25/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AAdockerfile%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%A8%E3%81%8D%E3%81%AB%E6%B0%97%E3%82%92%E3%81%A4%E3%81%91%E3%81%A8%E3%81%8F%E3%81%A8%E8%89%AF%E3%81%84%E3%81%93
#&&  apt-get autoremove -y \
#&&  apt-get clean \
# この下はどっちが必要か分からない
#&&  rm -rf /var/lib/apt/lists/* \  
#&&  rm -rf /usr/local/src/*


#RUN apt-get install -y vim less
#RUN apt-get install -y zsh less


#RUN apt-get update && apt-get install -y python3.9 python3.9-dev

RUN apt-get update && \
    apt-get install -y \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
#RUN apt-get update && apt-get install -y --no-install-recommends wget build-essential libreadline-dev \ 
#libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev

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
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# パッケージのインストール
COPY requirements.txt /root
WORKDIR /root
RUN pip install --no-cache-dir -r requirements.txt

# dashの不具合のため
#RUN pip uninstall werkzeug
#RUN pip install werkzeug==2.0.0




#EXPOSE 5050
CMD ["bash"]