FROM python:3.9.13-buster
USER root

RUN apt-get update
RUN apt-get install -y vim less
RUN apt-get install -y zsh less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install \
    dash==1.16.3 \
    pandas \
    category_encoders \
    scikit-learn

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8


# パッケージのインストール
COPY requirements.txt /root
WORKDIR /root
RUN pip install --no-cache-dir -r requirements.txt

# dashの不具合のため
#RUN pip uninstall werkzeug
#RUN pip install werkzeug==2.0.0




#EXPOSE 5050
CMD ["bash"]