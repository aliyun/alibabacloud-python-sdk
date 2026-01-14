# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDataItemListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetDataItemListResponseBodyData] = None,
        request_id: str = None,
    ):
        # Response parameters.
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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetDataItemListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDataItemListResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        period: int = None,
        unit: str = None,
    ):
        # The identifier of the data item.
        self.code = code
        # The name of the data item.
        self.name = name
        # Data filling method, 1: monthly value 2: annual value.
        self.period = period
        # The data item unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.name is not None:
            result['name'] = self.name

        if self.period is not None:
            result['period'] = self.period

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

