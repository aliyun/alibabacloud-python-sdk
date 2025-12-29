# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DataSourcePluginsValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        from_fields: str = None,
        parameters: Dict[str, str] = None,
    ):
        self.name = name
        self.from_fields = from_fields
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.from_fields is not None:
            result['fromFields'] = self.from_fields

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('fromFields') is not None:
            self.from_fields = m.get('fromFields')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

