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
        # The dimension key name of the APM query filter condition. Specifies which dimension to filter by, such as hostname or service name.
        # 
        # This parameter is required.
        self.key = key
        # The matching type of the APM query filter condition. Valid values:
        # - ALL: Matches all values.
        # - EQ: Exact match.
        # - NE: Not equal to.
        # - DISABLED: Disables the filter condition.
        # 
        # This parameter is required.
        self.type = type
        # The filter value. Can be empty when type is set to ALL or DISABLED.
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

