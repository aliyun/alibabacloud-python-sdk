# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KopilotChatStreamResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        delta: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
        role: str = None,
        run_id: str = None,
        thread_id: str = None,
        tool_call_id: str = None,
        tool_call_name: str = None,
        type: str = None,
    ):
        self.content = content
        self.delta = delta
        self.message = message
        self.message_id = message_id
        self.request_id = request_id
        self.role = role
        self.run_id = run_id
        self.thread_id = thread_id
        self.tool_call_id = tool_call_id
        self.tool_call_name = tool_call_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.delta is not None:
            result['Delta'] = self.delta

        if self.message is not None:
            result['Message'] = self.message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.tool_call_id is not None:
            result['ToolCallId'] = self.tool_call_id

        if self.tool_call_name is not None:
            result['ToolCallName'] = self.tool_call_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Delta') is not None:
            self.delta = m.get('Delta')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('ToolCallId') is not None:
            self.tool_call_id = m.get('ToolCallId')

        if m.get('ToolCallName') is not None:
            self.tool_call_name = m.get('ToolCallName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

