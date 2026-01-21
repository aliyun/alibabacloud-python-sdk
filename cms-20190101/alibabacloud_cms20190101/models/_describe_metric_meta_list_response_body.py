# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricMetaListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        resources: main_models.DescribeMetricMetaListResponseBodyResources = None,
        success: bool = None,
        total_count: str = None,
    ):
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The configuration of the metrics in the resources.
        self.resources = resources
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeMetricMetaListResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMetricMetaListResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeMetricMetaListResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeMetricMetaListResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeMetricMetaListResponseBodyResourcesResource(DaraModel):
    def __init__(
        self,
        description: str = None,
        dimensions: str = None,
        labels: str = None,
        metric_name: str = None,
        namespace: str = None,
        periods: str = None,
        statistics: str = None,
        unit: str = None,
    ):
        # The metric description.
        self.description = description
        # The monitoring dimensions of the resource. Multiple monitoring dimensions are separated with commas (,).
        self.dimensions = dimensions
        # The tags of the metric, including one or more JSON strings.
        # 
        # Format: `[{"name":"tag key","value":"tag value"}]`. The `name` can be repeated. The following tags are available:
        # 
        # *   metricCategory: the category of the metric.
        # *   alertEnable: indicates whether to report alerts for the metric.
        # *   alertUnit: the unit of the metric in the alerts.
        # *   unitFactor: the factor for metric unit conversion.
        # *   minAlertPeriod: the minimum interval at which the alert is reported.
        # *   productCategory: the category of the service.
        self.labels = labels
        # The metric name.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        self.namespace = namespace
        # The statistical periods of the metric. Multiple statistical periods are separated with commas (,).
        # 
        # Unit: seconds.
        self.periods = periods
        # The statistical method. Multiple statistical methods are separated with commas (,).
        self.statistics = statistics
        # The unit of the metric.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.periods is not None:
            result['Periods'] = self.periods

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Periods') is not None:
            self.periods = m.get('Periods')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

