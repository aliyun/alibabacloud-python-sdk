# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class LlmStreamChatRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        messages: Any = None,
        temperature: float = None,
        top_p: float = None,
        type: str = None,
    ):
        self.channel = channel
        # Conversation information
        self.messages = messages
        # Temperature value for the large model
        self.temperature = temperature
        # Top p parameter controlling the randomness of the large model\\"s output.
        self.top_p = top_p
        # Type of conversation
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.messages is not None:
            result['Messages'] = self.messages

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Messages') is not None:
            self.messages = m.get('Messages')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

