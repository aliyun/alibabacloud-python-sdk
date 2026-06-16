# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContinuousStrategy(DaraModel):
    def __init__(
        self,
        data_delay_minutes: int = None,
        enabled: bool = None,
        interval_unit: str = None,
        interval_value: int = None,
    ):
        self.data_delay_minutes = data_delay_minutes
        self.enabled = enabled
        self.interval_unit = interval_unit
        self.interval_value = interval_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_delay_minutes is not None:
            result['dataDelayMinutes'] = self.data_delay_minutes

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.interval_unit is not None:
            result['intervalUnit'] = self.interval_unit

        if self.interval_value is not None:
            result['intervalValue'] = self.interval_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataDelayMinutes') is not None:
            self.data_delay_minutes = m.get('dataDelayMinutes')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('intervalUnit') is not None:
            self.interval_unit = m.get('intervalUnit')

        if m.get('intervalValue') is not None:
            self.interval_value = m.get('intervalValue')

        return self

