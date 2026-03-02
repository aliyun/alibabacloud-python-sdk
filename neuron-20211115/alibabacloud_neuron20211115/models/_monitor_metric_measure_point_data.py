# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorMetricMeasurePointData(DaraModel):
    def __init__(
        self,
        measure: str = None,
        time_stamp: str = None,
        value: str = None,
        value_with_unit: str = None,
    ):
        self.measure = measure
        self.time_stamp = time_stamp
        self.value = value
        self.value_with_unit = value_with_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.measure is not None:
            result['measure'] = self.measure

        if self.time_stamp is not None:
            result['timeStamp'] = self.time_stamp

        if self.value is not None:
            result['value'] = self.value

        if self.value_with_unit is not None:
            result['valueWithUnit'] = self.value_with_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('measure') is not None:
            self.measure = m.get('measure')

        if m.get('timeStamp') is not None:
            self.time_stamp = m.get('timeStamp')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueWithUnit') is not None:
            self.value_with_unit = m.get('valueWithUnit')

        return self

