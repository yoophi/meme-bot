from meme_bot.request_objects.post_message import PostMessageRequestObject


def test_post_message_invalid_ro():
    ro = PostMessageRequestObject.from_dict({})
    assert bool(ro) is False


def test_post_message_valid_ro():
    ro = PostMessageRequestObject.from_dict(
        {"channel": "#my-channel", "message": "hello, world!"}
    )
    assert bool(ro) is True
    assert ro.channel == "#my-channel"
    assert ro.message == "hello, world!"
