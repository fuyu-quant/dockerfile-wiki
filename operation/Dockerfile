#https://github.com/teracyhq/docker-files/tree/master/ubuntu
#doodをするための
#https://blog.nijohando.jp/post/docker-in-docker-docker-outside-of-docker/
FROM teracy/ubuntu:16.04-dind-17.06.0-ce
USER root

# 環境系
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9


#RUN sudo apt-get update && \
#    sudo apt-get install -y \
#    ca-certificates \
#    curl \
#    gnupg \
#    lsb-release && \
#    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
#  echo \
#  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
#  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
#  sudo apt-get update && \
#  sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    docker.io 
    #docker-compose \
#&&  apt-get autoremove -y \
#&&  apt-get clean \
# この下はどっちが必要か分からない
#&&  rm -rf /var/lib/apt/lists/* \  
#&&  rm -rf /usr/local/src/*

#RUN apt-get update -y
#RUN apt-get install ca-certificates curl gnupg lsb-release -y
#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
#RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#RUN apt-get update
#RUN apt-get install docker-ce docker-ce-cli containerd.io



#RUN python3 -m pip install --upgrade pip 
#RUN pip install --upgrade setuptools

# パッケージのインストール
#COPY requirements.txt /root
#WORKDIR /root
#RUN pip install --no-cache-dir -r requirements.txt