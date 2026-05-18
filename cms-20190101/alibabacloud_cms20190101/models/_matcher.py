# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Matcher(DaraModel):
    def __init__(
        self,
        label: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The name of the metric dimension.
        self.label = label
        # The matching mode of the metric dimension. Only EQUALS is supported. Default value: EQUALS.
        self.operator = operator
        # The value of the metric dimension.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

