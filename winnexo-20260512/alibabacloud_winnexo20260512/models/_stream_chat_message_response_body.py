# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class StreamChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # The error code.
        self.code = code
        # The incremental content of the current SSE frame.
        self.content = content
        # The SSE event stream payload. On success, the response is returned as raw text/event-stream frames that must be consumed frame by frame in streaming mode.
        self.data = data
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The SSE event type, such as text, think, heartbeat, done, or error.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.data is not None:
            result['data'] = self.data

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

