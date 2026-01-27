# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthReportInterval(DaraModel):
    def __init__(
        self,
        time_unit: str = None,
        value: int = None,
    ):
        self.time_unit = time_unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

