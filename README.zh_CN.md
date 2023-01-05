[English](README.md) | Chinese

# [Memos](https://github.com/usememos/memos) 项目的 Telegram 机器人

## 使用方法

1. 使用 [@BotFather](https://t.me/BotFather) 创建一个机器人
2. 使用 [@userinfobot](https://t.me/userinfobot) 获取你的 chatid
3. 获取你的 Memos API URL
4. 使用以下命令运行机器人

```bash
docker run -e BOT_TOKEN="xxx" -e CHAT_ID="yyy" -e MEMO_API="zzz" -d --name tgmemobot fwing/tgmemobot
```

例如：

```bash
docker run -e BOT_TOKEN="588859xyz:xyz" -e CHAT_ID="xyz" -e MEMO_API="https://example.com/api/memo?openId=xyz" -d --name tgmemobot fwing/tgmemobot
```

### （非默认）支持发送图片

```bash
docker run -e BOT_TOKEN="xxx" -e CHAT_ID="yyy" -e MEMO_API="zzz" -d --name tgmemobot fwing/tgmemobot:photos
```

如上，你可以使用 `fwing/tgmemobot:photos` 镜像来支持发送图片到 Memos。

但是，由于 API 的限制，**含有多张图片的消息会被当作多条单张图片的消息，导致一条信息会创建多条 Memos！** 这可能不是你想要的。

PRs are welcome!

## 中国大陆用户注意

你需要一个可以访问 Telegram 服务的服务器来运行这个机器人。

## 特别感谢

[FlomoBot](https://github.com/wogong/flomobot)