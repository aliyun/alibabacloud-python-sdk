# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListSpecificationsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSpecificationsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSpecificationsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSpecificationsResponseBodyItems(DaraModel):
    def __init__(
        self,
        class_: str = None,
        cores: int = None,
        memory: int = None,
        shard: int = None,
        specification: str = None,
        storage: int = None,
    ):
        self.class_ = class_
        self.cores = cores
        self.memory = memory
        self.shard = shard
        # `RenderingSpec`
        self.specification = specification
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.shard is not None:
            result['Shard'] = self.shard

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Shard') is not None:
            self.shard = m.get('Shard')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

