# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        metric_data: main_models.ListResourceGroupMetricDataResponseBodyMetricData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Monitoring metric data.
        self.metric_data = metric_data
        # The request ID, used for locating logs and troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricData') is not None:
            temp_model = main_models.ListResourceGroupMetricDataResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m.get('MetricData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListResourceGroupMetricDataResponseBodyMetricData(DaraModel):
    def __init__(
        self,
        id: str = None,
        metric_name: str = None,
        metrics: List[main_models.ListResourceGroupMetricDataResponseBodyMetricDataMetrics] = None,
        next_token: str = None,
    ):
        # The unique identifier for the resource group.
        self.id = id
        # The metric name. Valid values:
        # 
        # *   CUSpec: Maximum CU capacity of the resource group, in CUs.
        # *   CUUsage: CU usage of the resource group, in CUs.
        # *   CUUtilization: CU utilization of the resource group, in %.
        # *   SlotSpec: Maximum number of concurrent slots for resource group scheduling, in slots.
        # *   SlotUsage: Used concurrency for resource group scheduling, in slots.
        # *   SchedulerCUMaxSpec: Maximum CU quota for data computing, in CUs.
        # *   SchedulerCUUsage: CU usage for data computing, in CUs.
        # *   SchedulerCUMinSpec: Minimum guaranteed CUs for data computing, in CUs.
        # *   DataIntegrationCUMaxSpec: Maximum CU quota for Data Integration, in CUs.
        # *   DataIntegrationCUUsage: CU usage for Data Integration, in CUs.
        # *   DataIntegrationCUMinSpec: Minimum guaranteed CUs for Data Integration, in CUs.
        # *   DataServiceCUMaxSpec: Maximum CU quota for DataService Studio, in CUs.
        # *   DataServiceCUUsage: CU usage for DataService Studio, in CUs.
        # *   DataServiceCUMinSpec: Minimum guaranteed CUs for DataService Studio, in CUs.
        # *   ServerIdeCUMaxSpec: Maximum CU quota for personal development environment, in CUs.
        # *   ServerIdeCUUsage: CU usage for personal development environment, in CUs.
        # *   ServerIdeCUMinSpec: Minimum guaranteed CUs for personal development environment, in CUs.
        self.metric_name = metric_name
        # The list of metric data.
        self.metrics = metrics
        # The pagination cursor.
        self.next_token = next_token

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.ListResourceGroupMetricDataResponseBodyMetricDataMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListResourceGroupMetricDataResponseBodyMetricDataMetrics(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        value: float = None,
    ):
        # The timestamp.
        self.timestamp = timestamp
        # The value of the metric data.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

