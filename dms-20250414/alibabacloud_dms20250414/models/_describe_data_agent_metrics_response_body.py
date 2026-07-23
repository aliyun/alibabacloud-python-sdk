# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeDataAgentMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDataAgentMetricsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request is abnormal.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request failed.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDataAgentMetricsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDataAgentMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        metric_type: str = None,
        metrics: List[main_models.DescribeDataAgentMetricsResponseBodyDataMetrics] = None,
        start_time: int = None,
    ):
        # The end time of the query range.
        self.end_time = end_time
        # The metric type.
        self.metric_type = metric_type
        # The list of metrics.
        self.metrics = metrics
        # The start time of the query range.
        self.start_time = start_time

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeDataAgentMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDataAgentMetricsResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        metric_name: str = None,
        success: bool = None,
        value: str = None,
    ):
        # The error message returned when the call fails.
        self.error_message = error_message
        # The metric name.
        self.metric_name = metric_name
        # Indicates whether the request is successful.
        self.success = success
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.success is not None:
            result['Success'] = self.success

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

