# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_points: List[main_models.DescribeMetricListResponseBodyDataPoints] = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        metric_name: str = None,
        metric_type: str = None,
        param: str = None,
        period: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned by the backend service. The number is incremented.
        self.code = code
        # The monitoring statistics.
        self.data_points = data_points
        # The dynamic part in the error message. This parameter is used to replace the %s variable in the **ErrMessage** parameter.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code returned for an exception.
        self.http_status_code = http_status_code
        # *   **InternetOut**: the outbound traffic over the Internet. Unit: byte.
        # *   **diskusage_utilization**: the disk usage.
        # *   **IntranetInRate**: the inbound traffic over the internal network. Unit: byte.
        # *   **InternetIn**: the inbound traffic from the Internet. Unit: byte.
        # *   **cpu_total**: the CPU utilization.
        # *   **memory_usedutilization**: the memory usage.
        # *   **IntranetOutRate**: the outbound traffic over the internal network. Unit: byte.
        self.metric_name = metric_name
        # Indicates whether the metrics of the cluster or a node are queried. Valid values:
        # 
        # *   **CLUSTER**: The metrics of the cluster are queried.
        # *   **NODE**: The metrics of a node are queried.
        self.metric_type = metric_type
        # The monitored object.
        # 
        # *   If the **MetricType** parameter is set to **NODE**, the value of this parameter is the ID of the node that is monitored.****
        # *   If the **MetricType** parameter is set to **CLUSTER**, the value of this parameter is the ID of the dedicated cluster. You can obtain the ID by calling the ListDedicatedCluster operation.
        self.param = param
        # The monitoring interval. Unit: seconds. Minimum value: 15.
        self.period = period
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data_points:
            for v1 in self.data_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DataPoints'] = []
        if self.data_points is not None:
            for k1 in self.data_points:
                result['DataPoints'].append(k1.to_map() if k1 else None)

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.param is not None:
            result['Param'] = self.param

        if self.period is not None:
            result['Period'] = self.period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data_points = []
        if m.get('DataPoints') is not None:
            for k1 in m.get('DataPoints'):
                temp_model = main_models.DescribeMetricListResponseBodyDataPoints()
                self.data_points.append(temp_model.from_map(k1))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMetricListResponseBodyDataPoints(DaraModel):
    def __init__(
        self,
        statistics: float = None,
        timestamp: int = None,
    ):
        # The statistical value.
        self.statistics = statistics
        # The timestamp of the record. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

