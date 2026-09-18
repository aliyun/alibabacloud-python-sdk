# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class SendChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
        work_mode: str = None,
    ):
        # The error code.
        self.code = code
        # The streaming response content.
        self.content = content
        # The SSE event stream payload. On success, the response is a text/event-stream raw frame that must be consumed frame by frame in streaming mode.
        self.data = data
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The event type.
        self.type = type
        # The session work mode that takes effect for the current turn. Valid values:
        # - ask: Quick Q&A.
        # - work: Deep work.
        # - direct: Direct connection (request-level).
        # 
        # In multi-digital-employee or task execution scenarios, if ask is provided, work takes effect instead.
        self.work_mode = work_mode

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

        if self.work_mode is not None:
            result['workMode'] = self.work_mode

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

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

        return self

