# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosticMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metrics: List[main_models.DescribeDiagnosticMetricsResponseBodyMetrics] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The diagnostic metrics.
        self.metrics = metrics
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

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
        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeDiagnosticMetricsResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiagnosticMetricsResponseBodyMetrics(DaraModel):
    def __init__(
        self,
        description: str = None,
        guest_metric: bool = None,
        metric_category: str = None,
        metric_id: str = None,
        metric_name: str = None,
        resource_type: str = None,
        supported_operating_system: str = None,
    ):
        # The description of the diagnostic metric.
        self.description = description
        # Indicates whether the diagnostic metric needs to be assessed by running a Cloud Assistant command in a guest operating system.
        self.guest_metric = guest_metric
        # The category of the diagnostic metric.
        self.metric_category = metric_category
        # The ID of the diagnostic metric.
        self.metric_id = metric_id
        # The name of the diagnostic metric.
        self.metric_name = metric_name
        # The resource type supported by the diagnostic metric.
        self.resource_type = resource_type
        # The operating system type supported by the diagnostic metric. Valid values:
        # 
        # *   Windows
        # *   Linux
        # *   All: Windows and Linux
        self.supported_operating_system = supported_operating_system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.guest_metric is not None:
            result['GuestMetric'] = self.guest_metric

        if self.metric_category is not None:
            result['MetricCategory'] = self.metric_category

        if self.metric_id is not None:
            result['MetricId'] = self.metric_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.supported_operating_system is not None:
            result['SupportedOperatingSystem'] = self.supported_operating_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GuestMetric') is not None:
            self.guest_metric = m.get('GuestMetric')

        if m.get('MetricCategory') is not None:
            self.metric_category = m.get('MetricCategory')

        if m.get('MetricId') is not None:
            self.metric_id = m.get('MetricId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SupportedOperatingSystem') is not None:
            self.supported_operating_system = m.get('SupportedOperatingSystem')

        return self

