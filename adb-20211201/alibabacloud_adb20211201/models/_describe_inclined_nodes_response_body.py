# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeInclinedNodesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeInclinedNodesResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The queried storage nodes.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeInclinedNodesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInclinedNodesResponseBodyItems(DaraModel):
    def __init__(
        self,
        disk_usage_ratio: str = None,
        node: str = None,
    ):
        # The disk usage of the storage node.
        self.disk_usage_ratio = disk_usage_ratio
        # The number of the storage node.
        self.node = node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_usage_ratio is not None:
            result['DiskUsageRatio'] = self.disk_usage_ratio

        if self.node is not None:
            result['Node'] = self.node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsageRatio') is not None:
            self.disk_usage_ratio = m.get('DiskUsageRatio')

        if m.get('Node') is not None:
            self.node = m.get('Node')

        return self

