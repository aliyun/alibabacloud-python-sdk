# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatContentResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        checkpoint: int = None,
        content: str = None,
        content_type: str = None,
        event_type: str = None,
        level: int = None,
        timestamp: str = None,
    ):
        # The category of the message, which helps parse the `content` field when it is a JSON object. For example,`PLAN` indicates that the message is an execution plan and conforms to the execution plan schema.
        self.category = category
        # The checkpoint value.
        self.checkpoint = checkpoint
        # The message content.
        self.content = content
        # The type of the content field. Valid values: `[str, json]`. If the value is `json`, the content field can be parsed as a JSON object.
        self.content_type = content_type
        # The message type, which distinguishes control signals from message data. For example,`CHAT_START` indicates the start of an agent\\"s reply,`CHAT_FINISH` indicates the end of the reply,`DATA` indicates a message that contains content, and`DELTA` indicates a part of an incremental output.
        self.event_type = event_type
        # The output level of the message. A higher value indicates greater importance.
        self.level = level
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.event_type is not None:
            result['event_type'] = self.event_type

        if self.level is not None:
            result['level'] = self.level

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

