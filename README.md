# DataScientist_MLOps
データサイエンティスト向けのMLOps的な何か

## Docker
* Docker環境の入り方
docker-compose exec Dockerのサービス名 bash

## JupyterLab
http://localhost:8080/lab

## Python3の環境
docker compose exec python3 bash

## Dashの立ち上げ
* コマンド
docker-compose exec dash-app zsh -c "python dash/app/app.py"
* リンク　　
http://127.0.0.1:8050/
* 終了コマンド
control + c
* 参考リンク
https://qiita.com/NobuYoshi/items/9078d0689fef748486ac

## mlflowへアクセス
http://localhost:15000/#/

## operation
* doodにより他のdockerを制御するためのdocker環境
* 以下のコマンドでoperationのdocker環境に入る  
docker-compose exec operation bash
* 以下のコマンドでDashを立ち上げたりできる   
docker exec dash-app bash -c "python dash/app/app.py"
* prefect
https://github.com/rpeden/prefect-docker-compose


## 全体の設計
* Dashで入力を受け取る
    誤った入力→無視
    正しい入力→doodでoperationのdockerにアクセス
    operationのpythonファイルを実行
    operationからもdoodにより他のdocker環境にアクセス→値を取得
    