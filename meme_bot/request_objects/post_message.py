from dataclasses import dataclass

from meme_bot.shared.request import ValidRequestObject, InvalidRequestObject


@dataclass
class PostMessageRequestObject(ValidRequestObject):
    channel: str
    message: str

    @classmethod
    def from_dict(cls, params):
        invalid_ro = InvalidRequestObject()
        channel = params.get("channel")
        message = params.get("message")

        if not channel:
            invalid_ro.add_error("channel", "`channel` cannot be empty")
        if not message:
            invalid_ro.add_error("message", "`message` cannot be empty")

        if invalid_ro.has_errors():
            return invalid_ro

        return cls(channel=channel, message=message)
