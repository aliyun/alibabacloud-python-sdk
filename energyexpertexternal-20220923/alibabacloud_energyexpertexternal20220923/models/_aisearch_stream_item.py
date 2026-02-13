# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class AISearchStreamItem(DaraModel):
    def __init__(
        self,
        content: str = None,
        params: Any = None,
        type: str = None,
    ):
        self.content = content
        self.params = params
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.params is not None:
            result['params'] = self.params

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

