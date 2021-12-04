
# LineBot實作

我使用 Python LINE Bot SDK 在 Heroku 上架設一個簡單的自我介紹機器人。

![](https://i.imgur.com/XMEDTeR.png)

https://youtu.be/yP7xa2vX6dI 




## 在你開始之前

確保您具有以下內容：

- 擁有 Line 帳號
- 擁有 [Heroku](https://www.heroku.com) 帳戶（您可以免費創建一個）

## Step1: 建立 Heroku 專案

1. 登入 Heroku 後，在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App

2. 輸入自己喜歡的 App name ，然後點擊 Create app

## Step2: 創建 Line Bot 頻道

1. 進入 [Line 控制台](https://developers.line.me/console/)

2. 創建提供者
3. 填入提供者名稱
4. 點擊 Create
5. 點擊 Create Channel
6. 填入 Bot 資訊
7. 同意 Line 條款，並按 Create
8. 選擇剛剛創建的 Bot

## 設定範例機器人

按照以下步驟架設一個回話機器人。

1. 下載 [範例程式碼](https://github.com/yaoandy107/line-bot-tutorial/archive/master.zip)
2. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的機器人
3. 開啟 webhook
4. 關閉預設罐頭回覆訊息

5. 產生 **Channel access token**
6. 取得 **Channel access token**
7. 取得 **Channel secret**

8. 使用編輯器開啟範例程式碼資料夾內的 app.py，將剛剛取得的 **channel secret** 和 **channel access token** 填入
   ![](https://i.imgur.com/Uz16joi.png)

## 將程式推到 Heroku 上

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟剛剛下載的範例程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序登錄到 Heroku
   ```shell＝
   heroku login
   ```
4. 初始化 git

   ```shell=
   $ git config --global user.name "你的名字"
   $ git config --global user.email 你的信箱
   ```

   注意：**你的名字** 和 **你的信箱** 要換成各自的 **名字** 和 **信箱**

5. 初始化 git

   ```shell＝
   git init
   ```

   注意：僅第一次使用時要輸入

6. 用 git 將資料夾與 heroku 連接
   ```shell＝
   heroku git:remote -a {HEROKU_APP_NAME}
   ```
   注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱
7. 輸入以下指令，將程式碼推上 Heroku，**如果有跳出錯誤請重新輸入**
   ```shell
   git add .
   git commit -m "Add code"
   git push -f heroku master
   ```
   **每當需要更新 Bot 時，請重新輸入上述指令**

## 將 Heroku 與 Line 綁定

1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
2. 在 webhook URL 中輸入 Heroku 網址

   ```shell
   {HEROKU_APP_NAME}.herokuapp.com/callback
   ```

   注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱

## 測試範例成果

1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
2. 通過在控制台的 “Channel settings” 頁面上掃描 QR Code，將您的 Bot 添加到 LINE 的朋友中
3. 在 Line 上向您的 Bot 發送文字訊息，並確認它會學你說話



2. 顯示 app 日誌
   ```shell
   heroku logs --tail --app {HEROKU_APP_NAME}
   ```
   注意：{HEROKU_APP_NAME} 是上述步驟 2 中的應用名稱。
   ```shell
   --tail                     # 持續打印日誌
   --app {HEROKU_APP_NAME}    # 指定 App
   ```
## 使用GitHub Desktop上傳至GitHub
1. add existing repository
2. intial commit
3. push origin
4. 之後用fetch, push更新程式碼
## 程式檔案解說

> 資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行

- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件

### app.py

可透過修改程式裡的 handle_message() 方法內的程式碼來控制機器人的訊息回覆

![](https://i.imgur.com/DNeNbpV.png)

新版範例程式碼內附註解
如想更多了解此程式，可以去研究 Git、Python3、[Flask 套件](http://docs.jinkan.org/docs/flask/)、[Line bot sdk](https://github.com/line/line-bot-sdk-python)

### util.py

這裡是我實作的function，其中包括：
1. imagemap_message() -> 點擊圖片顯示聯絡資訊
2. TextSendMessage() -> 自我介紹
3. Carousel_Template() -> 顯示會的程式語言，可點結查詢網站、能力值
4. image_gallery() -> 顯示喜歡的東西（照片）

## 參考資源

### 影片

* https://www.youtube.com/watch?v=vsxZ_4sFWoU&t=6s
* https://www.youtube.com/watch?v=_6Kbkd9RWs8
* https://www.youtube.com/watch?v=fC9wg0DwHKQ&t=808s
* https://www.youtube.com/watch?v=TzZM1BtGPtM
* https://marketingliveincode.com/?p=3906

### 官方教學
* https://github.com/line/line-bot-sdk-python
* https://developers.line.biz/en/reference/messaging-api/#send-reply-message

### GitHub & ReadMe

* https://github.com/yaoandy107/line-bot-tutorial
* https://github.com/maso0310/linebot

```
