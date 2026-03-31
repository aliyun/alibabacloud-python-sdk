# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateMmsDataSourceRequest(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
        networklink: str = None,
        type: str = None,
    ):
        self.config = config
        self.name = name
        self.networklink = networklink
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.name is not None:
            result['name'] = self.name

        if self.networklink is not None:
            result['networklink'] = self.networklink

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networklink') is not None:
            self.networklink = m.get('networklink')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

