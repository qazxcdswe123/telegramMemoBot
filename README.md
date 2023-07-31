# 迁移
现在memos已经内置了telegram bot，看了一下功能挺全的，可以考虑迁移过去，本项目估计不维护了

English | [中文](README.zh_CN.md)

# Telegram bot for the [Memos](https://github.com/usememos/memos) project

## Breaking changes

- Custom Telegram API endpoint is not supported anymore. Please use a server that can access Telegram services.

## Usage

1. Create a bot using [@BotFather](https://t.me/BotFather), and get your bot token.
2. Get your `chatid` from [@userinfobot](https://t.me/userinfobot)
3. Get your memos API URL.
4. Run the bot with the following command:

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="xxx" \
        -e CHAT_ID="yyy,YYY" \
        -e MEMO_API="zzz" \
        fwing/tgmemobot
```

- Hint: You can use multiple `CHAT_ID` by separating them with comma `,` (without space).
 
Example usage

```bash
docker run -d \
        --name tgmemobot \
        -e BOT_TOKEN="588859xyz:xyz" \
        -e CHAT_ID="470183200,1234" \
        -e MEMO_API="https://example.com/api/memo?openId=xyz" \
        fwing/tgmemobot
```

## Notice for China Mainland users

You will need a server that can access telegram services to run this bot.

## Special Thanks

- [FlomoBot](https://github.com/wogong/flomobot)
