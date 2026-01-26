# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeAlarmSeverityRequest(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        handler_id: int = None,
        region_id: str = None,
        severity: str = None,
    ):
        # The ID of the alert.
        # 
        # For more information about how to obtain the ID of an alert, see [ListAlertEvents](https://help.aliyun.com/document_detail/2612346.html).
        # 
        # This parameter is required.
        self.alarm_id = alarm_id
        # The ID of the handler.
        self.handler_id = handler_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The severity level of the alert. Valid values: P1, P2, P3, and P4. P4 indicates the lowest severity, whereas P1 indicates the highest severity.
        # 
        # This parameter is required.
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.handler_id is not None:
            result['HandlerId'] = self.handler_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('HandlerId') is not None:
            self.handler_id = m.get('HandlerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

