# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAsyncChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
        session_created: bool = None,
        session_id: str = None,
        user_message_id: str = None,
    ):
        # The business status code. A value of 200 indicates success. A failure returns a backend error code (ERR.* or InvalidParameter.*).
        self.code = code
        # The error description. This is empty when the request succeeds.
        self.message = message
        # The assistant message ID. Use this ID to call streamChatMessage to subscribe to the generation results.
        self.message_id = message_id
        # The request trace ID.
        self.request_id = request_id
        # Indicates whether a new session was created by this call.
        self.session_created = session_created
        # The session ID. For continued sessions, this matches the input value. For new sessions, this is a server-generated value.
        self.session_id = session_id
        # The user message ID.
        self.user_message_id = user_message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_created is not None:
            result['sessionCreated'] = self.session_created

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_message_id is not None:
            result['userMessageId'] = self.user_message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionCreated') is not None:
            self.session_created = m.get('sessionCreated')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userMessageId') is not None:
            self.user_message_id = m.get('userMessageId')

        return self

