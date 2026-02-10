# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClusterSuspEventStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        susp_statistics: main_models.GetClusterSuspEventStatisticsResponseBodySuspStatistics = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of alerts by risk level.
        self.susp_statistics = susp_statistics

    def validate(self):
        if self.susp_statistics:
            self.susp_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.susp_statistics is not None:
            result['SuspStatistics'] = self.susp_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuspStatistics') is not None:
            temp_model = main_models.GetClusterSuspEventStatisticsResponseBodySuspStatistics()
            self.susp_statistics = temp_model.from_map(m.get('SuspStatistics'))

        return self

class GetClusterSuspEventStatisticsResponseBodySuspStatistics(DaraModel):
    def __init__(
        self,
        remind: int = None,
        serious: int = None,
        suspicious: int = None,
    ):
        # The number of alerts whose Emergency level is Reminder.
        self.remind = remind
        # The number of alerts whose Emergency level is Urgent.
        self.serious = serious
        # The number of alerts whose Emergency level is Suspicious.
        self.suspicious = suspicious

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remind is not None:
            result['Remind'] = self.remind

        if self.serious is not None:
            result['Serious'] = self.serious

        if self.suspicious is not None:
            result['Suspicious'] = self.suspicious

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remind') is not None:
            self.remind = m.get('Remind')

        if m.get('Serious') is not None:
            self.serious = m.get('Serious')

        if m.get('Suspicious') is not None:
            self.suspicious = m.get('Suspicious')

        return self

