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

docker build -t <名稱>:<標籤> .
使用當前目錄的 Dockerfile 建立映像檔。

docker images
列出本地所有映像檔。

docker rmi <映像名稱>
刪除映像檔。
