# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricMetaListShrinkRequest(DaraModel):
    def __init__(
        self,
        keywords: str = None,
        labels_shrink: str = None,
        meta_format: str = None,
        metric_name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keywords = keywords
        # The labels used to filter resources. The following labels are supported:
        # 
        # - `metricCategory`: The metric category.
        # 
        # - `alertEnable`: Indicates whether to enable alerts.
        # 
        # - `alertUnit`: The recommended unit for alerts.
        # 
        # - `unitFactor`: The unit conversion factor.
        # 
        # - `minAlertPeriod`: The minimum alert period.
        # 
        # - `productCategory`: The product category.
        self.labels_shrink = labels_shrink
        # The source of the metadata. Valid values: `CMS` for CloudMonitor metrics and `PROM_BASIC` for basic Prometheus metrics.
        self.meta_format = meta_format
        # The name of the metric.
        self.metric_name = metric_name
        # The namespace of the product.
        self.namespace = namespace
        # The number of the page to return. Default value: `1`.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: `2000`.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['keywords'] = self.keywords

        if self.labels_shrink is not None:
            result['labels'] = self.labels_shrink

        if self.meta_format is not None:
            result['metaFormat'] = self.meta_format

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')

        if m.get('labels') is not None:
            self.labels_shrink = m.get('labels')

        if m.get('metaFormat') is not None:
            self.meta_format = m.get('metaFormat')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

