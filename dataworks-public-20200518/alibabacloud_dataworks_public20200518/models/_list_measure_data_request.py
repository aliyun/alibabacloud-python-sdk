# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMeasureDataRequest(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        domain_code: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The metering component. Valid values:
        # 
        # *   Count: The number of DideAlarmPhone (telephone/call) alerts, and the number of DideAlarmSms (SMS/text message) alerts.
        # 
        # This parameter is required.
        self.component_code = component_code
        # The measurement item. Valid values:
        # 
        # *   DideAlarmPhone: phone call-based alerts
        # *   DideAlarmSms: text message-based alerts
        # 
        # This parameter is required.
        self.domain_code = domain_code
        # The end timestamp of the metering cycle, in milliseconds. The metering data is aggregated by day. The time range between EndTime and StartTime cannot exceed 30 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start timestamp of the metering cycle, in milliseconds. The metering data is aggregated by day. The time range between EndTime and StartTime cannot exceed 30 days.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

