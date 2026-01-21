# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricMetaListRequest(DaraModel):
    def __init__(
        self,
        labels: str = None,
        metric_name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The tags for filtering metrics. Specify a JSON string.
        # 
        # Format: ` [{"name":"tag key","value":"tag value"},{"name":"tag key","value":"tag value"}]  `. The following tags are available:
        # 
        # *   metricCategory: the category of the metric.
        # *   alertEnable: specifies whether to report alerts for the metric.
        # *   alertUnit: the unit of the metric in the alerts.
        # *   unitFactor: the factor for metric unit conversion.
        # *   minAlertPeriod: the minimum interval at which the alert is reported.
        # *   productCategory: the category of the service.
        self.labels = labels
        # The metric name. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 30.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

