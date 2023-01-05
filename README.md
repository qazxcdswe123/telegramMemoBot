English | [Chinese](README.zh_CN.md)

# Telegram bot for the [Memos](https://github.com/usememos/memos) project

## Usage

1. Create a bot using [@BotFather](https://t.me/BotFather)
2. Get your chatid with [@userinfobot](https://t.me/userinfobot)
3. Get your memos API URL.
4. Run the bot with the following command:

```bash
docker run -e BOT_TOKEN="xxx" -e CHAT_ID="yyy" -e MEMO_API="zzz" -d --name tgmemobot fwing/tgmemobot
```

Example usage

```bash
docker run -e BOT_TOKEN="588859xyz:xyz" -e CHAT_ID="xyz" -e MEMO_API="https://example.com/api/memo?openId=xyz" -d --name tgmemobot fwing/tgmemobot
```

### (Optional) Support for photos

```bash
docker run -e BOT_TOKEN="xxx" -e CHAT_ID="yyy" -e MEMO_API="zzz" -d --name tgmemobot fwing/tgmemobot:photos
```

You can use docker image `fwing/tgmemobot:photos` to support medias.

However, due to limited API, **message with multiple photos will be considered as multiple single photo message, which
leads to multiple text memos with only one message sent!** This may lead to undesired behaviour.

PRs are welcome!

## Notice for China Mainland users

You will need a server that can access telegram services to run this bot.

## Special Thanks

[FlomoBot](https://github.com/wogong/flomobot)