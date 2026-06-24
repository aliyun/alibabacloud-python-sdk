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
        # Specifies whether complex aggregate query is required. Valid values:
        # 
        # - true: Required.
        # - false (default): Not required.
        self.complex_query_available = complex_query_available
        # The disk usage information.
        self.data_info = data_info
        # The metric information, including disk usage, search and write operations, and aggregation requests.
        self.metric = metric
        # Scenarios. Valid values:
        # 
        # - general: general-purpose scenario
        # - analysisVisualization: data analytics scenario
        # - dbAcceleration: database acceleration scenario
        # - search: search scenario
        # - log: log scenario.
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
        # The average QPS.
        self.average_qps = average_qps
        # The search or write metric code. Valid values:
        # 
        # - write: write
        # - search: search.
        self.code = code
        # The number of concurrent connections.
        self.concurrent = concurrent
        # The peak QPS.
        self.peak_qps = peak_qps
        # The expected average response time, in milliseconds.
        self.response_time = response_time
        # The throughput, in MB/s.
        self.throughput = throughput
        # The search or write peak type. Valid values:
        # 
        # - common: normal
        # - peak: peak.
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
        # The disk data metric code. Valid values:
        # 
        # - totalRawData: source data information
        # - document: data document information, estimated number of documents
        # - dailyIncrement: daily data growth
        # - dailyIncrement: daily incremental documents
        # - retentionTime: data retention period
        # - replica: replica settings.
        self.code = code
        # The metric value of disk usage.
        self.size = size
        # The total number of data entries.
        self.total_count = total_count
        # The disk data type. Valid values:
        # 
        # - hot: hot data
        # - warm: warm data.
        self.type = type
        # The data unit or time unit. Valid values:
        # 
        # - Data units: MiB, GiB, TB, PB
        # - Time units: DAYS, WEEKS, MONTHS, YEARS.
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

