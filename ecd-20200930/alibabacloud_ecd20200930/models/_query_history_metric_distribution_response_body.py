# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryMetricDistributionResponseBody(DaraModel):
    def __init__(
        self,
        distribution_list: List[main_models.QueryHistoryMetricDistributionResponseBodyDistributionList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.distribution_list = distribution_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.distribution_list:
            for v1 in self.distribution_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DistributionList'] = []
        if self.distribution_list is not None:
            for k1 in self.distribution_list:
                result['DistributionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.distribution_list = []
        if m.get('DistributionList') is not None:
            for k1 in m.get('DistributionList'):
                temp_model = main_models.QueryHistoryMetricDistributionResponseBodyDistributionList()
                self.distribution_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryHistoryMetricDistributionResponseBodyDistributionList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
        max: float = None,
        min: float = None,
    ):
        self.count = count
        self.label = label
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

