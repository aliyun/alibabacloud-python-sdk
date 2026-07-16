# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class DescribeProductDataRedundancyTypeStatResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeProductDataRedundancyTypeStatResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The unique request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeProductDataRedundancyTypeStatResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProductDataRedundancyTypeStatResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeProductDataRedundancyTypeStatResponseBodyDataContent] = None,
    ):
        # The list of records returned by the request.
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeProductDataRedundancyTypeStatResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        return self

class DescribeProductDataRedundancyTypeStatResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        resource_count: int = None,
        storage_class: str = None,
    ):
        # The data redundancy type.
        self.data_redundancy_type = data_redundancy_type
        # The resource count.
        self.resource_count = resource_count
        # The storage class.
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

