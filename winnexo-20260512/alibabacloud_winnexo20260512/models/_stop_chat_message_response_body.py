# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        finish_reason: str = None,
        message: str = None,
        message_id: str = None,
        partial_content: str = None,
        request_id: str = None,
        session_id: str = None,
        status: str = None,
    ):
        # The status code.
        self.code = code
        # The reason for stopping.
        self.finish_reason = finish_reason
        # The description of the status code.
        self.message = message
        # The message ID.
        self.message_id = message_id
        # The partially generated content.
        self.partial_content = partial_content
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_id = session_id
        # The final status of the message.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.partial_content is not None:
            result['partialContent'] = self.partial_content

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('partialContent') is not None:
            self.partial_content = m.get('partialContent')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

