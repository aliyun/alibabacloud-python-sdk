# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricMetaListShrinkRequest(DaraModel):
    def __init__(
        self,
        labels_shrink: str = None,
        meta_format: str = None,
        metric_name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.labels_shrink = labels_shrink
        self.meta_format = meta_format
        self.metric_name = metric_name
        self.namespace = namespace
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

