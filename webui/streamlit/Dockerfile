# streamlitがサポートしているのはpython3.7〜3.9
FROM python:3.9.13-slim
USER root

# environment
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
ENV TZ JST-9


# Installing packages
COPY ../streamlit ~/streamlit

# Installing packages
WORKDIR ~/streamlit
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["streamlit", "run", "~/streamlit/app.py", "--server.port=8060", "--server.address=0.0.0.0"]