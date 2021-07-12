FROM python:3.9

# 環境変数
ENV APP_PATH /opt/apps/server

# パスの準備
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

# 必要なパッケージのインストール
COPY ./packages.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./packages.txt
