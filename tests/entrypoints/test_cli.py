from click.testing import CliRunner

from meme_bot.entrypoints.cli import main


def test_meme_bot_cli():
    runner = CliRunner()
    result = runner.invoke(main, ['post-message', 'channel', 'message'])
    assert result.exit_code == 0
    assert result.output == 'post-message\nchannel=channel\nmessage=message\n'
