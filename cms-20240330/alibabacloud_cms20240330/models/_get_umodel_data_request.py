# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetUmodelDataRequest(DaraModel):
    def __init__(
        self,
        content: Any = None,
        method: str = None,
    ):
        # Query conditions
        self.content = content
        # Method
        # 
        # This parameter is required.
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.method is not None:
            result['method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('method') is not None:
            self.method = m.get('method')

        return self

