# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeTableDetailResponseBody(DaraModel):
    def __init__(
        self,
        avg_size: int = None,
        items: main_models.DescribeTableDetailResponseBodyItems = None,
        request_id: str = None,
    ):
        # The average number of rows in partitions.
        self.avg_size = avg_size
        # The queried shard.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_size is not None:
            result['AvgSize'] = self.avg_size

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgSize') is not None:
            self.avg_size = m.get('AvgSize')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeTableDetailResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTableDetailResponseBodyItems(DaraModel):
    def __init__(
        self,
        shard: List[main_models.DescribeTableDetailResponseBodyItemsShard] = None,
    ):
        # The queried shards.
        self.shard = shard

    def validate(self):
        if self.shard:
            for v1 in self.shard:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Shard'] = []
        if self.shard is not None:
            for k1 in self.shard:
                result['Shard'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shard = []
        if m.get('Shard') is not None:
            for k1 in m.get('Shard'):
                temp_model = main_models.DescribeTableDetailResponseBodyItemsShard()
                self.shard.append(temp_model.from_map(k1))

        return self

class DescribeTableDetailResponseBodyItemsShard(DaraModel):
    def __init__(
        self,
        id: int = None,
        size: int = None,
    ):
        # The partition ID. Only the numeric part of the partition name is returned.
        self.id = id
        # The number of rows in the partition.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

