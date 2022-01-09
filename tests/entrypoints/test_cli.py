from click.testing import CliRunner

from meme_bot.entrypoints.cli import main
from meme_bot.use_cases.post_message import PostMessageUseCase


def test_meme_bot_cli(mocker):
    mock_execute = mocker.patch.object(PostMessageUseCase, "execute")
    runner = CliRunner()
    result = runner.invoke(main, ["post-message", "channel", "message"])
    mock_execute.assert_called()
    # assert result.exit_code == 0
    # assert result.output == 'post-message\nchannel=channel\nmessage=message\n'
