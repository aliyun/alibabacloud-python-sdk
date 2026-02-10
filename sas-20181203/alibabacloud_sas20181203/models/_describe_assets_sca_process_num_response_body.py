# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetsScaProcessNumResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeAssetsScaProcessNumResponseBodyData] = None,
        request_id: str = None,
    ):
        # The statistical results.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAssetsScaProcessNumResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAssetsScaProcessNumResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        uuid: str = None,
    ):
        # The number of Java processes.
        # 
        # >  If no processes exist on the asset, no statistical result is returned.
        self.count = count
        # The UUID of the asset.
        # 
        # >  If no processes exist on the asset, no statistical result is returned.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

