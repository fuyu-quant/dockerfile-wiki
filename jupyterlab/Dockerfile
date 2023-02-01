FROM python:3.9.7-buster
USER root
ARG DEBIAN_FRONTEND=noninteractive

# パッケージの追加とタイムゾーンの設定
# 必要に応じてインストールするパッケージを追加してください
RUN apt-get update && apt-get install -y \
    tzdata \
&&  ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Tokyo

# JupyterLab関連のパッケージ（いくつかの拡張機能を含む）
# 必要に応じて、JupyterLabの拡張機能などを追加してください
RUN python3 -m pip install --upgrade pip \
&&  pip install --no-cache-dir \
    black \
    jupyterlab \
    jupyterlab_code_formatter \
    jupyterlab-git \
    #lckr-jupyterlab-variableinspector \
    jupyterlab_widgets \
    ipywidgets \
    jupyterlab-language-pack-ja-JP \
    import-ipynb


# GitHubからsshでcloneするための設定
# 参考になったサイト
# https://github.com/yuiki-iwayama/JupyterLab-Docker
ARG GITHUB_USER
ARG GITHUB_EMAIL
RUN mkdir -p ~/.ssh  && \
  git config --global user.name "fuyu-quant" && \
  git config --global user.email fuyufuyu@gamil.com
#COPY ./jupyterlab/utils/config /root/.ssh
#COPY ./jupyterlab/utils/init.sh /usr/bin

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt