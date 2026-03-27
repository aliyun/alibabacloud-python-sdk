# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class UpsertUmodelDataRequest(DaraModel):
    def __init__(
        self,
        elements: List[Any] = None,
        method: str = None,
    ):
        # Element content
        self.elements = elements
        # Method
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elements is not None:
            result['elements'] = self.elements

        if self.method is not None:
            result['method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elements') is not None:
            self.elements = m.get('elements')

        if m.get('method') is not None:
            self.method = m.get('method')

        return self

