# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class FirstRank(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: Any = None,
        name: str = None,
        type: str = None,
    ):
        self.active = active
        self.description = description
        self.meta = meta
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.description is not None:
            result['description'] = self.description

        if self.meta is not None:
            result['meta'] = self.meta

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

