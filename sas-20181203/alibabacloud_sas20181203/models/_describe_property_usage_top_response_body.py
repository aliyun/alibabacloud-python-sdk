# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyUsageTopResponseBody(DaraModel):
    def __init__(
        self,
        item_count: int = None,
        request_id: str = None,
        top_statistic_items: List[main_models.DescribePropertyUsageTopResponseBodyTopStatisticItems] = None,
        type: str = None,
    ):
        # The number of fingerprints.
        self.item_count = item_count
        # The request ID.
        self.request_id = request_id
        # The statistical results.
        self.top_statistic_items = top_statistic_items
        # The type of the asset fingerprint. Valid value:
        # 
        # *   **port**: port
        # *   **process**: process
        # *   **software**: software
        # *   **user**: account
        # *   **sca**: middleware
        self.type = type

    def validate(self):
        if self.top_statistic_items:
            for v1 in self.top_statistic_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_count is not None:
            result['ItemCount'] = self.item_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopStatisticItems'] = []
        if self.top_statistic_items is not None:
            for k1 in self.top_statistic_items:
                result['TopStatisticItems'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_statistic_items = []
        if m.get('TopStatisticItems') is not None:
            for k1 in m.get('TopStatisticItems'):
                temp_model = main_models.DescribePropertyUsageTopResponseBodyTopStatisticItems()
                self.top_statistic_items.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribePropertyUsageTopResponseBodyTopStatisticItems(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # The quantity.
        self.count = count
        # The statistical item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

