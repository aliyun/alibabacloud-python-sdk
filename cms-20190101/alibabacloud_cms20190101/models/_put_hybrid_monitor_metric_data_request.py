# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutHybridMonitorMetricDataRequest(DaraModel):
    def __init__(
        self,
        metric_list: List[main_models.PutHybridMonitorMetricDataRequestMetricList] = None,
        namespace: str = None,
        region_id: str = None,
    ):
        # The monitoring data.
        # 
        # Valid values of N: 1 to 100.
        # 
        # This parameter is required.
        self.metric_list = metric_list
        # The name of the namespace.
        # 
        # For information about how to obtain the name of a namespace, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.namespace = namespace
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

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_list = []
        if m.get('MetricList') is not None:
            for k1 in m.get('MetricList'):
                temp_model = main_models.PutHybridMonitorMetricDataRequestMetricList()
                self.metric_list.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class PutHybridMonitorMetricDataRequestMetricList(DaraModel):
    def __init__(
        self,
        labels: List[main_models.PutHybridMonitorMetricDataRequestMetricListLabels] = None,
        name: str = None,
        ts: int = None,
        value: str = None,
    ):
        # The tags of the metric.
        # 
        # Valid values of N: 1 to 100.
        self.labels = labels
        # The metric name.
        # 
        # Valid values of N: 1 to 100.
        # 
        # The name can contain letters, digits, and underscores (_). The name must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The time when the monitoring data is imported. The value is a timestamp.
        # 
        # Valid values of N: 1 to 100.
        # 
        # Unit: milliseconds. By default, the current time is used.
        self.ts = ts
        # The value of the metric.
        # 
        # Valid values of N: 1 to 100.
        # 
        # The value must be an integer or a floating-point number.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.ts is not None:
            result['TS'] = self.ts

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.PutHybridMonitorMetricDataRequestMetricListLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TS') is not None:
            self.ts = m.get('TS')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class PutHybridMonitorMetricDataRequestMetricListLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the metric.
        # 
        # Valid values of N: 1 to 100.
        # 
        # The key can contain letters, digits, and underscores (_). The key must start with a letter or an underscore (_).
        # 
        # >  You must specify both the Key and Value parameters.
        self.key = key
        # The tag value of the metric.
        # 
        # Valid values of N: 1 to 100.
        # 
        # >  You must specify both the Key and Value parameters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

