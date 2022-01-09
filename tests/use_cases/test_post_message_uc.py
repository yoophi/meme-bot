from meme_bot.request_objects.post_message import PostMessageRequestObject
from meme_bot.shared.request import InvalidRequestObject
from meme_bot.shared.response import ResponseFailure, ResponseSuccess
from meme_bot.use_cases.post_message import PostMessageUseCase


def test_post_message_uc_fail():
    uc = PostMessageUseCase()
    ro = InvalidRequestObject()
    res = uc.execute(ro)
    assert isinstance(res, ResponseFailure)


def test_post_message_uc_success():
    uc = PostMessageUseCase()
    ro = PostMessageRequestObject.from_dict(
        {"channel": "#my-channel", "message": "hello, world!"}
    )
    res = uc.execute(ro)
    assert isinstance(res, ResponseSuccess)
