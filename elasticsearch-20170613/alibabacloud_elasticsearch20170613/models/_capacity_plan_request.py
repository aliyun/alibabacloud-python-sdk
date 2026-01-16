# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CapacityPlanRequest(DaraModel):
    def __init__(
        self,
        complex_query_available: bool = None,
        data_info: List[main_models.CapacityPlanRequestDataInfo] = None,
        metric: List[main_models.CapacityPlanRequestMetric] = None,
        usage_scenario: str = None,
    ):
        # Indicates whether there is a need for complex aggregation queries. Options:
        # 
        # - true: Yes
        # - false (default): No
        self.complex_query_available = complex_query_available
        # Disk usage status.
        self.data_info = data_info
        # Metrics information including disk usage, search and write operations, aggregation requests, etc.
        self.metric = metric
        # Usage scenarios, options:
        # 
        # - general: General scenario
        # - analysisVisualization: Data analysis scenario
        # - dbAcceleration: Database acceleration scenario
        # - search: Search scenario
        # - log: Log scenario
        self.usage_scenario = usage_scenario

    def validate(self):
        if self.data_info:
            for v1 in self.data_info:
                 if v1:
                    v1.validate()
        if self.metric:
            for v1 in self.metric:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complex_query_available is not None:
            result['complexQueryAvailable'] = self.complex_query_available

        result['dataInfo'] = []
        if self.data_info is not None:
            for k1 in self.data_info:
                result['dataInfo'].append(k1.to_map() if k1 else None)

        result['metric'] = []
        if self.metric is not None:
            for k1 in self.metric:
                result['metric'].append(k1.to_map() if k1 else None)

        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complexQueryAvailable') is not None:
            self.complex_query_available = m.get('complexQueryAvailable')

        self.data_info = []
        if m.get('dataInfo') is not None:
            for k1 in m.get('dataInfo'):
                temp_model = main_models.CapacityPlanRequestDataInfo()
                self.data_info.append(temp_model.from_map(k1))

        self.metric = []
        if m.get('metric') is not None:
            for k1 in m.get('metric'):
                temp_model = main_models.CapacityPlanRequestMetric()
                self.metric.append(temp_model.from_map(k1))

        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')

        return self

class CapacityPlanRequestMetric(DaraModel):
    def __init__(
        self,
        average_qps: int = None,
        code: str = None,
        concurrent: int = None,
        peak_qps: int = None,
        response_time: int = None,
        throughput: int = None,
        type: str = None,
    ):
        # Average QPS.
        self.average_qps = average_qps
        # Search or write metric code. Options:
        # 
        # - write: Write
        # - search: Search
        self.code = code
        # Concurrent number.
        self.concurrent = concurrent
        # Peak QPS.
        self.peak_qps = peak_qps
        # Expected average response time, unit: milliseconds.
        self.response_time = response_time
        # Throughput, unit: MB/S.
        self.throughput = throughput
        # Search/write peak type. Options:
        # 
        # - common: Regular
        # - peak: Peak
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_qps is not None:
            result['averageQps'] = self.average_qps

        if self.code is not None:
            result['code'] = self.code

        if self.concurrent is not None:
            result['concurrent'] = self.concurrent

        if self.peak_qps is not None:
            result['peakQps'] = self.peak_qps

        if self.response_time is not None:
            result['responseTime'] = self.response_time

        if self.throughput is not None:
            result['throughput'] = self.throughput

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageQps') is not None:
            self.average_qps = m.get('averageQps')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('concurrent') is not None:
            self.concurrent = m.get('concurrent')

        if m.get('peakQps') is not None:
            self.peak_qps = m.get('peakQps')

        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')

        if m.get('throughput') is not None:
            self.throughput = m.get('throughput')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CapacityPlanRequestDataInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        size: int = None,
        total_count: int = None,
        type: str = None,
        unit: str = None,
    ):
        # Disk data metric code. Options:
        # 
        # - totalRawData: Raw data information
        # - document: Data document information, estimated document count
        # - dailyIncrement: Daily data growth
        # - dailyIncrementDoc: Daily incremental document count
        # - retentionTime: Data retention period
        # - replica: Replica settings
        self.code = code
        # Disk usage metric value.
        self.size = size
        # Total number of data entries.
        self.total_count = total_count
        # Disk data type. Options:
        # 
        # - hot: Hot data
        # - warm: Cold data
        self.type = type
        # Data or time unit. Options:
        # 
        # - Data units: MiB, GiB, TB, PB
        # - Time units: DAYS, WEEKS, MONTHS, YEARS
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.size is not None:
            result['size'] = self.size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

