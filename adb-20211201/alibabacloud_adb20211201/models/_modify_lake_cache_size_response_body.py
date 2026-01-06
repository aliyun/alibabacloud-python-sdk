# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyLakeCacheSizeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ModifyLakeCacheSizeResponseBodyData = None,
        request_id: str = None,
    ):
        # The status code. The value 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ModifyLakeCacheSizeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyLakeCacheSizeResponseBodyData(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        data_size: int = None,
        instances: List[str] = None,
    ):
        # The size of the lake cache space. Unit: GB.
        self.capacity = capacity
        # The size of the data that occupies the lake cache space. Unit: GB.
        self.data_size = data_size
        # The clusters that share the lake cache space.
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.instances is not None:
            result['Instances'] = self.instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        return self

