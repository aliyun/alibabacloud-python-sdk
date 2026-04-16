# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CostTabDTO(DaraModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        model_types: List[str] = None,
    ):
        self.key = key
        self.label = label
        self.model_types = model_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.label is not None:
            result['label'] = self.label

        if self.model_types is not None:
            result['modelTypes'] = self.model_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        return self

