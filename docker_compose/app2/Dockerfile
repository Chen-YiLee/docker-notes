# 使用 Ubuntu 22.04 作為基礎映像檔
FROM ubuntu:22.04

# 避免互動式安裝卡住
ENV DEBIAN_FRONTEND=noninteractive

# 安裝 Python3 和 pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# 設定預設工作目錄
WORKDIR /app

# 安裝python所需library
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# 複製所有本地檔案進入 container 的 /app
COPY . /app

CMD ["python3", "main.py"]