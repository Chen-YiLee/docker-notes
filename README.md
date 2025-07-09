# 桌面套件安裝
## 安裝XFCE桌面工具
XFCE是較輕量化的桌面工具，RAM和CPU的占用量較少。
對於老舊電腦、虛擬機或需要節省資源的伺服器特別合適。

安裝步驟
### 1. 更新套件
```bash
sudo apt update && sudo apt upgrade -y
```
### 2. 安裝 XFCE 桌面環境 
```bash
sudo apt install xfce4 lightdm -y
```
### 3.安裝登錄管理器（建議用 lightdm）
安裝過程中會跳出畫面問你選擇預設的登入管理器，請選「lightdm」
如果沒有跳出來則輸入：
```bash
sudo apt install lightdm -y
```
4. 安裝完成後，重新啟動 (先不要做這行)
```bash
sudo reboot
```


# Docker 基本指令與操作筆記
## 安裝 Docker 在 Ubuntu 22.04 (ARM 架構)
---
## ✅ 系統需求
- 作業系統：Ubuntu 22.04 (ARM64 / aarch64)
- 權限：具有 `sudo` 權限的使用者
- 網路：可以存取 `https://download.docker.com`
---

## 🧰 安裝步驟
### 1. 更新套件並安裝必要工具
```bash
sudo apt update
```
```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
```
---
### 2. 新增 Docker GPG 金鑰
```bash
sudo mkdir -p /etc/apt/keyrings
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
---
### 3. 新增 Docker APT 套件來源
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
---
### 4. 安裝 Docker Engine 與相關工具
```bash
sudo apt update
```
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
---
### 5. 啟用並啟動 Docker 服務
```bash
sudo systemctl enable docker
```
```bash
sudo systemctl start docker
```
---
### 6. 測試 Docker 是否安裝成功
```bash
sudo docker run hello-world
```
 應該會看到 Docker 成功運作的歡迎訊息

---
### 7. 讓使用者不需 sudo 執行 Docker (可不執行)
```bash
sudo usermod -aG docker $USER
```
執行後請 **重新登入或重啟機器**，或輸入以下指令立即生效：
```bash
newgrp docker
```
---
## 📌 備註
- 安裝過程會自動選擇適合 ARM 的套件，無需手動指定架構。
- 如需部署特定服務，可搜尋是否支援 ARM 的 Docker 映像（例如 `arm64v8/nginx`）。
---
## 🔗 參考資料
- [Docker 官方文件](https://docs.docker.com/engine/install/ubuntu/)
- [ARM 架構映像庫](https://hub.docker.com/search?q=&type=image&architecture=arm64)

  
### 🐳 安裝與基本資訊

| 指令             | 說明                       |
|:-----------------|:---------------------------|
| docker --version | 查看已安裝的 Docker 版本   |
| docker info      | 顯示系統整體的 Docker 資訊 |

### 📦 映像檔（Image）管理

| 指令                                 | 說明                       |
|:-------------------------------------|:---------------------------|
| docker pull <image_name>             | 下載映像檔                 |
| docker build -t <image_name>:<image_tag> . | 使用 Dockerfile 建立映像檔 |
| docker images                        | 列出本地所有映像檔         |
| docker rmi <image_name>              | 刪除映像檔                 |

### 🧱 容器（Container）管理

| 指令                                            | 說明               |
|:------------------------------------------------|:-------------------|
| docker run <image_name>                         | 執行映像檔建立容器 |
| docker run -it <image_name> bash                | 交互式終端執行容器 |
| docker ps                                       | 顯示運行中容器     |
| docker start <container_name or container_id>   | 啟動容器           |
| docker stop <container_name or container_id>    | 停止容器           |
| docker restart <container_name or container_id> | 重新啟動容器       |
| docker rm <container_name or container_id>      | 刪除容器           |

### 🛠️ 容器互動

| 指令                                                     | 說明           |
|:---------------------------------------------------------|:---------------|
| docker exec -it <container_name or container_id> <order> | 容器內執行指令 |
| docker logs <container_name or container_id>             | 查看容器日誌   |
| docker cp <container_id>:<container_path> <local_path>   | 從容器複製檔案 |

### 📄 資料卷（Volumes）與資料持久化

| 指令                                            | 說明             |
|:------------------------------------------------|:-----------------|
| docker volume create <volume_name>              | 建立資料卷       |
| docker volume ls                                | 顯示所有資料卷   |
| docker run -v <volume>:<container_path> <image> | 掛載資料卷至容器 |

### 🧰 網路管理

| 指令                                              | 說明               |
|:--------------------------------------------------|:-------------------|
| docker network ls                                 | 列出 Docker 網路   |
| docker network create <network_name>              | 建立新網路         |
| docker network connect <network_name> <container> | 容器連接至指定網路 |

### 🧹 清理與釋放資源

| 指令                   | 說明                 |
|:-----------------------|:---------------------|
| docker system prune    | 移除未使用的所有資源 |
| docker image prune     | 清除未使用的映像檔   |
| docker container prune | 刪除已停止的容器     |

# 🐳 從 Dockerfile 建立映像檔並進入容器（完整範例）

這是一個簡單的範例說明如何使用 Dockerfile 建立映像檔，執行容器並進入互動式終端。

---

## 📁 1. 建立 Dockerfile

在你的工作目錄中建立一個名為 `Dockerfile` 的檔案，內容如下：

```Dockerfile
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
# 複製所有本地檔案進入 container 的 /app
COPY . /app

# 使用 sleep infinity 讓 container 持續運作
CMD ["sleep", "infinity"]
```

---

## 🛠️ 2. 建立映像檔

在有 `Dockerfile` 的目錄中執行：

```bash
docker build -t <image_name> .
```

- `-t <image_name>`：建立的映像檔名稱
- `.`：表示使用目前目錄的 Dockerfile

---

## 🚀 3. 執行容器

```bash
docker run -d --name <container_name> <image_name>
```

- `-it`：互動模式與終端
- `--name`：指定容器名稱
- `<image_name>`：剛剛建立的映像名稱

進入容器後會看到熟悉的 Ubuntu shell。

### 用volume執行容器
```bash
docker run -d -v <volume>:<container_path> --name <container_name> <image_name>
```

---

## 🔁 4. 再次進入已建立的容器

若你已離開容器，可以使用以下方式重新進入(要確保容器還在執行)：

```bash
docker exec -it <container_name> bash
```

---

## 🧹 5. 清除容器與映像檔

```bash
docker stop <container_name>
docker rm <container_name>
docker rmi <image_name>
```

---

## 🧾 小提示

- 可加入更多 `RUN` 指令自訂環境（如 Git、Python 等）
- 你也可以透過 `docker volume` 掛載資料夾進容器



# Docker Compose 指令教學筆記

Docker Compose 是用來 **定義與管理多個容器服務** 的工具，透過一個 `docker-compose.yml` 檔案即可統一控制整個應用環境。

---
### 安裝docker-compose 工具：
```bash
sudo apt install docker-compose 
```
## 📦 常用指令總覽

| 指令                                      | 說明                                          |
|-------------------------------------------|-----------------------------------------------|
| `docker-compose up`                       | 啟動所有服務，根據 yml 建立容器              |
| `docker-compose up -d`                    | 背景模式執行容器                              |
| `docker-compose down`                     | 停止並移除容器、網路等                        |
| `docker-compose build`                    | 建構映像檔                                    |
| `docker-compose stop`                     | 停止容器但不移除                              |
| `docker-compose start`                    | 啟動已停止的容器                              |
| `docker-compose restart`                  | 重新啟動容器                                  |
| `docker-compose ps`                       | 顯示服務狀態                                  |
| `docker-compose logs`                     | 查看日誌                                      |
| `docker-compose logs -f`                  | 即時追蹤日誌                                  |
| `docker-compose exec <服務名稱> <指令>`   | 在容器中執行指令                              |
| `docker-compose config`                   | 驗證設定檔格式                                |
| `docker-compose pull`                     | 下載映像檔                                     |
| `docker-compose rm`                       | 刪除已停止的服務容器                          |

---

## 🚀 常用操作範例

### 啟動服務（背景模式）：
```bash
docker-compose up -d
```

### 查看執行中的容器：
```bash
docker-compose ps
```

### 查看並追蹤日誌：
```bash
docker-compose logs -f
```

---

## 📁 範例 docker-compose.yml

```yaml
version: "3.9"

services:
  app1:
    build: ./app1
    container_name: app1
    ports:
      - "5000:5000"
    depends_on:
      - app2
    restart: unless-stopped

  app2:
    build: ./app2
    container_name: app2
    ports:
      - "5001:5001"
    restart: unless-stopped
    
```

---

## 📌 小提示

- `docker-compose.yml` 必須與指令執行目錄在同一層
- 支援 `.env` 環境變數設定
- 適用於開發、測試、CI/CD、自動化部署等場景

---

> ✍️ 文件整理：Chen-Yi Lee 
> 📄 用途：Docker Compose 學習筆記、快速查詢

