# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetResellerUserAlarmThresholdRequest(DaraModel):
    def __init__(
        self,
        alarm_thresholds: str = None,
        alarm_type: str = None,
        owner_id: int = None,
    ):
        self.alarm_thresholds = alarm_thresholds
        # This parameter is required.
        self.alarm_type = alarm_type
        # This parameter is required.
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_thresholds is not None:
            result['AlarmThresholds'] = self.alarm_thresholds

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmThresholds') is not None:
            self.alarm_thresholds = m.get('AlarmThresholds')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

