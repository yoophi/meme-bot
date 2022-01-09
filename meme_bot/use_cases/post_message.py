from typing import Union

from meme_bot.request_objects.post_message import PostMessageRequestObject
from meme_bot.shared.request import InvalidRequestObject
from meme_bot.shared.response import ResponseFailure, ResponseSuccess


class PostMessageUseCase:
    def execute(self, ro: Union[InvalidRequestObject, PostMessageRequestObject]):
        if not ro:
            return ResponseFailure.build_from_invalid_request_object(ro)

        return ResponseSuccess(True)
