# Docker 基本指令與操作筆記

## 🐳 安裝與基本資訊
查看已安裝的 Docker 版本
```bash
docker --version
```
顯示系統整體的 Docker 資訊
```bash
docker info
```

## 📦 映像檔（Image）管理
從 Docker Hub 下載映像檔，例如：docker pull ubuntu
```bash
docker pull <image_name>
```
使用當前目錄的 Dockerfile 建立映像檔
```bash
docker build -t <image_name>:<tag> .
```
列出本地所有映像檔
```bash
docker images
```
刪除映像檔
```bash
docker rmi <image_name>
```

## 🧱 容器（Container）管理
使用映像檔建立並執行容器
```bash
docker run <image_name>
```
啟動容器並進入交互式終端（常用於測試）
```bash
docker run -it <image_name> bash
```
顯示正在運行的容器
```bash
docker ps
```
啟動已停止的容器
```bash
docker start <container_name or container_id>
```
停止正在運行的容器
```bash
docker stop <container_name or container_id>
```
重新啟動容器
```bash
docker restart <container_name or container_id>
```
刪除容器（必須是停止狀態）
```bash
docker rm <container_name or container_id>
```

## 🛠️ 容器互動
在正在運行的容器中執行指令，例如 bash
```bash
docker exec -it <container_name or container_id> <order>
```
查看容器的執行日誌
```bash
docker logs <container_name or container_id>
```
從容器複製檔案到主機
```bash
docker cp  <container_id>:<container_path> <local_path>
```

## 📄 資料卷（Volumes）與資料持久化
建立一個新的資料卷
```bash
docker volume create <volume_name>
```
顯示所有資料卷
```bash
docker volume ls
```
將資料卷掛載至容器中
```bash
docker run -v <volume>:<container_path> <image>
```

## 🧰 網路管理
列出所有 Docker 網路
```bash
docker network ls
```
建立新的網路
```bash
docker network create <network_name>
```
將容器連接到指定網路
```bash
docker network connect <network_name> <container>
```

## 🧹 清理與釋放資源
移除未使用的所有資源（映像檔、容器、網路等
```bash
docker system prune
```
清除未使用的映像檔
```bash
docker image prune
```
刪除已停止的容器
```bash
docker container prune
```
