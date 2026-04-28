# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstanceInspectionRequest(DaraModel):
    def __init__(
        self,
        instance: str = None,
        items: List[str] = None,
        region: str = None,
        source: str = None,
    ):
        self.instance = instance
        self.items = items
        self.region = region
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['instance'] = self.instance

        if self.items is not None:
            result['items'] = self.items

        if self.region is not None:
            result['region'] = self.region

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

