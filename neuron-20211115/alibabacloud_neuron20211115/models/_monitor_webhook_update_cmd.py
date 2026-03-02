# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorWebhookUpdateCmd(DaraModel):
    def __init__(
        self,
        id: int = None,
        method: str = None,
        name: str = None,
        type: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.method = method
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

