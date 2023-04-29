[English](README.md) | Chinese

# [Memos](https://github.com/usememos/memos) 项目的 Telegram 机器人

## 破坏性更新

- 不再支持自定义 Telegram API 反代地址。请使用一个可以访问 Telegram 服务的服务器。

## 使用方法

1. 使用 [@BotFather](https://t.me/BotFather) 创建一个机器人，获取你的 bot token.
2. 使用 [@userinfobot](https://t.me/userinfobot) 获取你的 chatid
3. 获取你的 Memos API URL
4. 使用以下命令运行机器人

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="xxx" \
        -e CHAT_ID="yyy,YYY" \
        -e MEMO_API="zzz" \
        fwing/tgmemobot
```

- 提示：你可以使用逗号 `,`（不要有空格）分隔多个 `CHAT_ID`。

例如：

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="588859xyz:xyz" \
        -e CHAT_ID="470183200,1234" \
        -e MEMO_API="https://example.com/api/memo?openId=xyz" \
        fwing/tgmemobot
```

## 中国大陆用户注意

你需要一个可以访问 Telegram 服务的服务器来运行这个机器人。

## 特别感谢

[FlomoBot](https://github.com/wogong/flomobot)