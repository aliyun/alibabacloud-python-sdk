# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumerGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
        order: bool = None,
        timeout: int = None,
    ):
        self.name = name
        self.order = order
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.order is not None:
            result['order'] = self.order

        if self.timeout is not None:
            result['timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        return self

