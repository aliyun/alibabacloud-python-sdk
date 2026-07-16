# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApmFilterConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The tag key to filter by. For example, to filter traces by region, set this parameter to `RegionId`.
        # 
        # This parameter is required.
        self.key = key
        # The comparison operator used to match the tag\\"s value. Valid values: `EQUAL` and `NOT_EQUAL`.
        # 
        # This parameter is required.
        self.type = type
        # The value to compare against the tag\\"s value. Used with the `key` and `type` parameters to form a complete filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

