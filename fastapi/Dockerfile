FROM python:3.9.13-buster
USER root


# environment
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
ENV TZ JST-9



# Installing packages
COPY requirements.txt /root
WORKDIR /root
RUN pip install --no-cache-dir -r requirements.txt

# 最初に起動する際に必要
COPY /src/main.py /root
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8040"]