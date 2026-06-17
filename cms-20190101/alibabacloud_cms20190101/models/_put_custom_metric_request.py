# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutCustomMetricRequest(DaraModel):
    def __init__(
        self,
        metric_list: List[main_models.PutCustomMetricRequestMetricList] = None,
        region_id: str = None,
    ):
        # The list of monitoring data.
        # 
        # This parameter is required.
        self.metric_list = metric_list
        self.region_id = region_id

    def validate(self):
        if self.metric_list:
            for v1 in self.metric_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricList'] = []
        if self.metric_list is not None:
            for k1 in self.metric_list:
                result['MetricList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_list = []
        if m.get('MetricList') is not None:
            for k1 in m.get('MetricList'):
                temp_model = main_models.PutCustomMetricRequestMetricList()
                self.metric_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class PutCustomMetricRequestMetricList(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        group_id: str = None,
        metric_name: str = None,
        period: str = None,
        time: str = None,
        type: str = None,
        values: str = None,
    ):
        # The dimension map, which is used to query monitoring data of a specified resource. Valid values of N: 1 to 21.
        # 
        # Format: a collection of key-value pairs. A commonly used key-value pair collection is: `{"Key":"Value"}`.
        # 
        # The length of Key and Value is 1 to 64 characters. Characters beyond the first 64 are truncated.
        # 
        # The values of Key and Value can contain letters, digits, periods (.), hyphens (-), underscores (_), forward slashes (/), and backslashes (\\).
        # 
        # > Dimensions must be passed in as a JSON string that represents the map object, and must be passed in order.
        # 
        # This parameter is required.
        self.dimensions = dimensions
        # The ID of the application group. Valid values of N: 1 to 21.
        # 
        # > If the metric does not belong to any application group, enter 0.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the metric. Valid values of N: 1 to 21. For more information, see [Metrics of cloud services](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The aggregation period. Valid values of N: 1 to 21. Unit: seconds. Valid values: 60 and 300.
        # 
        # > If the type of the reported value is 1, you must set this parameter.
        self.period = period
        # The time when the metric occurred. Valid values of N: 1 to 21. The following two types of values are supported:
        # - UTC time. Format: YYYY-MM-DDThh:mm:ssZ. For example: 20171012T132456.888+0800.
        # - A Long-type timestamp. For example: 1508136760000.
        self.time = time
        # The type of the reported value. Valid values of N: 1 to 21. Valid values:
        # 
        # - 0: raw data.
        # - 1: aggregate data.
        # 
        # > When you report aggregate data, we recommend that you report both data with a period of 60 seconds and data with a period of 300 seconds. Otherwise, monitoring data cannot be queried for a time span of more than 7 days.
        # 
        # This parameter is required.
        self.type = type
        # The collection of metric values. Valid values of N: 1 to 21.
        # 
        # > If the type of the reported value is 0, the raw values are reported. CloudMonitor aggregates raw values into multiple values, such as maximum, count, and sum, by period.
        # 
        # This parameter is required.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

