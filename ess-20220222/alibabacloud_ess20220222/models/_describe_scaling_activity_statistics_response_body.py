# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingActivityStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_error_code_statistics: main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatistics = None,
        scaling_activity_status_statistics: main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatistics = None,
    ):
        self.request_id = request_id
        self.scaling_activity_error_code_statistics = scaling_activity_error_code_statistics
        self.scaling_activity_status_statistics = scaling_activity_status_statistics

    def validate(self):
        if self.scaling_activity_error_code_statistics:
            self.scaling_activity_error_code_statistics.validate()
        if self.scaling_activity_status_statistics:
            self.scaling_activity_status_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_activity_error_code_statistics is not None:
            result['ScalingActivityErrorCodeStatistics'] = self.scaling_activity_error_code_statistics.to_map()

        if self.scaling_activity_status_statistics is not None:
            result['ScalingActivityStatusStatistics'] = self.scaling_activity_status_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingActivityErrorCodeStatistics') is not None:
            temp_model = main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatistics()
            self.scaling_activity_error_code_statistics = temp_model.from_map(m.get('ScalingActivityErrorCodeStatistics'))

        if m.get('ScalingActivityStatusStatistics') is not None:
            temp_model = main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatistics()
            self.scaling_activity_status_statistics = temp_model.from_map(m.get('ScalingActivityStatusStatistics'))

        return self

class DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatistics(DaraModel):
    def __init__(
        self,
        statistic: List[main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatisticsStatistic] = None,
    ):
        self.statistic = statistic

    def validate(self):
        if self.statistic:
            for v1 in self.statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Statistic'] = []
        if self.statistic is not None:
            for k1 in self.statistic:
                result['Statistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k1 in m.get('Statistic'):
                temp_model = main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k1))

        return self

class DescribeScalingActivityStatisticsResponseBodyScalingActivityStatusStatisticsStatistic(DaraModel):
    def __init__(
        self,
        failed_activity_count: int = None,
        success_activity_count: int = None,
        time: str = None,
        warning_activity_count: int = None,
    ):
        self.failed_activity_count = failed_activity_count
        self.success_activity_count = success_activity_count
        self.time = time
        self.warning_activity_count = warning_activity_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_activity_count is not None:
            result['FailedActivityCount'] = self.failed_activity_count

        if self.success_activity_count is not None:
            result['SuccessActivityCount'] = self.success_activity_count

        if self.time is not None:
            result['Time'] = self.time

        if self.warning_activity_count is not None:
            result['WarningActivityCount'] = self.warning_activity_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedActivityCount') is not None:
            self.failed_activity_count = m.get('FailedActivityCount')

        if m.get('SuccessActivityCount') is not None:
            self.success_activity_count = m.get('SuccessActivityCount')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('WarningActivityCount') is not None:
            self.warning_activity_count = m.get('WarningActivityCount')

        return self

class DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatistics(DaraModel):
    def __init__(
        self,
        error_statistic: List[main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatisticsErrorStatistic] = None,
    ):
        self.error_statistic = error_statistic

    def validate(self):
        if self.error_statistic:
            for v1 in self.error_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorStatistic'] = []
        if self.error_statistic is not None:
            for k1 in self.error_statistic:
                result['ErrorStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_statistic = []
        if m.get('ErrorStatistic') is not None:
            for k1 in m.get('ErrorStatistic'):
                temp_model = main_models.DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatisticsErrorStatistic()
                self.error_statistic.append(temp_model.from_map(k1))

        return self

class DescribeScalingActivityStatisticsResponseBodyScalingActivityErrorCodeStatisticsErrorStatistic(DaraModel):
    def __init__(
        self,
        count: int = None,
        error_code: str = None,
        time: str = None,
    ):
        self.count = count
        self.error_code = error_code
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

