FROM python:3.9.13-slim
USER root

# environment
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
ENV TZ JST-9


COPY . ~/gradio

# Installing packages
WORKDIR ~/gradio
RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "app.py"]