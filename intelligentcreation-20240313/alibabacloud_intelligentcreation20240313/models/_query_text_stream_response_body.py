# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTextStreamResponseBody(DaraModel):
    def __init__(
        self,
        end: bool = None,
        index: int = None,
        message: str = None,
        type: int = None,
    ):
        self.end = end
        self.index = index
        # Id of the request
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

