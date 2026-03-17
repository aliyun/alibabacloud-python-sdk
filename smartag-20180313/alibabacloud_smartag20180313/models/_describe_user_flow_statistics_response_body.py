# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeUserFlowStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sag_statistics: main_models.DescribeUserFlowStatisticsResponseBodySagStatistics = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.sag_statistics = sag_statistics

    def validate(self):
        if self.sag_statistics:
            self.sag_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sag_statistics is not None:
            result['SagStatistics'] = self.sag_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SagStatistics') is not None:
            temp_model = main_models.DescribeUserFlowStatisticsResponseBodySagStatistics()
            self.sag_statistics = temp_model.from_map(m.get('SagStatistics'))

        return self

class DescribeUserFlowStatisticsResponseBodySagStatistics(DaraModel):
    def __init__(
        self,
        statistics: List[main_models.DescribeUserFlowStatisticsResponseBodySagStatisticsStatistics] = None,
    ):
        self.statistics = statistics

    def validate(self):
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.DescribeUserFlowStatisticsResponseBodySagStatisticsStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class DescribeUserFlowStatisticsResponseBodySagStatisticsStatistics(DaraModel):
    def __init__(
        self,
        total_bytes: str = None,
        total_leave_bytes: str = None,
        user_name: str = None,
    ):
        self.total_bytes = total_bytes
        self.total_leave_bytes = total_leave_bytes
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.total_leave_bytes is not None:
            result['TotalLeaveBytes'] = self.total_leave_bytes

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalLeaveBytes') is not None:
            self.total_leave_bytes = m.get('TotalLeaveBytes')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

