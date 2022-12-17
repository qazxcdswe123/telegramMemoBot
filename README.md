English | [Chinese](README.zh_CN.md)

# Telegram bot for the [Memos](https://github.com/usememos/memos) project

## Usage

1. Create a bot using [@BotFather](https://t.me/BotFather)
2. **Update the `config.py` file with your favorite editor!**
3. Install the dependencies using `pip3 install -r requirements.txt`
4. Run the bot using `python3 main.py`
5. Enjoy!

### Support for medias (photos)

You can use `media_support_main.py` to add photos support to your bot.

However, due to limited API, **message with multiple photos will be considered as multiple single photo message which
leads to multiple text memos!** This may lead to undesired behaviour.

I'm still working on a better solution(in 2023), but for now this is the best I can do.

PRs are welcome!

### Support for docker

Planned in 2023

## Notice for China Mainland users

You will need a server that can access telegram services to run this bot.

## Special Thanks

[FlomoBot](https://github.com/wogong/flomobot)