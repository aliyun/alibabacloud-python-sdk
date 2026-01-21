# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Incident(DaraModel):
    def __init__(
        self,
        action_time: int = None,
        alert_count: int = None,
        end_time: int = None,
        grouping_data: Dict[str, Any] = None,
        grouping_id: str = None,
        grouping_key: str = None,
        incident_id: str = None,
        incident_status: str = None,
        severity: str = None,
        start_time: int = None,
        strategy_uuid: str = None,
        user_id: str = None,
    ):
        self.action_time = action_time
        self.alert_count = alert_count
        self.end_time = end_time
        self.grouping_data = grouping_data
        self.grouping_id = grouping_id
        self.grouping_key = grouping_key
        self.incident_id = incident_id
        self.incident_status = incident_status
        self.severity = severity
        self.start_time = start_time
        self.strategy_uuid = strategy_uuid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_time is not None:
            result['ActionTime'] = self.action_time

        if self.alert_count is not None:
            result['AlertCount'] = self.alert_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.grouping_data is not None:
            result['GroupingData'] = self.grouping_data

        if self.grouping_id is not None:
            result['GroupingId'] = self.grouping_id

        if self.grouping_key is not None:
            result['GroupingKey'] = self.grouping_key

        if self.incident_id is not None:
            result['IncidentId'] = self.incident_id

        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.strategy_uuid is not None:
            result['StrategyUuid'] = self.strategy_uuid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')

        if m.get('AlertCount') is not None:
            self.alert_count = m.get('AlertCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupingData') is not None:
            self.grouping_data = m.get('GroupingData')

        if m.get('GroupingId') is not None:
            self.grouping_id = m.get('GroupingId')

        if m.get('GroupingKey') is not None:
            self.grouping_key = m.get('GroupingKey')

        if m.get('IncidentId') is not None:
            self.incident_id = m.get('IncidentId')

        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StrategyUuid') is not None:
            self.strategy_uuid = m.get('StrategyUuid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

