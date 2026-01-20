# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FeatureViewConfigValuePartitionsValue(DaraModel):
    def __init__(
        self,
        value: str = None,
        values: List[str] = None,
        start_value: str = None,
        end_value: str = None,
    ):
        self.value = value
        self.values = values
        self.start_value = start_value
        self.end_value = end_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        if self.values is not None:
            result['Values'] = self.values

        if self.start_value is not None:
            result['StartValue'] = self.start_value

        if self.end_value is not None:
            result['EndValue'] = self.end_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        if m.get('StartValue') is not None:
            self.start_value = m.get('StartValue')

        if m.get('EndValue') is not None:
            self.end_value = m.get('EndValue')

        return self

