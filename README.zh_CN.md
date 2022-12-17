[English](README.md) | Chinese

# [Memos](https://github.com/usememos/memos) 项目的 Telegram 机器人

## 使用方法

1. 使用 [@BotFather](https://t.me/BotFather) 创建一个机器人
2. **使用你喜欢的编辑器更新 `config.py` 文件！**
3. 使用 `pip3 install -r requirements.txt` 安装依赖
4. 使用 `python3 main.py` 运行机器人
5. Enjoy!

### 支持发送图片

你可以使用 `media_support_main.py` 来为你的机器人添加图片支持。

但是，由于 API 限制，似乎机器人只能逐条读取消息，含多个图片的信息将被视为多个单张图片，**所以带有多张图片的消息将导致多条 Memos**

我正在努力寻找更好的解决方案（2023 年），但是现在这是我能做到的最好的方案。

PRs are welcome!

### 支持 Docker

计划于 2023 年

## 中国大陆用户注意

你需要一个可以访问 Telegram 服务的服务器来运行这个机器人。

## 特别感谢

[FlomoBot](https://github.com/wogong/flomobot)