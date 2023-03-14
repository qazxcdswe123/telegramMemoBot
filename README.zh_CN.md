[English](README.md) | Chinese

# [Memos](https://github.com/usememos/memos) 项目的 Telegram 机器人

## 破坏性更新

- 图片发送现在使用环境变量 `INCLUDE_PHOTO` 来控制，而不是使用 `photos` 标签的镜像。

## 使用方法

1. 使用 [@BotFather](https://t.me/BotFather) 创建一个机器人，获取你的 bot token.
2. 使用 [@userinfobot](https://t.me/userinfobot) 获取你的 chatid
3. 获取你的 Memos API URL
4. 使用以下命令运行机器人

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="xxx" \
        -e CHAT_ID="yyy" \
        -e MEMO_API="zzz" \
        fwing/tgmemobot
```

例如：

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="588859xyz:xyz" \
        -e CHAT_ID="470183200" \
        -e MEMO_API="https://example.com/api/memo?openId=xyz" \
        fwing/tgmemobot
```

### （可选）支持发送图片

添加 `INCLUDE_PHOTO=True` 到环境变量来启用图片支持。

```bash
docker run -d \
        --name tgmemobot \
        -e INCLUDE_PHOTO=True \
......
```

但是，由于 API 的限制，**含有多张图片的消息会被当作多条单张图片的消息，导致一条信息会创建多条 Memos！** 这可能不是你想要的。

PRs are welcome!

### （可选）自定义 Telegram API 反代地址

设置 `TG_API_URL` 环境变量来使用自定义的 Telegram API 反代地址。

例如

```bash
docker run -d \
          --name tgmemobot \
          -e TG_API_URL="https://workers.dev/bot" \
......
```



## 中国大陆用户注意

你需要一个可以访问 Telegram 服务的服务器来运行这个机器人。或者使用反代 API。

## 特别感谢

[FlomoBot](https://github.com/wogong/flomobot)