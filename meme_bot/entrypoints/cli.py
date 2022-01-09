import click

from meme_bot.use_cases.post_message import PostMessageUseCase


@click.group()
def main():
    pass


@main.add_command
@click.command()
@click.argument("channel", required=True)
@click.argument("message", required=True)
def post_message(channel, message):
    uc = PostMessageUseCase()
    res = uc.execute()
