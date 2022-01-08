import click


@click.group()
def main():
    pass


@main.add_command
@click.command()
@click.argument('channel', required=True)
@click.argument('message', required=True)
def post_message(channel, message):
    click.echo('post-message')
    click.echo(f'channel={channel}')
    click.echo(f'message={message}')
