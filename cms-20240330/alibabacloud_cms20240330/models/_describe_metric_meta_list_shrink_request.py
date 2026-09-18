# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricMetaListShrinkRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        category: str = None,
        keywords: str = None,
        labels_shrink: str = None,
        meta_format: str = None,
        metric_name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language.
        self.aliyun_lang = aliyun_lang
        # The category.
        self.category = category
        # The keyword.
        self.keywords = keywords
        # Filters resources by label. The following labels are available:
        # - metricCategory: the metric category description.
        # - alertEnable: specifies whether alerting is required.
        # - alertUnit: the recommended alert unit.
        # - unitFactor: the unit conversion factor.
        # - minAlertPeriod: the minimum alert period.
        # - productCategory: the product type category.
        self.labels_shrink = labels_shrink
        # The metadata source. Valid values:
        # 
        # - CMS: CloudMonitor Basic monitoring metrics.
        # - PROM_BASIC: Prometheus CloudMonitor Basic monitoring metrics.
        self.meta_format = meta_format
        # The metric name.
        self.metric_name = metric_name
        # The namespace, which is used to distinguish between services.
        self.namespace = namespace
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 2000.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        if self.category is not None:
            result['category'] = self.category

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
        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        if m.get('category') is not None:
            self.category = m.get('category')

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

