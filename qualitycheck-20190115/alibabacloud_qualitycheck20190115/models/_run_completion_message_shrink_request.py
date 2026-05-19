# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunCompletionMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        messages_shrink: str = None,
        model_code: str = None,
        stream: bool = None,
    ):
        self.messages_shrink = messages_shrink
        self.model_code = model_code
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.messages_shrink is not None:
            result['Messages'] = self.messages_shrink

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages_shrink = m.get('Messages')

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

