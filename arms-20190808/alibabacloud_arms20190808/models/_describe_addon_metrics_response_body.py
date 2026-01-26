# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeAddonMetricsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeAddonMetricsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The metric details.
        self.data = data
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAddonMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAddonMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        group: str = None,
        labels: List[main_models.DescribeAddonMetricsResponseBodyDataLabels] = None,
        metrics: List[main_models.DescribeAddonMetricsResponseBodyDataMetrics] = None,
    ):
        # The metric group.
        self.group = group
        # The tags.
        self.labels = labels
        # The metrics.
        self.metrics = metrics

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DescribeAddonMetricsResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeAddonMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k1))

        return self

class DescribeAddonMetricsResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        description: str = None,
        labels: List[main_models.DescribeAddonMetricsResponseBodyDataMetricsLabels] = None,
        metric: str = None,
        type: str = None,
        unit: str = None,
    ):
        # The description of the metric.
        self.description = description
        # The tags.
        self.labels = labels
        # The metric name.
        self.metric = metric
        # The type of the metric.
        self.type = type
        # The unit of the metric.
        self.unit = unit

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
        if self.description is not None:
            result['Description'] = self.description

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.type is not None:
            result['Type'] = self.type

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DescribeAddonMetricsResponseBodyDataMetricsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribeAddonMetricsResponseBodyDataMetricsLabels(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        source: str = None,
    ):
        # The description of the tag.
        self.description = description
        # The tag key.
        self.key = key
        # The source of the tag.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class DescribeAddonMetricsResponseBodyDataLabels(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        source: str = None,
    ):
        # The description of the tag.
        self.description = description
        # The tag key.
        self.key = key
        # The source of the tag.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

