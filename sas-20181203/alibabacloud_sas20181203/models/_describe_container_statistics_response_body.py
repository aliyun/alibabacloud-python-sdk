# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeContainerStatisticsResponseBodyData = None,
        request_id: str = None,
    ):
        # The alert statistics of container assets.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeContainerStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        remind_alarm_count: int = None,
        serious_alarm_count: int = None,
        suspicious_alarm_count: int = None,
        total_alarm_count: int = None,
        total_node: int = None,
        has_risk_node: int = None,
    ):
        # The number of alerts whose risk level is **Reminder**.
        self.remind_alarm_count = remind_alarm_count
        # The number of alerts whose risk level is **Urgent**.
        self.serious_alarm_count = serious_alarm_count
        # The number of alerts whose risk level is **Suspicious**.
        self.suspicious_alarm_count = suspicious_alarm_count
        # The total number of alerts that are generated in the current container cluster.
        self.total_alarm_count = total_alarm_count
        # The total number of nodes in the current container cluster.
        self.total_node = total_node
        # The number of nodes on which alerts are generated in the current container cluster.
        self.has_risk_node = has_risk_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remind_alarm_count is not None:
            result['RemindAlarmCount'] = self.remind_alarm_count

        if self.serious_alarm_count is not None:
            result['SeriousAlarmCount'] = self.serious_alarm_count

        if self.suspicious_alarm_count is not None:
            result['SuspiciousAlarmCount'] = self.suspicious_alarm_count

        if self.total_alarm_count is not None:
            result['TotalAlarmCount'] = self.total_alarm_count

        if self.total_node is not None:
            result['TotalNode'] = self.total_node

        if self.has_risk_node is not None:
            result['hasRiskNode'] = self.has_risk_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemindAlarmCount') is not None:
            self.remind_alarm_count = m.get('RemindAlarmCount')

        if m.get('SeriousAlarmCount') is not None:
            self.serious_alarm_count = m.get('SeriousAlarmCount')

        if m.get('SuspiciousAlarmCount') is not None:
            self.suspicious_alarm_count = m.get('SuspiciousAlarmCount')

        if m.get('TotalAlarmCount') is not None:
            self.total_alarm_count = m.get('TotalAlarmCount')

        if m.get('TotalNode') is not None:
            self.total_node = m.get('TotalNode')

        if m.get('hasRiskNode') is not None:
            self.has_risk_node = m.get('hasRiskNode')

        return self

