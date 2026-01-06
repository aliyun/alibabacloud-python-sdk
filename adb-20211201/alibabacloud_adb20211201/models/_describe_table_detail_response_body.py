# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeTableDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        avg_size: str = None,
        items: main_models.DescribeTableDetailResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The average number of rows in a shard.
        self.avg_size = avg_size
        # The queried data distribution.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.avg_size is not None:
            result['AvgSize'] = self.avg_size

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AvgSize') is not None:
            self.avg_size = m.get('AvgSize')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeTableDetailResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

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
        # The shard ID. Only the numeric part of the shard name is returned.
        self.id = id
        # The number of rows in the table.
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

