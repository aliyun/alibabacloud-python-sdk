# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListInstancesMetricsOutput(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        metrics_list: List[main_models.InstanceMetricInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.metrics_list = metrics_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.metrics_list:
            for v1 in self.metrics_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['metricsList'] = []
        if self.metrics_list is not None:
            for k1 in self.metrics_list:
                result['metricsList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.metrics_list = []
        if m.get('metricsList') is not None:
            for k1 in m.get('metricsList'):
                temp_model = main_models.InstanceMetricInfo()
                self.metrics_list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

