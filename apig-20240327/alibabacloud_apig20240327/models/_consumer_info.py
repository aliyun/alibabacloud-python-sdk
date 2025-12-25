# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumerInfo(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        enable: bool = None,
        name: str = None,
    ):
        self.consumer_id = consumer_id
        self.enable = enable
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.enable is not None:
            result['enable'] = self.enable

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

